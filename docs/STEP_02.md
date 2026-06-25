# الخطوة 2 — اختبارات دخان للمرحلة الخلفية

## الهدف
بناء حزمة اختبارات آلية تتحقق من أن المرحلة الخلفية تعمل بشكل صحيح **دون الحاجة إلى لوحة Arduino حقيقية**.

## ما تم إنجازه

### 1. إنشاء `backend/tests/test_backend.py`
يستخدم `unittest` المدمج في Python (لا حاجة لـ pytest) ويغطي:

| مجموعة الاختبارات | ما تتحقق منه |
|-------------------|--------------|
| `TestAVRTTarget` | ثوابت AVR وإنشاء `TargetMachine` للـ AVR والـ host. |
| `TestOptimizer` | تحسين IR بسيط وضبط `triple`/`datalayout` الخاصين بـ AVR. |
| `TestCodegen` | توليد تجميعة AVR وملف كائن AVR صالح (يبدأ بـ `\x7fELF`). |
| `TestLinker` | تجميع طبقة الربط وربطها — تُتخطى تلقائياً إذا لم يكن `avr-g++` متوفراً. |
| `TestSerialOverloadDispatch` | التأكد من أن `ir_generator.py` يحتوي على overloads `سيريال_اطبع_صحيح/عشري/نص`. |

### 2. ميزات التصميم
- **لا تعتمد على ملفات خارجية:** كل اختبار يبني IR بسيط داخلياً.
- **تخطٍّ ذكي:** اختبارات الربط تُتخطى على الأجهزة التي لا تحتوي على `avr-g++` بدلاً من الفشل.
- **سريعة:** 11 اختباراً تكتمل في أجزاء من الثانية.

## التشغيل

```bash
export PYTHONIOENCODING=utf-8
.venv/Scripts/python -m unittest backend.tests.test_backend -v
```

## النتيجة المتوقعة

```text
Ran 11 tests in 0.039s
OK (skipped=2)
```

الاختبارات المُتخطاة (`skipped=2`) تتعلق بـ AVR toolchain؛ ستعمل عند تثبيت `avr-g++`.

## الخطوة التالية
[STEP_03](STEP_03.md) — إنشاء `docs/PLAN.md` النهائي وتوثيق كيفية تثبيت AVR toolchain وإنتاج `firmware.hex`.
