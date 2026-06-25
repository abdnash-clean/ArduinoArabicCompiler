# backend/tests/test_backend.py
# =============================================================================
#  اختبارات دخان للمرحلة الخلفية (Backend Smoke Tests)
# -----------------------------------------------------------------------------
#  تتحقق هذه الاختبارات من:
#    - تسجيل هدف AVR وإنشاء TargetMachine.
#    - تحسين IR وإصدار كائن AVR صالح.
#    - تجميع طبقة الربط (glue) عند توفر AVR toolchain.
#    - اختيار overload الصحيح لـ Serial.print.
#
#  لا تحتاج هذه الاختبارات إلى لوحة Arduino حقيقية.
# =============================================================================

import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

# التأكد من إمكانية استيراد الوحدات من جذر المشروع
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from backend.avr_target import (
    AVR_CPU,
    AVR_DATALAYOUT,
    AVR_TRIPLE,
    make_avr_target_machine,
    make_host_target_machine,
)
from backend import codegen
from backend.optimizer import Optimizer
from backend.linker import build_glue, link, elf_to_hex, LinkError, _find_executable, _guess_arduino_paths


MINIMAL_IR = """
target triple = "avr-atmel-none"
target datalayout = "e-P1-p:16:8-i8:8-i16:8-i32:8-i64:8-f32:8-f64:8-n8-a:8"

define void @setup() {
entry:
  ret void
}

define void @loop() {
entry:
  ret void
}
""".strip()


class TestAVRTTarget(unittest.TestCase):
    """اختبارات إعداد آلة الهدف AVR."""

    def test_triple_and_cpu_constants(self):
        self.assertEqual(AVR_TRIPLE, "avr-atmel-none")
        self.assertEqual(AVR_CPU, "atmega328p")
        self.assertIn("p:16:8", AVR_DATALAYOUT)

    def test_avr_target_machine_available(self):
        tm = make_avr_target_machine()
        self.assertIsNotNone(
            tm,
            "خلفية AVR غير متوفرة في llvmlite; تأكد من أن النسخة بنيت مع دعم AVR."
        )

    def test_host_target_machine_available(self):
        tm = make_host_target_machine()
        self.assertIsNotNone(tm)


class TestOptimizer(unittest.TestCase):
    """اختبارات تحسين LLVM IR."""

    def test_optimize_returns_ir_string(self):
        opt = Optimizer(opt_level=1, size_level=0, verbose=False)
        result = opt.optimize(MINIMAL_IR)
        self.assertIsInstance(result, str)
        self.assertIn("define void @setup", result)
        self.assertIn("define void @loop", result)

    def test_optimize_sets_avr_target_info(self):
        opt = Optimizer(opt_level=1, size_level=0, verbose=False)
        result = opt.optimize(MINIMAL_IR)
        self.assertIn(f'target triple = "{AVR_TRIPLE}"', result)
        self.assertIn(f'target datalayout = "{AVR_DATALAYOUT}"', result)


class TestCodegen(unittest.TestCase):
    """اختبارات توليد التجميع / ملف الكائن."""

    def setUp(self):
        self.opt = Optimizer(opt_level=1, size_level=0, verbose=False)
        self.optimized_ir = self.opt.optimize(MINIMAL_IR)

    def test_emit_assembly_returns_avr_assembly(self):
        asm = codegen.emit_assembly(self.optimized_ir, opt_level=1)
        self.assertIsInstance(asm, str)
        # AVR mnemonics we expect to see in even the smallest program
        self.assertIn("ret", asm)

    def test_emit_object_returns_avr_elf(self):
        obj = codegen.emit_object(self.optimized_ir, opt_level=1)
        self.assertIsInstance(obj, bytes)
        self.assertGreater(len(obj), 0)
        # ELF magic for a 32-bit LSB relocatable object
        self.assertEqual(obj[:4], b"\x7fELF")

    def test_write_object_creates_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            out_path = os.path.join(tmp, "test.o")
            codegen.write_object(self.optimized_ir, out_path, opt_level=1)
            self.assertTrue(os.path.exists(out_path))
            with open(out_path, "rb") as f:
                self.assertEqual(f.read()[:4], b"\x7fELF")


