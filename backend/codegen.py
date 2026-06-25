# backend/codegen.py
# =============================================================================
#  توليد التجميع / ملف الكائن من LLVM IR (Codegen)
# -----------------------------------------------------------------------------
#  يفترض هذا الملف أنّ IR المُمرَّر قد تم تحسينه مسبقاً عبر `backend.optimizer`.
#  لا يقوم بأي تحسين — فقط parse و emit.
# =============================================================================

import llvmlite.binding as llvm
from backend.avr_target import make_avr_target_machine


def _make_codegen_target_machine(opt_level: int = 2):
    tm = make_avr_target_machine(opt_level)
    if tm is None:
        raise RuntimeError(
            "لا يمكن توليد كود AVR: خلفية AVR غير متوفرة في هذه النسخة من llvmlite. "
            "استخدم llc/clang أو avr-gcc على الكود المحسّن بدلاً من ذلك."
        )
    return tm


def emit_assembly(llvm_ir: str, opt_level: int = 2) -> str:
    """يولّد لغة تجميع AVR من LLVM IR محسّن."""
    tm = _make_codegen_target_machine(opt_level)
    mod = llvm.parse_assembly(llvm_ir)
    mod.verify()
    return tm.emit_assembly(mod)


def emit_object(llvm_ir: str, opt_level: int = 2) -> bytes:
    """يولّد ملف كائن AVR (.o) من LLVM IR محسّن."""
    tm = _make_codegen_target_machine(opt_level)
    mod = llvm.parse_assembly(llvm_ir)
    mod.verify()
    return tm.emit_object(mod)


def write_object(llvm_ir: str, out_path: str, opt_level: int = 2) -> None:
    """يكتب ملف الكائن (.o) إلى القرص من LLVM IR محسّن."""
    with open(out_path, "wb") as fh:
        fh.write(emit_object(llvm_ir, opt_level))
