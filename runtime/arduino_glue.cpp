// runtime/arduino_glue.cpp
// =============================================================================
//  طبقة الربط (Glue Layer) بين شيفرة LLVM المولّدة والنواة الحقيقية لـ Arduino
// -----------------------------------------------------------------------------
//  المترجم يصرّح برموز خارجية مثل c_pinMode، c_digitalWrite، panic_div_zero
//  لكنها غير معرّفة في شيفرة LLVM. هذا الملف يوفّر التنفيذات الحقيقية باستخدام
//  نواة Arduino (Arduino.h). كما يوفّر نقطة الدخول main() التي تستدعي
//  init() ثم setup() ثم loop() بشكل لا نهائي.
//
//  مهم جداً: لغة المترجم تعتبر "صحيح" = i32، بينما AVR C يعتبر int = 16-بت.
//  لذا كل المعلمات هنا من نوع int32_t لتتوافق مع ABI التي يتوقعها LLVM.
// =============================================================================

#include <Arduino.h>
#include <stdint.h>
#include <avr/interrupt.h>   // cli()

// الدالتان setup() و loop() يولّدهما المترجم بروابط C (not C++ mangled).
extern "C" {
    void setup();
    void loop();

    // --- نواة Arduino الأساسية -------------------------------------------
    void    c_pinMode(int32_t p, int32_t m)      { pinMode((uint8_t)p, (uint8_t)m); }
    void    c_digitalWrite(int32_t p, int32_t v) { digitalWrite((uint8_t)p, (uint8_t)v); }
    int32_t c_digitalRead(int32_t p)             { return (int32_t)digitalRead((uint8_t)p); }
    void    c_analogWrite(int32_t p, int32_t v)  { analogWrite((uint8_t)p, (int)v); }
    int32_t c_analogRead(int32_t p)              { return (int32_t)analogRead((uint8_t)p); }
    void    c_delay(int32_t ms)                  { delay((uint32_t)ms); }
    int32_t c_millis()                           { return (int32_t)millis(); }

    // --- مكتبة السيريال ---------------------------------------------------
    void    c_serialBegin(int32_t baud)          { Serial.begin((long)baud); }
    void    c_serialPrintInt(int32_t v)          { Serial.println(v); }
    void    c_serialPrintFloat(double v)         { Serial.println(v); }
    void    c_serialPrintString(const char* s)   { Serial.println(s); }

    // --- معالج خطأ القسمة على صفر -----------------------------------------
    // ينبغي ألا يعود أبداً. نعلن عن الخطأ عبر Serial ثم نوقف المعالج بأمان.
    void panic_div_zero() {
        Serial.println(F("[Runtime Error] Division by zero! Program halted safely."));
        Serial.flush();

        cli();                      // إيقاف جميع المقاطعات
        pinMode(13, OUTPUT);        // LED الموجود على اللوحة كمؤشر خطأ

        for (;;) {
            digitalWrite(13, HIGH);
            for (volatile long i = 0; i < 150000; i++);
            digitalWrite(13, LOW);
            for (volatile long i = 0; i < 150000; i++);
        }
    }
}

// =============================================================================
//  نقطة الدخول الرئيسية
// -----------------------------------------------------------------------------
//  نواة Arduino تحتوي على main.cpp خاص بها تتوقع setup() و loop() بروابط C++.
//  لكن مترجمنا يصدّرهما بروابط C، لذا نقدّم main() خاصة بنا ولا نربط main.cpp
//  الخاصة بالنواة. يجب استدعاء init() أولاً لأنها تهيّئ المؤقتات التي تعتمد
//  عليها delay() و millis() و PWM.
// =============================================================================
int main(void) {
    init();
    setup();
    for (;;) {
        loop();
        if (serialEventRun) serialEventRun();
    }
}
