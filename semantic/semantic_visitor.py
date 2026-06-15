# semantic/semantic_visitor.py
from ast_dir.visitor_interface import ASTVisitor
from ast_dir.nodes import *
from semantic.environment import Environment, SemanticError
from semantic.symbols import VariableSymbol, FunctionSymbol

class SemanticVisitor(ASTVisitor):
    def __init__(self):
        # تهيئة البيئة العامة (Global Scope)
        self.current_env = Environment()
        # قائمة لتجميع الأخطاء الدلالية لعرضها للمستخدم دفعة واحدة
        self.errors = []

    def log_error(self, line: int, column: int, message: str):
        """دالة مساعدة لتسجيل الأخطاء بتنسيق هندسي منظم"""
        self.errors.append(f"خطأ دلالي (سطر {line}): {message}")

    # نقطة انطلاق الزائر لعبور الشجرة
    def visit_ProgramNode(self, node: ProgramNode):
        for decl in node.declarations:
            decl.accept(self)

    # إدارة النطاقات داخل الكتل البرمجية {}
    def visit_BlockNode(self, node: BlockNode):
        # 1. حفظ مؤشر البيئة الحالية (الأب)
        previous_env = self.current_env
        # 2. الغوص للأسفل: إنشاء بيئة فرعية محاطة بالبيئة السابقة
        self.current_env = Environment(enclosing=previous_env)
        # 3. زيارة الجمل داخل النطاق الفرعي الجديد
        for stmt in node.statements:
            stmt.accept(self)
        # 4. الصعود للأعلى: استعادة البيئة السابقة (تدمير النطاق المحلي)
        self.current_env = previous_env

    # التحقق من تعريف المتغيرات وتخزينها
    def visit_VarDeclNode(self, node: VarDeclNode):
        # أولاً: زيارة القيمة الابتدائية للتأكد من خلوها من الأخطاء
        if node.value:
            node.value.accept(self)
        
        # ثانياً: إنشاء رمز (Symbol) للمتغير الجديد
        symbol = VariableSymbol(name=node.name, sym_type=node.var_type)
        
        # ثالثاً: تسجيل المتغير في البيئة الحالية
        try:
            self.current_env.define(node.name, symbol)
        except SemanticError as e:
            self.log_error(node.line, node.column, str(e))

    # التحقق من وجود المتغير عند استدعائه (المرجع)
    def visit_IdNode(self, node: IdNode):
        try:
            self.current_env.resolve(node.name)
        except SemanticError as e:
            self.log_error(node.line, node.column, str(e))

    # التحقق من المتغير عند الإسناد إليه (س = قيمة)
    def visit_AssignNode(self, node: AssignNode):
        # 1. تقييم الجانب الأيمن أولاً
        if node.value:
            node.value.accept(self)
        # 2. التأكد من أن المتغير المراد تحديثه موجود أصلاً بالذاكرة
        try:
            self.current_env.resolve(node.name)
        except SemanticError as e:
            self.log_error(node.line, node.column, str(e))

    # التحقق من صحة تعريف الدوال وإدارة نطاقاتها ومعاملاتها
    def visit_FuncDeclNode(self, node: FuncDeclNode):
        # 1. تسجيل اسم الدالة في النطاق الحالي
        func_symbol = FunctionSymbol(name=node.name, return_type=node.return_type, arity=len(node.params))
        try:
            self.current_env.define(node.name, func_symbol)
        except SemanticError as e:
            self.log_error(node.line, node.column, str(e))

        # 2. الغوص لأسفل: فتح نطاق خاص للدالة للتعامل مع المتغيرات المحلية والمعاملات
        previous_env = self.current_env
        self.current_env = Environment(enclosing=previous_env)

        # 3. تعريف معاملات الدالة (Parameters) داخل نطاقها الجديد
        for param_name, param_type in node.params:
            p_symbol = VariableSymbol(name=param_name, sym_type=param_type)
            try:
                self.current_env.define(param_name, p_symbol)
            except SemanticError as e:
                self.log_error(node.line, node.column, str(e))

        # 4. زيارة الجمل البرمجية داخل جسم الدالة (دون استدعاء BlockNode لكي لا نفتح نطاقاً إضافياً مكرراً)
        if node.body and isinstance(node.body, BlockNode):
            for stmt in node.body.statements:
                stmt.accept(self)

        # 5. الصعود للأعلى: إغلاق نطاق الدالة
        self.current_env = previous_env

    # تمرير الزيارة للاستدعاءات والعقد الأخرى لتكملة مسار التحليل
    def visit_FuncCallNode(self, node: FuncCallNode):
        for arg in node.args:
            arg.accept(self)

    def visit_IfNode(self, node: IfNode):
        if node.condition:
            node.condition.accept(self)
        if node.then_block:
            node.then_block.accept(self)
        if node.else_block:
            node.else_block.accept(self)

    def visit_WhileNode(self, node: WhileNode):
        if node.condition:
            node.condition.accept(self)
        if node.body:
            node.body.accept(self)

    def visit_BinOpNode(self, node: BinOpNode):
        if node.left:
            node.left.accept(self)
        if node.right:
            node.right.accept(self)

    def visit_UnaryOpNode(self, node: UnaryOpNode):
        if node.expr:
            node.expr.accept(self)

    def visit_NumberNode(self, node: NumberNode):
        pass

    def visit_StringNode(self, node: StringNode):
        pass

    def visit_CharNode(self, node: CharNode):
        pass

    def visit_BoolNode(self, node: BoolNode):
        pass

    def visit_ReturnNode(self, node: ReturnNode):
        if node.value:
            node.value.accept(self)