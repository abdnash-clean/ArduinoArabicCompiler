# semantic/symbols.py
from typing import Any

# الفئة الأساسية لأي كيان يتم تعريفه في الكود
class Symbol:
    def __init__(self, name: str, sym_type: Any = None):
        self.name = name
        self.type = sym_type  # نوع البيانات (صحيح، عشري، نص، الخ)

    def __repr__(self):
        return f"<{self.__class__.__name__}: name='{self.name}', type='{self.type}'>"

# فئة مخصصة للمتغيرات العادية
class VariableSymbol(Symbol):
    def __init__(self, name: str, sym_type: Any = None):
        super().__init__(name, sym_type)

# فئة مخصصة للدوال (سنستخدمها لاحقاً لتعريف إعداد وتكرار وغيرها)
class FunctionSymbol(Symbol):
    def __init__(self, name: str, return_type: Any = None, arity: int = 0):
        super().__init__(name, return_type)
        self.arity = arity  # عدد المعاملات التي تقبلها الدالة