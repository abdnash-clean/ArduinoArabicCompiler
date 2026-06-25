# backend/optimizer.py
# =============================================================================
#  المرحلة الوسطى (Middle-End): تحسين الكود الوسيط LLVM IR
# -----------------------------------------------------------------------------
#  يأخذ نصّ الـ LLVM IR القادم من مولّد الكود (ir_generator)، يطبّق
#  تمريرات التحسين (Optimization Passes)، ثم يعيد الكود المحسّن.
#
#  الهدف: AVR / ATmega328P (Arduino Uno) — معالج 8-بت محدود الفلاش.
#  llvmlite 0.47.0
#
#  ملاحظة: إعداد آلة الهدف و توليد التجميع / ملف الكائن انتقلا إلى:
#    - backend/avr_target.py
#    - backend/codegen.py
# =============================================================================

import re
import llvmlite.binding as llvm

from backend.avr_target import (
    make_avr_target_machine,
    make_host_target_machine,
    apply_avr_target_info,
)


# =============================================================================
#  إصلاح خاص بخلفية AVR التجريبية في LLVM/llvmlite
# -----------------------------------------------------------------------------
#  خلفية AVR تنهار بـ: Assertion `isUIntN(BitWidth, val)` عند توليد التعليمة:
#        icmp ult iW X, C     حيث C ثابت كبير (بت الإشارة = 1)
#  الحل: تحويل المقارنة غير الإشارية إلى إشارية بقلب بت الإشارة على الطرفين.
# =============================================================================

_ICMP_ULT_RE = re.compile(
    r"^(?P<indent>[ \t]*)"
    r"(?P<dst>%[A-Za-z0-9_.$-]+)\s*=\s*"
    r"icmp\s+(?:samesign\s+)?ult\s+"
    r"i(?P<bits>\d+)\s+"
    r"(?P<lhs>%[A-Za-z0-9_.$-]+)\s*,\s*"
    r"(?P<rhs>-?\d+)"
    r"(?P<tail>.*)$"
)


def _avr_fix_unsigned_icmp(text):
    """يحوّل 'icmp ult iW X, C' ذات الثابت الكبير إلى مقارنة إشارية مكافئة."""
    out = []
    count = 0
    for line in text.split("\n"):
        m = _ICMP_ULT_RE.match(line)
        if m is None:
            out.append(line)
            continue
        bits = int(m.group("bits"))
        rhs = int(m.group("rhs"))
        mask = (1 << bits) - 1
        uval = rhs & mask
        if bits < 8 or not (uval >> (bits - 1)):
            out.append(line)
            continue
        signbit = 1 << (bits - 1)
        biased_u = uval ^ signbit
        biased_s = biased_u if biased_u < signbit else biased_u - (1 << bits)
        signbit_s = -signbit
        ty = "i%d" % bits
        bias = m.group("dst") + ".avrbias"
        out.append("%s%s = xor %s %s, %d" % (
            m.group("indent"), bias, ty, m.group("lhs"), signbit_s))
        out.append("%s%s = icmp slt %s %s, %d%s" % (
            m.group("indent"), m.group("dst"), ty, bias, biased_s, m.group("tail")))
        count += 1
    return "\n".join(out), count


class Optimizer:
    """
    محسّن الكود الوسيط.

    opt_level  : مستوى تحسين الأداء (0-3).
    size_level : مستوى تقليل الحجم (0,1,2). مهم جداً لـ AVR محدود الفلاش.

    الموصى به للمتحكمات: opt_level=2, size_level=1  (أي -Os).
    """

    def __init__(self, opt_level: int = 2, size_level: int = 1, verbose: bool = False):
        self.opt_level = opt_level
        self.size_level = size_level
        self.verbose = verbose

    # -- الدالة الرئيسية: تحسين الكود الوسيط -----------------------------
    def optimize(self, llvm_ir: str) -> str:
        # 1) تحليل + تحقق قبلي
        mod = llvm.parse_assembly(llvm_ir)
        mod.verify()

        # 2) ضبط معلومات الهدف
        apply_avr_target_info(mod)

        # 3) تشغيل التحسين
        try:
            self._run_new_pass_manager(mod)
        except AttributeError:
            self._run_legacy_pass_manager(mod)

        # 4) تحقق بعدي
        mod.verify()

        # 5) إصلاح خاص بخلفية AVR
        fixed_text, n_fixed = _avr_fix_unsigned_icmp(str(mod))
        if n_fixed:
            if self.verbose:
                print(f"[AVR] حُوّلت {n_fixed} مقارنة 'ult' بثابت كبير إلى مقارنة إشارية.")
            mod = llvm.parse_assembly(fixed_text)
            mod.verify()

        # 6) إرجاع الكود المحسّن
        return str(mod)

    # -- مدير التمرير الجديد (New Pass Manager) ---------------------------
    def _run_new_pass_manager(self, mod):
        tm = make_avr_target_machine(self.opt_level) or make_host_target_machine()

        pto = llvm.create_pipeline_tuning_options(
            speed_level=self.opt_level,
            size_level=self.size_level,
        )
        for attr, val in (
            ("loop_vectorization", False),
            ("slp_vectorization", False),
            ("loop_interleaving", False),
            ("loop_unrolling", self.size_level == 0),
        ):
            try:
                setattr(pto, attr, val)
            except (AttributeError, TypeError):
                pass

        pb = llvm.create_pass_builder(tm, pto)
        mpm = pb.getModulePassManager()
        mpm.run(mod, pb)

    # -- مدير التمرير القديم (Legacy) -----------------------------------
    def _run_legacy_pass_manager(self, mod):
        pmb = llvm.create_pass_manager_builder()
        pmb.opt_level = self.opt_level
        pmb.size_level = self.size_level
        for attr, val in (("loop_vectorize", False), ("slp_vectorize", False)):
            try:
                setattr(pmb, attr, val)
            except (AttributeError, TypeError):
                pass
        if self.size_level > 0:
            try:
                pmb.disable_unroll_loops = True
            except (AttributeError, TypeError):
                pass

        pm = llvm.create_module_pass_manager()
        tm = make_avr_target_machine(self.opt_level)
        if tm is not None:
            tm.add_analysis_passes(pm)
        pmb.populate(pm)
        pm.run(mod)


# تشغيل مستقل: python3 -m backend.optimizer input.ll [opt_level] [size_level] > output.ll
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("الاستخدام: python3 -m backend.optimizer <ملف.ll> [opt_level] [size_level]")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as fh:
        ir_text = fh.read()

    opt_lvl = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    size_lvl = int(sys.argv[3]) if len(sys.argv) > 3 else 1

    optimizer = Optimizer(opt_level=opt_lvl, size_level=size_lvl, verbose=True)
    print(optimizer.optimize(ir_text))
