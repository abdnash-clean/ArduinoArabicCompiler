# خطة المرحلة الخلفية — Arduino Arabic Compiler (AVR / ATmega328P)

> خطة العمل الكاملة للمرحلة الخلفية، مع ما تم إنجازه وما يحتاج إلى اختبار على جهاز حقيقي.

## ملخص الوضع الحالي

المرحلة الخلفية تحول AST إلى LLVM IR، ثم تحسّنه، ثم تولّد كائن AVR، وأخيراً تربطه مع طبقة الربط (glue) ونواة Arduino لإنتاج `firmware.hex`.

## ملفات المرحلة الخلفية

```text
backend/
  avr_target.py        # إعداد TargetMachine لـ AVR
  codegen.py           # IR → assembly / object
  optimizer.py         # تحسين LLVM IR + إصلاح AVR ult
  linker.py            # glue + link + objcopy → .hex
  tests/
    test_backend.py    # اختبارات دخان للخلفية
runtime/
  arduino_glue.cpp     # C wrappers + panic + main()
build.py               # مساعد بناء سريع
.github/workflows/ci.yml  # CI للاختبارات
```

## خطوات التنفيذ

| الخطوة | الملف | الحالة |
|--------|-------|--------|
| 1 — إعادة تنظيم `optimizer.py` وإنشاء `avr_target.py` + `codegen.py` | `backend/avr_target.py`, `backend/codegen.py`, `backend/optimizer.py` | ✅ منجز |
| 1 — طبقة الربط `arduino_glue.cpp` + `linker.py` | `runtime/arduino_glue.cpp`, `backend/linker.py` | ✅ منجز |
| 1 — Serial.print overloads | `backend/ir_generator.py` | ✅ منجز |
| 2 — اختبارات خلفية آلية | `backend/tests/test_backend.py` | ✅ منجز |
| 3 — توحيد أسماء الدوال المدمجة | `backend/ir_generator.py` | ✅ منجز |
| 4 — توثيق الاستخدام ودليل AVR toolchain | `docs/STEP_04.md` | ✅ منجز |
| 5 — مساعد بناء + CI | `build.py`, `.github/workflows/ci.yml` | ✅ منجز |
| 6 — تثبيت Arduino toolchain تلقائياً | `tools/setup_avr_toolchain.py`, `tools/build_core.py` | ✅ منجز |
| 7 — اختبار على جهاز حقيقي (Arduino Uno) | — | ⏳ يحتاج لوحة Arduino متصلة |

## معايير النجاح

- [x] `python main.py` يولّد `output.o` صالحاً لـ AVR.
- [x] `python -m unittest backend.tests.test_backend` يمر بنسبة 100% (باستثناء اختبارات الربط عند غياب `avr-g++`).
- [x] كل أسماء الدوال المدمجة متوافقة بين السجل الدلالي والمولّد بعد التسوية.
- [x] ربط `output.o + arduino_glue.o + core.a` ينجح بدون رموز غير محلولة.
- [ ] `firmware.hex` يعمل على Arduino Uno (blink / Serial / divide-by-zero panic).

## ملاحظات تقنية

- `صحيح` = LLVM `i32`، بينما AVR C `int` = 16-bit. كل wrappers في `arduino_glue.cpp` تستخدم `int32_t`.
- `setup()` و `loop()` يصدّرهما المترجم بروابط C؛ `arduino_glue.cpp` يقدّم `main()` خاصة تستدعيهما.
- `panic_div_zero()` لا تعود أبداً: تعلن الخطأ عبر Serial ثم توقف المقاطعات وتتجمد.
- Serial.print لم يعد variadic؛ تم استبداله بـ `c_serialPrintInt/Float/String` لتجنب ABI المعقد على AVR.
