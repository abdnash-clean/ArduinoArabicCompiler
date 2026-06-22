# semantic/builtins_registry.py
from semantic.symbols import ConstantSymbol, FunctionSymbol
from semantic.types_system import INT_TYPE, FLOAT_TYPE, STRING_TYPE, VOID_TYPE

# 1. Core Constants & Functions (Always loaded)
CORE_CONSTANTS = {
    "عالي": ConstantSymbol("عالي", INT_TYPE),    # HIGH
    "منخفض": ConstantSymbol("منخفض", INT_TYPE),  # LOW
    "مدخل": ConstantSymbol("مدخل", INT_TYPE),    # INPUT
    "مخرج": ConstantSymbol("مخرج", INT_TYPE),    # OUTPUT
}

CORE_FUNCTIONS = {
    "وضع_الطرف": FunctionSymbol("وضع_الطرف", VOID_TYPE, 2),       # pinMode
    "اكتب_رقمي": FunctionSymbol("اكتب_رقمي", VOID_TYPE, 2),       # digitalWrite
    "اقرا_رقمي": FunctionSymbol("اقرا_رقمي", INT_TYPE, 1),        # digitalRead
    "اكتب_تناظري": FunctionSymbol("اكتب_تناظري", VOID_TYPE, 2),   # analogWrite
    "اقرا_تناظري": FunctionSymbol("اقرا_تناظري", INT_TYPE, 1),    # analogRead
    "انتظر": FunctionSymbol("انتظر", VOID_TYPE, 1),              # delay
    "الزمن_الحالي": FunctionSymbol("الزمن_الحالي", INT_TYPE, 0),  # millis
}

# 2. Libraries (Loaded ONLY when imported)
LIBRARIES = {
    "سيريال": {
        "سيريال_ابدا": FunctionSymbol("سيريال_ابدا", VOID_TYPE, 1),  # Serial.begin
        "سيريال_اطبع": FunctionSymbol("سيريال_اطبع", VOID_TYPE, 1),  # Serial.print
    },
}

# 3. Hardware registers (ATmega328P / Arduino Uno)
#    Arabic name -> data-memory address. Treated as writable 8-bit cells.
#    اتجاه = DDR (direction), منفذ = PORT (output), دخل = PIN (input)
REGISTERS = {
    "اتجاه_ب": 0x24,  # DDRB
    "منفذ_ب": 0x25,   # PORTB
    "دخل_ب": 0x23,    # PINB

    "اتجاه_ج": 0x27,  # DDRC
    "منفذ_ج": 0x28,   # PORTC
    "دخل_ج": 0x26,    # PINC

    "اتجاه_د": 0x2A,  # DDRD
    "منفذ_د": 0x2B,   # PORTD
    "دخل_د": 0x29,    # PIND
}
