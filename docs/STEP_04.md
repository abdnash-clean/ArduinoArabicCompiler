# الخطوة 4 — التوثيق النهائي ودليل AVR toolchain

## الهدف
كتابة توثيق واضح لكيفية استخدام المرحلة الخلفية وإنتاج `firmware.hex` ورفعه على Arduino Uno.

## المتطلبات

1. Python 3.14+ مع الـ dependencies:
   ```bash
   python -m venv .venv
   .venv\Scripts\pip install -r requirements.txt   # Windows
   # .venv/bin/pip install -r requirements.txt      # Linux/macOS
   ```

2. **llvmlite مع دعم AVR** — تحقق منه:
   ```bash
   .venv/Scripts/python -c "import llvmlite.binding as llvm; print(llvm.Target.from_triple('avr-atmel-none'))"
   ```
   يجب أن يطبع:
   ```text
   <Target avr (Atmel AVR Microcontroller)>
   ```

3. **Arduino AVR toolchain** (اختياري — يمكن تثبيته تلقائياً داخل المشروع):
   - أسهل طريقة على Windows: استخدم المساعد المدمج:
     ```bash
     python build.py setup
     ```
     هذا يثبت `arduino-cli` ونواة `arduino:avr` ويبني `runtime/core.a` داخل المشروع.
   - أو يدوياً:
     ```bash
     arduino-cli core install arduino:avr
     ```
   - على Linux:
     ```bash
     sudo apt install gcc-avr avr-libc binutils-avr avrdude
     ```

## سير العمل الكامل (باستخدام build.py)

يوجد مساعد بناء سريع `build.py`:

```bash
python build.py setup       # تثبيت Arduino toolchain وبناء core.a (مرة واحدة)
python build.py test        # اختبارات الخلفية
python build.py compile     # تشغيل main.py بالكامل
python build.py link        # الربط (يتطلب core.a)
python build.py flash       # الرفع على اللوحة
python build.py clean       # تنظيف الملفات المولّدة
```

### 1. كتابة البرنامج
عدّل `test_arduino.txt` باللغة العربية. مثال بسيط (Blink):

```arabic
اعداد {
    وضع_الطرف(13, مخرج);
}

تكرار {
    اكتب_رقمي(13, عالي);
    انتظر(1000);
    اكتب_رقمي(13, منخفض);
    انتظر(1000);
}
```

### 2. ترجمة البرنامج

```bash
export PYTHONIOENCODING=utf-8
python build.py compile
```

النتائج:
- `output.o` — كائن AVR.
- `output.s` — التجميعة AVR (للمراجعة).
- `firmware.hex` — ملف Intel HEX جاهز للرفع على Arduino.

مثال على ناتج ناجح:
```text
[linker] ✅ تم إنشاء firmware.hex
AVR Memory Usage
Program:    4766 bytes (14.5% Full)
Data:        208 bytes (10.2% Full)
```

### 3. الربط اليدوي (إذا لم يكتمل تلقائياً)

```bash
# أولاً: بناء أو العثور على core.a
# طريقة سريعة: اجمع أي sketch فارغ بـ arduino-cli ثم انسخ core.a من مجلد البناء

# ثانياً: الربط
python -m backend.linker output.o <path/to/core.a>
```

### 4. رفع البرنامج على اللوحة

```bash
# Linux
avrdude -c arduino -p atmega328p -P /dev/ttyACM0 -b 115200 -U flash:w:firmware.hex:i

# Windows
avrdude -c arduino -p atmega328p -P COM3 -b 115200 -U flash:w:firmware.hex:i
```

> لبعض نسخ Arduino Nano القديمة استخدم `-b 57600`.

### 5. مراقبة Serial

إذا كان البرنامج يستخدم `سيريال_ابدا(9600)` و `سيريال_اطبع(...)`:

```bash
arduino-cli monitor -p /dev/ttyACM0 --config baudrate=9600
```

## تشغيل الاختبارات

```bash
export PYTHONIOENCODING=utf-8
.venv/Scripts/python -m unittest backend.tests.test_backend -v
```

## أخطاء شائعة

