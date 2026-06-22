# semantic/semantic_analyzer.py
from ast_dir.visitor_interface import ASTVisitor
from ast_dir.nodes import *
from semantic.environment import Environment, SemanticError
from semantic.symbols import VariableSymbol, FunctionSymbol
from semantic.types_system import *
from semantic.builtins_registry import CORE_CONSTANTS, CORE_FUNCTIONS, LIBRARIES, REGISTERS


class SemanticAnalyzerVisitor(ASTVisitor):
    def __init__(self):
        # تهيئة البيئة العامة (Global Scope)
        self.current_env = Environment()
        # قائمة لتجميع أخطاء الأنواع والنطاقات
        self.errors = []
        self.loop_depth = 0
        self.current_function_return_type = None
        # Load Core Constants automatically
        for name, symbol in CORE_CONSTANTS.items():
            self.current_env.define(name, symbol)

        # Load Core Functions automatically
        for name, symbol in CORE_FUNCTIONS.items():
            self.current_env.define(name, symbol)

        # Load hardware registers as writable integer variables
        for reg_name in REGISTERS:
            self.current_env.define(reg_name, VariableSymbol(reg_name, INT_TYPE))

    def log_error(self, line: int, column: int, message: str):
        self.errors.append(f"خطأ دلالي (سطر {line}): {message}")

    # 1. زيارة البرنامج (المدخل الرئيسي)
    def visit_ProgramNode(self, node: ProgramNode):
        for decl in node.declarations:
            decl.accept(self)

    # 2. زيارة الكتل البرمجية {} وإدارة النطاق
    def visit_BlockNode(self, node: BlockNode):
        previous_env = self.current_env
        self.current_env = Environment(enclosing=previous_env)
        for stmt in node.statements:
            stmt.accept(self)
        self.current_env = previous_env

    # 3. زيارة إعلان المتغير والتحقق من التوافق
    def visit_VarDeclNode(self, node: VarDeclNode):
        # تقييم نوع القيمة الابتدائية أولاً
        value_type = node.value.accept(self) if node.value else ERROR_TYPE

        # تحويل نوع البيانات النصي إلى كائن النوع المقابل
        type_mapping = {
            'صحيح': INT_TYPE,
            'رقم': INT_TYPE,
            'عشري': FLOAT_TYPE,
            'كسري': FLOAT_TYPE,
            'نص': STRING_TYPE,
            'منطقي': BOOL_TYPE,
            'فارغ': VOID_TYPE
        }
        declared_type = type_mapping.get(node.var_type, STRING_TYPE)

        # التحقق من توافق الأنواع
        if value_type != ERROR_TYPE:
            if value_type == INT_TYPE and declared_type == FLOAT_TYPE:
                pass  # مسموح التحويل من صحيح إلى عشري
            elif value_type != declared_type:
                self.log_error(node.line, node.column, f"لا يمكن إسناد قيمة من نوع '{value_type}' إلى متغير من نوع '{declared_type}'.")
        # حفظ المتغير في البيئة
        try:
            sym = VariableSymbol(node.name, declared_type)
            self.current_env.define(node.name, sym)
        except SemanticError as e:
            self.log_error(node.line, node.column, str(e))

    # 4. زيارة الأرقام وإرجاع النوع صحيح
    def visit_NumberNode(self, node: NumberNode):
        if node.value.is_integer():
            node.resolved_type = INT_TYPE
            return INT_TYPE
        node.resolved_type = FLOAT_TYPE
        return FLOAT_TYPE

    # 5. زيارة استخدام المتغير
    def visit_IdNode(self, node: IdNode):
        try:
            sym = self.current_env.resolve(node.name)
            node.resolved_type = sym.type
            return sym.type
        except SemanticError:
            self.log_error(node.line, node.column, f"استخدام لمتغير غير معرّف '{node.name}'.")
            # تطبيق تسميم الرمز لمنع الأخطاء المتكررة في نفس المعادلة
            return ERROR_TYPE

    # 6. زيارة الإسناد والتحقق من توافق الأنواع
    def visit_AssignNode(self, node: AssignNode):
        value_type = node.value.accept(self) if node.value else ERROR_TYPE
        try:
            sym = self.current_env.resolve(node.name)

            from semantic.symbols import ConstantSymbol
            if isinstance(sym, ConstantSymbol):
                self.log_error(node.line, node.column, f"لا يمكن تغيير قيمة الثابت '{node.name}'.")
                return ERROR_TYPE

            declared_type = sym.type

            if value_type == INT_TYPE and declared_type == FLOAT_TYPE:
                node.resolved_type = FLOAT_TYPE
                return FLOAT_TYPE

            if value_type != ERROR_TYPE and value_type != declared_type:
                self.log_error(node.line, node.column, f"لا يمكن إسناد قيمة من نوع '{value_type}' إلى متغير من نوع '{declared_type}'.")
            else:
                node.resolved_type = declared_type
                return declared_type
        except SemanticError:
            self.log_error(node.line, node.column, f"استخدام لمتغير غير معرّف '{node.name}'.")
            return ERROR_TYPE

    # 7. زيارة العمليات الثنائية وتطبيق التسميم
    def visit_BinOpNode(self, node: BinOpNode):
        left_type = node.left.accept(self) if node.left else ERROR_TYPE
        right_type = node.right.accept(self) if node.right else ERROR_TYPE

        # ميزة التسميم (Poisoning)
        if left_type == ERROR_TYPE or right_type == ERROR_TYPE:
            return ERROR_TYPE

        # التحقق من معاملات الرياضيات
        if node.op in ['+', '-', '*', '/']:
            if left_type == INT_TYPE and right_type == INT_TYPE:
                node.resolved_type = INT_TYPE
                return INT_TYPE
            elif left_type == FLOAT_TYPE and right_type == FLOAT_TYPE:
                node.resolved_type = FLOAT_TYPE
                return FLOAT_TYPE
            elif left_type == INT_TYPE and right_type == FLOAT_TYPE:
                node.left.resolved_type = FLOAT_TYPE
                node.resolved_type = FLOAT_TYPE
                return FLOAT_TYPE
            elif left_type == FLOAT_TYPE and right_type == INT_TYPE:
                node.right.resolved_type = FLOAT_TYPE
                node.resolved_type = FLOAT_TYPE
                return FLOAT_TYPE
            else:
                self.log_error(node.line, node.column, f"العملية '{node.op}' غير مسموحة بين '{left_type}' و '{right_type}'.")
                return ERROR_TYPE
        # التحقق من معاملات المقارنة
        elif node.op in ['<', '>', '<=', '>=', '==', '!=']:
            if left_type == right_type:
                node.resolved_type = BOOL_TYPE
                return BOOL_TYPE
            else:
                self.log_error(node.line, node.column, f"المقارنة '{node.op}' غير مسموحة بين '{left_type}' و '{right_type}'.")
                return ERROR_TYPE
        # التحقق من معاملات البت (Bitwise) والإزاحة (Shift)
        elif node.op in ['&', '|', '^', '<<', '>>']:
            if left_type == INT_TYPE and right_type == INT_TYPE:
                node.resolved_type = INT_TYPE
                return INT_TYPE
            else:
                self.log_error(node.line, node.column, f"العملية '{node.op}' تتطلب معاملين من نوع 'صحيح'.")
                return ERROR_TYPE
        # التحقق من العمليات المنطقية (و / أو)
        elif node.op in ['و', 'أو']:
            if left_type == BOOL_TYPE and right_type == BOOL_TYPE:
                node.resolved_type = BOOL_TYPE
                return BOOL_TYPE
            else:
                self.log_error(node.line, node.column, f"العملية المنطقية '{node.op}' تتطلب معاملين من نوع 'منطقي'.")
                return ERROR_TYPE
        return ERROR_TYPE

    # 8. زيارة تعريف الدالة
    def visit_FuncDeclNode(self, node: FuncDeclNode):
        type_mapping = {
            'صحيح': INT_TYPE,
            'عشري': FLOAT_TYPE,
            'نص': STRING_TYPE,
            'منطقي': BOOL_TYPE,
            'فارغ': VOID_TYPE
        }
        ret_type = type_mapping.get(node.return_type, ERROR_TYPE)
        func_symbol = FunctionSymbol(node.name, ret_type, len(node.params))
        try:
            self.current_env.define(node.name, func_symbol)
        except SemanticError as e:
            self.log_error(node.line, node.column, str(e))

        previous_func_return_type = self.current_function_return_type
        self.current_function_return_type = ret_type
        # دخول النطاق
        previous_env = self.current_env
        self.current_env = Environment(enclosing=previous_env)

        for param_name, param_type in node.params:
            p_type = type_mapping.get(param_type, STRING_TYPE)
            p_symbol = VariableSymbol(param_name, p_type)
            try:
                self.current_env.define(param_name, p_symbol)
            except SemanticError as e:
                self.log_error(node.line, node.column, str(e))

        if node.body and isinstance(node.body, BlockNode):
            for stmt in node.body.statements:
                stmt.accept(self)

        self.current_env = previous_env
        self.current_function_return_type = previous_func_return_type

    # 9. زيارة بقية العقد
    def visit_FuncCallNode(self, node: FuncCallNode):
        for arg in node.args:
            arg.accept(self)
        try:
            sym = self.current_env.resolve(node.name)
            node.resolved_type = sym.type
            return sym.type
        except SemanticError as e:
            self.log_error(node.line, node.column, str(e))
            return ERROR_TYPE

    def visit_IfNode(self, node: IfNode):
        if node.condition:
            cond_type = node.condition.accept(self)
            if cond_type != ERROR_TYPE and cond_type != BOOL_TYPE:
                self.log_error(node.line, node.column, f"شرط 'لو' يجب أن يكون من نوع 'منطقي' وليس '{cond_type}'.")
        if node.then_block:
            node.then_block.accept(self)
        if node.else_block:
            node.else_block.accept(self)

    def visit_WhileNode(self, node: WhileNode):
        if node.condition:
            cond_type = node.condition.accept(self)
            if cond_type != ERROR_TYPE and cond_type != BOOL_TYPE:
                self.log_error(node.line, node.column, f"شرط 'طالما' يجب أن يكون من نوع 'منطقي' وليس '{cond_type}'.")

        self.loop_depth += 1  # الدخول في حلقة تكرار
        if node.body:
            node.body.accept(self)
        self.loop_depth -= 1  # الخروج من حلقة التكرار

    def visit_ReturnNode(self, node: ReturnNode):
        # 1. Determine what type is being returned
        if node.value:
            ret_type = node.value.accept(self)
        else:
            ret_type = VOID_TYPE

        # 2. Check if the returned type matches the function's expected type
        if self.current_function_return_type:
            if ret_type != ERROR_TYPE and ret_type != self.current_function_return_type:
                self.log_error(
                    node.line,
                    node.column,
                    f"نوع الإرجاع '{ret_type}' لا يتطابق مع نوع الدالة '{self.current_function_return_type}'."
                )
        else:
            self.log_error(node.line, node.column, "لا يمكن استخدام أمر 'ارجع' خارج الدوال.")

        # 3. Save the type for the LLVM Generator!
        node.resolved_type = ret_type

        return ret_type

    def visit_UnaryOpNode(self, node: UnaryOpNode):
        if node.expr:
            return node.expr.accept(self)
        return ERROR_TYPE

    def visit_StringNode(self, node: StringNode):
        return STRING_TYPE

    def visit_CharNode(self, node: CharNode):
        return STRING_TYPE

    def visit_BoolNode(self, node: BoolNode):
        return BOOL_TYPE

    def visit_ImportNode(self, node: ImportNode):
        pass  # الاستيراد لا يحتاج لتحليل أنواع حالياً

    def visit_BreakNode(self, node: BreakNode):
        if self.loop_depth == 0:
            self.log_error(node.line, node.column, "لا يمكن استخدام أمر 'اقطع' خارج حلقات التكرار (طالما).")
        return ERROR_TYPE

    def visit_ContinueNode(self, node: ContinueNode):
        if self.loop_depth == 0:
            self.log_error(node.line, node.column, "لا يمكن استخدام أمر 'استمر' خارج حلقات التكرار (طالما).")
        return ERROR_TYPE
