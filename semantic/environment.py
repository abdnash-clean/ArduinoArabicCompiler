# semantic/environment.py
from semantic.symbols import Symbol

class SemanticError(Exception):
    """استثناء مخصص لأخطاء التحليل الدلالي"""
    pass

class Environment:
    def __init__(self, enclosing: 'Environment' = None):
        self._values = {}          # القاموس الداخلي لتخزين الرموز في هذا النطاق فقط
        self.enclosing = enclosing  # مؤشر يشير إلى النطاق الأب (الخارجي)

    def define(self, name: str, symbol: Symbol):
        """تعريف متغير جديد في النطاق الحالي ويمنع تكرار نفس الاسم في نفس النطاق"""
        if name in self._values:
            raise SemanticError(f"خطأ دلالي: المتغير '{name}' معرّف مسبقاً في هذا النطاق.")
        self._values[name] = symbol

    def resolve(self, name: str) -> Symbol:
        """البحث عن متغير: يبدأ من النطاق الحالي ويصعد للنطاقات الآباء إذا لزم الأمر"""
        # 1. هل المتغير موجود في النطاق الحالي؟
        if name in self._values:
            return self._values[name]
            
        # 2. إذا لم يجده، هل يوجد نطاق أب لنسأله؟
        if self.enclosing is not None:
            return self.enclosing.resolve(name)
            
        # 3. إذا وصلنا للقمة ولم نجده، فهو غير معرف
        raise SemanticError(f"خطأ دلالي: استخدام لمتغير غير معرّف '{name}'.")

    def print_stack(self, level=0):
        """دالة مساعدة لطباعة محتويات الذاكرة الحالية للتصحيح"""
        print(f"{'  ' * level}└─ Scope Level {level}: {list(self._values.keys())}")
        if self.enclosing:
            self.enclosing.print_stack(level + 1)