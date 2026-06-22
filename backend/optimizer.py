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
#  ملاحظة مهمة جداً حول تهيئة الأهداف (تغيّر في 0.47):
#    - الدالة initialize() (تهيئة الهدف الأصلي) أصبحت مهملة (deprecated)،
#      والتهيئة التلقائية تشملها — لكنها تشمل الهدف الأصلي (native) فقط.
#    - أهداف التصريف المتقاطع مثل AVR ما زالت تتطلب initialize_all_targets()
#      صراحةً (وهي ليست مهملة). لهذا نستدعيها قبل from_triple("avr-...").
#      بدونها تحصل على: "Unable to find target for this triple (no targets are registered)".
# =============================================================================

import warnings
import llvmlite.binding as llvm

# عنوان الهدف ومخطط البيانات الخاص بـ AVR
AVR_TRIPLE = "avr-atmel-none"
AVR_CPU = "atmega328p"
# مخطط بيانات AVR: المؤشرات 16-بت، المحاذاة 8-بت (بايت واحد)
AVR_DATALAYOUT = "e-P1-p:16:8-i8:8-i16:8-i32:8-i64:8-f32:8-f64:8-n8-a:8"


class Optimizer:
    """
    محسّن الكود الوسيط.

    opt_level  : مستوى تحسين الأداء (0-3).
    size_level : مستوى تقليل الحجم (0,1,2). مهم جداً لـ AVR محدود الفلاش:
                 1 ≈ -Os   و   2 ≈ -Oz

    الموصى به للمتحكمات: opt_level=2, size_level=1  (أي -Os).
    """

    # تُسجّل أهداف LLVM مرة واحدة فقط لكل العملية
    _targets_initialized = False

    @classmethod
    def _ensure_targets_initialized(cls):
        """تُسجّل كل خلفيات الأهداف (بما فيها AVR) مرة واحدة.

        في llvmlite 0.47 التهيئة التلقائية تشمل الهدف الأصلي (native) فقط.
        أهداف التصريف المتقاطع مثل AVR تحتاج initialize_all_targets() صراحةً.
        نتجنّب initialize() الأصلية (المهملة) ونكتفي بتسجيل كل الأهداف.
        """
        if cls._targets_initialized:
            return
        # إن كان AVR مسجّلاً أصلاً (مثلاً بسبب تهيئة سابقة) فلا حاجة لشيء
        try:
            llvm.Target.from_triple(AVR_TRIPLE)
            cls._targets_initialized = True
            return
        except RuntimeError:
            pass
        # تسجيل كل الأهداف + طابعات التجميع (مطلوبة لـ emit_object/emit_assembly)
        # نكتم أي تحذير إهمال احتياطيّاً (هذه الدوال غير مهملة لكن للأمان)
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
        cls._targets_initialized = True

    def __init__(self, opt_level: int = 2, size_level: int = 1, verbose: bool = False):
        self.opt_level = opt_level
        self.size_level = size_level
        self.verbose = verbose
        # تسجيل الأهداف (مطلوب لـ AVR — هدف غير أصلي)
        self._ensure_targets_initialized()

    # -- آلة هدف AVR (قد لا تكون خلفية AVR مضمّنة في llvmlite) --------------
    def _make_avr_target_machine(self):
        self._ensure_targets_initialized()
        try:
            target = llvm.Target.from_triple(AVR_TRIPLE)
            return target.create_target_machine(
                cpu=AVR_CPU,
                features="",
                opt=self.opt_level,
                reloc="static",     # المتحكمات لا تستخدم كوداً مستقل الموقع
                codemodel="small",
            )
        except RuntimeError as e:
            if self.verbose:
                print(f"[تحذير] خلفية AVR غير متوفرة في llvmlite: {e}")
                print("        سيتم تنفيذ التحسينات المستقلة عن الهدف فقط.")
            return None

    # -- آلة هدف احتياطية (هدف جهازك) — تكفي لتشغيل التحسينات -----
    def _make_host_target_machine(self):
        self._ensure_targets_initialized()
        # مدير التمرير الجديد يتطلب آلة هدف؛ والتحسينات مستقلة عن الهدف غالباً
        target = llvm.Target.from_triple(llvm.get_process_triple())
        return target.create_target_machine()

    # -- الدالة الرئيسية: تحسين الكود الوسيط ------------------------------
    def optimize(self, llvm_ir: str) -> str:
        # 1) تحليل + تحقق قبلي (يكشف أخطاء مولّد الكود)
        mod = llvm.parse_assembly(llvm_ir)
        mod.verify()

        # 2) ضبط معلومات الهدف (تساعد المحسّن على أحجام ومحاذاة صحيحة)
        try:
            mod.triple = AVR_TRIPLE
            mod.data_layout = AVR_DATALAYOUT
        except Exception:
            pass

        # 3) تشغيل التحسين: نجرّب مدير التمرير الجديد، وإن غاب نسقط للقديم
        try:
            self._run_new_pass_manager(mod)
        except AttributeError:
            self._run_legacy_pass_manager(mod)

        # 4) تحقق بعدي ثم إرجاع الكود المحسّن
        mod.verify()
        return str(mod)

    # -- مدير التمرير الجديد (New Pass Manager) — المسار الافتراضي -------
    def _run_new_pass_manager(self, mod):
        tm = self._make_avr_target_machine() or self._make_host_target_machine()

        pto = llvm.create_pipeline_tuning_options(
            speed_level=self.opt_level,
            size_level=self.size_level,
        )
        # لا فائدة من المتجهات/فكّ الحلقات على معالج 8-بت محدود الفلاش
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

    # -- مدير التمرير القديم (Legacy) — سقوط احتياطي فقط ----------------
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
        tm = self._make_avr_target_machine()
        if tm is not None:
            tm.add_analysis_passes(pm)
        pmb.populate(pm)
        pm.run(mod)

    # -- جسر إلى المرحلة الخلفية: توليد التجميع -----------------------------
    def emit_assembly(self, llvm_ir: str) -> str:
        """يولّد لغة تجميع AVR — فقط إن كانت خلفية AVR متوفرة في llvmlite."""
        tm = self._make_avr_target_machine()
        if tm is None:
            raise RuntimeError(
                "لا يمكن توليد التجميع: خلفية AVR غير متوفرة في هذه النسخة من llvmlite. "
                "استخدم llc/clang أو avr-gcc على الكود المحسّن بدلاً من ذلك."
            )
        mod = llvm.parse_assembly(self.optimize(llvm_ir))
        return tm.emit_assembly(mod)

    def emit_object(self, llvm_ir: str) -> bytes:
        """يولّد ملف كائن AVR (.o) بعد التحسين — جاهزاً للربط (linking).
        يتطلب توفّر خلفية AVR في llvmlite."""
        tm = self._make_avr_target_machine()
        if tm is None:
            raise RuntimeError(
                "لا يمكن توليد ملف الكائن: خلفية AVR غير متوفرة في هذه النسخة من llvmlite."
            )
        mod = llvm.parse_assembly(self.optimize(llvm_ir))
        return tm.emit_object(mod)

    def write_object(self, llvm_ir: str, out_path: str) -> None:
        """يكتب ملف الكائن (.o) إلى القرص مباشرةً."""
        with open(out_path, "wb") as fh:
            fh.write(self.emit_object(llvm_ir))


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
