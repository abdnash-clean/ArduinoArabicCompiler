# semantic/builtins_registry.py
from semantic.symbols import ConstantSymbol, FunctionSymbol
from semantic.types_system import INT_TYPE, FLOAT_TYPE, STRING_TYPE, VOID_TYPE

# 1. Core Constants & Functions (Always loaded)
CORE_CONSTANTS = {
    "عالي": ConstantSymbol("عالي", INT_TYPE),        # HIGH
    "منخفض": ConstantSymbol("منخفض", INT_TYPE),    # LOW
    "مدخل": ConstantSymbol("مدخل", INT_TYPE),        # INPUT
    "مخرج": ConstantSymbol("مخرج", INT_TYPE),        # OUTPUT
}

CORE_FUNCTIONS = {
    "وضع_الطرف": FunctionSymbol("وضع_الطرف", VOID_TYPE, 2),       # pinMode
    "اكتب_رقمي": FunctionSymbol("اكتب_رقمي", VOID_TYPE, 2),       # digitalWrite
    "اقرأ_رقمي": FunctionSymbol("اقرأ_رقمي", INT_TYPE, 1),       # digitalRead
    "اكتب_تناظري": FunctionSymbol("اكتب_تناظري", VOID_TYPE, 2),   # analogWrite
    "اقرأ_تناظري": FunctionSymbol("اقرأ_تناظري", INT_TYPE, 1),   # analogRead
    "انتظر": FunctionSymbol("انتظر", VOID_TYPE, 1),               # delay
    "الزمن_الحالي": FunctionSymbol("الزمن_الحالي", INT_TYPE, 0),  # millis
}

# 2. Libraries (Loaded ONLY when imported)
# Example: Serial (سيريال) or Servo (محرك)
LIBRARIES = {
    "سيريال": {
        "سيريال_ابدأ": FunctionSymbol("سيريال_ابدأ", VOID_TYPE, 1),    # Serial.begin
        "سيريال_اطبع": FunctionSymbol("سيريال_اطبع", VOID_TYPE, 1),    # Serial.print
    },
}