| الخطأ | السبب | الحل |
|-------|-------|------|
| `No module named 'llvmlite'` | لم يتم تفعيل الـ venv | ` .venv\Scripts\activate` أو استخدم `.venv/Scripts/python` |
| `Unable to find target for this triple` | llvmlite بدون AVR | أعد تثبيت llvmlite أو استخدم external toolchain |
| `avr-g++ not found` | Arduino toolchain غير مثبت | ثبّت `arduino-cli core install arduino:avr` |
| `undefined reference to c_pinMode` | `arduino_glue.cpp` لم يُربط | تأكد من وجود `arduino_glue.o` في الأمر |
| `undefined reference to setup`/`loop` | IR لم يُصدّرهما | تأكد من وجود `اعداد` و `تكرار` في المصدر |
| برنامج يتجمد بدون رسالة | `panic_div_zero` تم تنشيطه | افحص القسمة على صفر |

## اختبار على جهاز Arduino Uno حقيقي

### ما تحتاجه
- لوحة **Arduino Uno** (أو متوافقة ATmega328P).
- كابل **USB A-to-B**.
- نفس الكمبيوتر الذي يحتوي على `firmware.hex`.

### 1. توصيل اللوحة
1. وصّل Arduino Uno بالكمبيوتر عبر كابل USB.
2. انتظر بضع ثوانٍ حتى يتعرف Windows على المنفذ.

### 2. معرفة منفذ COM

```bash
python build.py ports
```

أو من سطر أوامر عادي:
```bash
tools/arduino-cli/bin/arduino-cli.exe board list
```

سترى شيئاً مثل:
```text
Port Protocol Type              Board Name  FQBN            Core
COM3 serial   Serial Port (USB) Arduino Uno arduino:avr:uno arduino:avr
```

إذا لم تظهر اللوحة، تأكد من تثبيت تعريف CH340/CP210x إذا كانت نسخة صينية.

### 3. رفع البرنامج (Flash)

استبدل `COM3` بالمنفذ الذي ظهر لديك:

```bash
python build.py flash COM3
```

أو يدوياً بـ avrdude:
```bash
tools/arduino-cli/data/packages/arduino/tools/avrdude/8.0.0-arduino1/bin/avrdude.exe \
  -c arduino -p atmega328p -P COM3 -b 115200 \
  -U flash:w:firmware.hex:i
```

> لبعض نسخ Arduino Nano القديمة استخدم `-b 57600`.

### 4. اختبار Blink

استخدم الملف `samples/blink.txt`:

```bash
cp samples/blink.txt test_arduino.txt
python build.py compile
python build.py flash COM3
```

يجب أن يبدأ الـ LED الموجود على اللوحة (بجانب pin 13) بالوميض كل ثانية.

### 5. اختبار Serial

استخدم الملف `samples/serial_hello.txt`:

```bash
cp samples/serial_hello.txt test_arduino.txt
python build.py compile
python build.py flash COM3
```

ثم افتح Serial Monitor:

```bash
tools/arduino-cli/bin/arduino-cli.exe monitor -p COM3 --config baudrate=9600
```

سترى:
```text
مرحباً من Arduino!
0
مرحباً من Arduino!
1
...
```

### 6. اختبار القسمة على صفر (panic)

أضف في أي برنامج سطراً مثل:
```arabic
متغير نتيجة : صحيح = 10 / 0 ؛
```

بعد رفع البرنامج:
- إذا كان `سيريال_ابدا()` مفعّلاً، تظهر رسالة:
  ```text
  [Runtime Error] Division by zero! Program halted safely.
  ```
- بعدها يتوقف البرنامج ويبدأ LED على pin 13 بالوميض كرمز خطأ.

### استكشاف أخطاء شائعة

| المشكلة | الحل |
|---------|------|
| اللوحة لا تظهر في `build.py ports` | جرب كابل USB آخر أو منفذ USB آخر؛ تأكد من تعريف CH340/CP210x. |
| `avrdude: stk500_getsync()` | غالباً المنفذ خاطئ أو الباود خاطئ؛ جرب `-b 57600`. |
| البرنامج لا يعمل بعد الرفع | تأكد أن `test_arduino.txt` يحتوي `اعداد` و `تكرار`. |
| Serial لا يطبع | تأكد من كتابة `استيراد "سيريال" ؛` في أول الملف وفتح المراقب على نفس baudrate. |

## الخلاصة

المرحلة الخلفية الآن كاملة:
- مُقسّمة إلى وحدات واضحة (`avr_target`, `codegen`, `optimizer`, `linker`).
- تحتوي على طبقة ربط كاملة.
- تدعم Serial بأنواع متعددة.
- تحتوي على اختبارات آلية.
- تنتج `firmware.hex` جاهزاً للرفع على Arduino Uno.
- تتضمن toolchain محمول داخل المشروع.

الخطوة الأخيرة هي ربط اللوحة وتجربة `samples/blink.txt`.
