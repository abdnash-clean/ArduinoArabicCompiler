# الخطوة 3 — توحيد أسماء الدوال المدمجة

## الهدف
إزالة التناقض بين `semantic/builtins_registry.py` و `backend/ir_generator.py` بحيث تنجح عمليات البحث عن الدوال المدمجة بعد تسوية النص العربي.

## المشكلة
`normlize.py` يحوّل كل من `أ`, `إ`, `آ` إلى `ا` قبل التحليل المعجمي. هذا يعني أنّ:

| ما يكتبه المستخدم | بعد التسوية |
|-------------------|-------------|
| `اقرأ_رقمي` | `اقرا_رقمي` |
| `اقرا_رقمي` | `اقرا_رقمي` |
| `ابدأ` | `ابدا` |

لكن السجل الدلالي كان يستخدم `اقرا_رقمي` بينما `ir_generator.py` كان يستخدم `اقرأ_رقمي` (بهمزة). النتيجة:
- التحليل الدلالي ينجح.
- توليد LLVM IR يفشل صامتاً لأنّ البحث عن `اقرا_رقمي` في `self.builtins` لا يعثر على شيء.

## ما تم إنجازه

### 1. تصحيح المفاتيح في `backend/ir_generator.py`
| المفتاح القديم | المفتاح الجديد |
|----------------|----------------|
| `اقرأ_رقمي` | `اقرا_رقمي` |
| `اقرأ_تناظري` | `اقرا_تناظري` |
| `سيريال_ابدأ` | `سيريال_ابدا` |

### 2. إضافة اختبارات توافق
في `backend/tests/test_backend.py` أضفنا:
- `TestBuiltinNameConsistency.test_all_semantic_core_functions_exist_in_ir`
- `TestBuiltinNameConsistency.test_all_semantic_serial_functions_exist_in_ir`

هذه الاختبارات تتأكد أن كل دالة مدمجة في السجل الدلالي لها تعريف مقابل في `ir_generator.py`.

## التحقق

```bash
export PYTHONIOENCODING=utf-8
.venv/Scripts/python -m unittest backend.tests.test_backend -v
```

النتيجة:
```text
Ran 13 tests in 0.037s
OK (skipped=2)
```

## الخطوة التالية
[STEP_04](STEP_04.md) — التوثيق النهائي: خطة كاملة ودليل تثبيت AVR toolchain وإنتاج `firmware.hex`.
