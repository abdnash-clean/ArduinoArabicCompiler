# semantic/types_system.py

# الفئة الأساسية لأي نوع بيانات
class Type:
    def __eq__(self, other):
        # تطابق اسمي: نوعان متطابقان إذا كانا من نفس الفئة
        return isinstance(other, self.__class__)

class IntType(Type):
    def __str__(self): return "صحيح"

class FloatType(Type):
    def __str__(self): return "عشري"

class StringType(Type):
    def __str__(self): return "نص"

class BoolType(Type):
    def __str__(self): return "منطقي"

class VoidType(Type):
    def __str__(self): return "فارغ"

class ErrorType(Type):
    """النوع المسموم: يُستخدم عند وجود خطأ لمنع تكرار رسائل الخطأ اللاحقة لنفس السبب"""
    def __str__(self): return "داللي_خطأ"

# ثوابت عامة لتوفير الذاكرة وسهولة المقارنة
INT_TYPE = IntType()
VOID_TYPE = VoidType()
FLOAT_TYPE = FloatType()
STRING_TYPE = StringType()
BOOL_TYPE = BoolType()
ERROR_TYPE = ErrorType()