class TestLinker(unittest.TestCase):
    """اختبارات الربط — تُتخطى عندما لا يكون AVR toolchain متوفراً."""

    @classmethod
    def setUpClass(cls):
        cls.has_avr_toolchain = _find_executable("avr-g++") is not None

    def _optimized_ir(self):
        return Optimizer(opt_level=1, size_level=0, verbose=False).optimize(MINIMAL_IR)

    @unittest.skipUnless(
        _find_executable("avr-g++"),
        "AVR toolchain غير متوفر على هذه الآلة."
    )
    def test_build_glue_produces_object(self):
        paths = _guess_arduino_paths()
        with tempfile.TemporaryDirectory() as tmp:
            glue_o = os.path.join(tmp, "glue.o")
            built = build_glue(
                glue_cpp=str(PROJECT_ROOT / "runtime" / "arduino_glue.cpp"),
                out_o=glue_o,
                core_inc=str(paths.get("core_inc")) if paths.get("core_inc") else None,
                variant_inc=str(paths.get("variant_inc")) if paths.get("variant_inc") else None,
            )
            self.assertTrue(built.exists())

    @unittest.skipUnless(
        _find_executable("avr-g++") and _find_executable("avr-objcopy"),
        "AVR toolchain غير متوفر على هذه الآلة."
    )
    def test_glue_compiles_even_without_serial_usage(self):
        # يضمن أن طبقة الربط تُترجم بمفردها دون أخطاء بناء
        paths = _guess_arduino_paths()
        with tempfile.TemporaryDirectory() as tmp:
            glue_o = os.path.join(tmp, "glue.o")
            build_glue(
                glue_cpp=str(PROJECT_ROOT / "runtime" / "arduino_glue.cpp"),
                out_o=glue_o,
                core_inc=str(paths.get("core_inc")) if paths.get("core_inc") else None,
                variant_inc=str(paths.get("variant_inc")) if paths.get("variant_inc") else None,
            )
            self.assertTrue(os.path.exists(glue_o))


class TestSerialOverloadDispatch(unittest.TestCase):
    """اختبار اختيار overload الصحيح لـ Serial.print."""

    def test_builtins_contain_typed_serial_overloads(self):
        from backend.ir_generator import LLVMIRGenerator
        gen = LLVMIRGenerator()
        self.assertIn("سيريال_اطبع_صحيح", gen.builtins)
        self.assertIn("سيريال_اطبع_عشري", gen.builtins)
        self.assertIn("سيريال_اطبع_نص", gen.builtins)


class TestBuiltinNameConsistency(unittest.TestCase):
    """التأكد من توافق أسماء الدوال المدمجة بين الـ semantic والـ IR generator."""

    def test_all_semantic_core_functions_exist_in_ir(self):
        from semantic.builtins_registry import CORE_FUNCTIONS
        from backend.ir_generator import LLVMIRGenerator

        gen = LLVMIRGenerator()
        for name in CORE_FUNCTIONS:
            self.assertIn(
                name, gen.builtins,
                f"الدالة المدمجة '{name}' موجودة في السجل الدلالي لكن غير معرّفة في IR generator."
            )

    def test_all_semantic_serial_functions_exist_in_ir(self):
        from semantic.builtins_registry import LIBRARIES
        from backend.ir_generator import LLVMIRGenerator

        gen = LLVMIRGenerator()
        serial_funcs = LIBRARIES.get("سيريال", {})
        for name in serial_funcs:
            if name == "سيريال_اطبع":
                # تم استبدالها بـ overloads في IR generator
                self.assertIn("سيريال_اطبع_صحيح", gen.builtins)
                self.assertIn("سيريال_اطبع_عشري", gen.builtins)
                self.assertIn("سيريال_اطبع_نص", gen.builtins)
            else:
                self.assertIn(
                    name, gen.builtins,
                    f"دالة السيريال '{name}' موجودة في السجل الدلالي لكن غير معرّفة في IR generator."
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
