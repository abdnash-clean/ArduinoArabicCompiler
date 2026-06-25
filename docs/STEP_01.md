# الخطوة 1 — طبقة الربط (Glue Layer) وإنتاج firmware.hex

## الهدف
جعل ملف `output.o` القادم من المترجم **قابلاً للربط** بحيث ينتج `firmware.hex` جاهز للرفع على Arduino Uno.

## ما تم إنجازه

### 1. إعادة تنظيم المرحلة الخلفية
| الملف الجديد | المسؤولية |
|--------------|-----------|
| `backend/avr_target.py` | تسجيل هدف AVR وإنشاء `TargetMachine`. |
| `backend/codegen.py` | توليد التجميع وملف الكائن من LLVM IR محسّن. |
| `backend/optimizer.py` | التحسين فقط (بدون target setup أو codegen). |
| `backend/linker.py` | تجميع Glue + ربط + إنتاج HEX. |
| `runtime/arduino_glue.cpp` | تنفيذات دوال Arduino و `panic_div_zero` و `main()`. |

### 2. طبقة الربط `runtime/arduino_glue.cpp`
توفر تنفيذات لكل الرموز الخارجية التي يصرّح بها LLVM IR:
- `c_pinMode`, `c_digitalWrite`, `c_digitalRead`
- `c_analogWrite`, `c_analogRead`
- `c_delay`, `c_millis`
- `c_serialBegin`, `c_serialPrintInt`, `c_serialPrintFloat`, `c_serialPrintString`
- `panic_div_zero`
- `main()` تستدعي `init()` → `setup()` → `loop()`

> **ملاحظة ABI:** لغة المترجم تعتبر `صحيح` = `i32`، بينما AVR C يعتبر `int` = 16-بت. لذلك كل المعلمات في Glue تستخدم `int32_t`.

### 3. ربط `سيريال_اطبع` بالـ overloads المكتوبة
تم تعديل `backend/ir_generator.py` ليختار بين:
- `c_serialPrintInt` للأعداد الصحيحة
- `c_serialPrintFloat` للأعداد العشرية
- `c_serialPrintString` للنصوص

بدلاً من الـ variadic `c_serialPrint` الذي كان صعب التنفيذ على AVR.

### 4. تكامل `main.py`
بعد توليد `output.o` والتجميع، يحاول `main.py` الآن تلقائياً:
1. تجميع `runtime/arduino_glue.cpp` → `arduino_glue.o`
2. ربط `output.o + arduino_glue.o + core.a` → `firmware.elf`
3. تحويل `firmware.elf` → `firmware.hex`

إذا لم يكن AVR toolchain مثبتاً، يطبع رسالة توضيحية ولا يتوقف البرنامج بشكل قاتل.

## التحقق

تشغيل:
```bash
export PYTHONIOENCODING=utf-8
.venv/Scripts/python main.py
```

النتيجة المتوقعة:
- يُولَّد `output.o` (AVR ELF relocatable).
- يُطبع التجميعة AVR.
- يصل إلى خطوة الربط؛ إذا لم يكن `avr-g++` متوفراً تظهر رسالة توضيحية.

## المتطلبات المتبقية

لإكمال الربط فعلياً يجب تثبيت Arduino AVR toolchain:
```bash
# Windows / Linux / macOS
arduino-cli core install arduino:avr

# أو على Linux
sudo apt install gcc-avr avr-libc binutils-avr
```

ثم تشغيل الربط يدوياً:
```bash
python -m backend.linker output.o <path/to/core.a>
```

## الخطوة التالية
[STEP_02](STEP_02.md) — بناء اختبارات خلفية آلية للتحقق من IR والربط بدون الحاجة إلى لوحة حقيقية.
