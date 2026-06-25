# backend/avr_target.py
# =============================================================================
#  إعداد آلة الهدف AVR / ATmega328P
# -----------------------------------------------------------------------------
#  يتولّى هذا الملف تسجيل أهداف LLVM وجميع طابعات التجميع، وإنشاء
#  TargetMachine المناسب للمتحكم ATmega328P (Arduino Uno / Nano).
#
#  llvmlite 0.47.0
# =============================================================================

import warnings
import llvmlite.binding as llvm

AVR_TRIPLE = "avr-atmel-none"
AVR_CPU = "atmega328p"
# مخطط بيانات AVR: مؤشرات 16-بت، محاذاة 8-بت
AVR_DATALAYOUT = "e-P1-p:16:8-i8:8-i16:8-i32:8-i64:8-f32:8-f64:8-n8-a:8"

_targets_initialized = False


def ensure_targets_initialized() -> None:
    """تسجيل كل أهداف LLVM وطابعات التجميع مرة واحدة لكل العملية.

    AVR هدف غير أصلي (cross target)، لذا نحتاج `initialize_all_targets()`
    و `initialize_all_asmprinters()` بدلاً من `initialize_native_target()`.
    """
    global _targets_initialized
    if _targets_initialized:
        return

    # إذا كان AVR مسجّلاً أصلاً فلا داعي لإعادة التسجيل
    try:
        llvm.Target.from_triple(AVR_TRIPLE)
        _targets_initialized = True
        return
    except RuntimeError:
        pass

    for fn_name in ("initialize_all_targets", "initialize_all_asmprinters"):
        fn = getattr(llvm, fn_name, None)
        if fn is None:
            continue
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                fn()
        except Exception:
            pass

    _targets_initialized = True


def make_avr_target_machine(opt_level: int = 2):
    """إنشاء TargetMachine لـ AVR ATmega328P.

    تعيد None إذا كانت خلفية AVR غير متوفرة في نسخة llvmlite المثبتة.
    """
    ensure_targets_initialized()
    try:
        target = llvm.Target.from_triple(AVR_TRIPLE)
        return target.create_target_machine(
            cpu=AVR_CPU,
            features="",
            opt=opt_level,
            reloc="static",      # المتحكمات لا تستخدم كوداً مستقل الموقع
            codemodel="small",
        )
    except RuntimeError:
        return None


def make_host_target_machine():
    """إنشاء TargetMachine لجهاز المطور (هدف احتياطي للتحسين فقط)."""
    ensure_targets_initialized()
    target = llvm.Target.from_triple(llvm.get_process_triple())
    return target.create_target_machine()


def apply_avr_target_info(mod) -> None:
    """ضبط triple و data layout الخاصين بـ AVR على وحدة LLVM."""
    try:
        mod.triple = AVR_TRIPLE
        mod.data_layout = AVR_DATALAYOUT
    except Exception:
        pass
