# frontend/ast_builder.py
from frontend.ArArduinoParserVisitor import ArArduinoParserVisitor
from frontend.ArArduinoParser import ArArduinoParser
from ast_dir.nodes import *

class ASTBuilderVisitor(ArArduinoParserVisitor):
    # دالة مساعدة لنسخ رقم السطر والعمود الأصلي من ملف الكود إلى عقدة الـ AST
    def set_metadata(self, node: ASTNode, ctx):
        if node and ctx and ctx.start:
            node.line = ctx.start.line
            node.column = ctx.start.column
        return node

    def visitProgram(self, ctx: ArArduinoParser.ProgramContext):
        imports = [self.visit(imp) for imp in ctx.importStmt()] if ctx.importStmt() else []
        declarations = [self.visit(decl) for decl in ctx.declaration()]
        node = ProgramNode(imports=imports, declarations=declarations)
        return self.set_metadata(node, ctx)
    
    def visitDeclaration(self, ctx: ArArduinoParser.DeclarationContext):
        if ctx.varDecl():
            return self.visit(ctx.varDecl())
        elif ctx.funDecl():
            return self.visit(ctx.funDecl())

    def visitVarDecl(self, ctx: ArArduinoParser.VarDeclContext):
        name = ctx.ID().getText()
        var_type = ctx.type_().getText()
        value = self.visit(ctx.expression())
        node = VarDeclNode(name=name, var_type=var_type, value=value)
        return self.set_metadata(node, ctx)

    def visitFunDecl(self, ctx: ArArduinoParser.FunDeclContext):
        return self.visit(ctx.funcBody())

    def visitFuncBody(self, ctx: ArArduinoParser.FuncBodyContext):
        if ctx.SETUP():
            name = ctx.SETUP().getText()  # 'إعداد'
            params = []
            return_type = "فارغ"
            body = self.visit(ctx.block())
        elif ctx.LOOP():
            name = ctx.LOOP().getText()   # 'تكرار'
            params = []
            return_type = "فارغ"
            body = self.visit(ctx.block())
        else:
            name = ctx.ID().getText()
            params = self.visit(ctx.params()) if ctx.params() else []
            return_type = ctx.type_().getText()
            body = self.visit(ctx.block())
        node = FuncDeclNode(name=name, params=params, return_type=return_type, body=body)
        return self.set_metadata(node, ctx)

    def visitParams(self, ctx: ArArduinoParser.ParamsContext):
        return [self.visit(param) for param in ctx.param()]

    def visitParam(self, ctx: ArArduinoParser.ParamContext):
        name = ctx.ID().getText()
        param_type = ctx.type_().getText()
        return (name, param_type)

    def visitBlock(self, ctx: ArArduinoParser.BlockContext):
        statements = []
        for stmt in ctx.statement():
            node = self.visit(stmt)
            if node:
                statements.append(node)
        # استخدام الاسم المفتاحية statements= لمنع بايثون من الخلط
        node = BlockNode(statements=statements)
        return self.set_metadata(node, ctx)

    def visitStatement(self, ctx: ArArduinoParser.StatementContext):
        if ctx.varDecl(): return self.visit(ctx.varDecl())
        elif ctx.idStatement(): return self.visit(ctx.idStatement())
        elif ctx.ifStat(): return self.visit(ctx.ifStat())
        elif ctx.whileStat(): return self.visit(ctx.whileStat())
        elif ctx.returnStat(): return self.visit(ctx.returnStat())
        elif ctx.breakStat(): return self.visit(ctx.breakStat())     
        elif ctx.continueStat(): return self.visit(ctx.continueStat())    
        elif ctx.block(): return self.visit(ctx.block())
        return None

    def visitIdStatement(self, ctx: ArArduinoParser.IdStatementContext):
        name = ctx.ID().getText()
        suffix = ctx.idSuffix()
        node = None
        
        if suffix.ASSIGN():
            val = self.visit(suffix.expression())
            node = AssignNode(name=name, op='=', value=val)
        elif suffix.ADD_ASSIGN():
            val = self.visit(suffix.expression())
            desugared_value = BinOpNode(left=IdNode(name=name), op='+', right=val)
            node = AssignNode(name=name, op='=', value=desugared_value)
        elif suffix.SUB_ASSIGN():
            val = self.visit(suffix.expression())
            desugared_value = BinOpNode(left=IdNode(name=name), op='-', right=val)
            node = AssignNode(name=name, op='=', value=desugared_value)
        elif suffix.INC():
            desugared_value = BinOpNode(left=IdNode(name=name), op='+', right=NumberNode(value=1.0))
            node = AssignNode(name=name, op='=', value=desugared_value)
        elif suffix.DEC():
            desugared_value = BinOpNode(left=IdNode(name=name), op='-', right=NumberNode(value=1.0))
            node = AssignNode(name=name, op='=', value=desugared_value)
        elif suffix.LPAREN():
            args = self.visit(suffix.args()) if suffix.args() else []
            node = FuncCallNode(name=name, args=args)
            
        return self.set_metadata(node, ctx)

    def visitArgs(self, ctx: ArArduinoParser.ArgsContext):
        return [self.visit(expr) for expr in ctx.expression()]

    def visitIfStat(self, ctx: ArArduinoParser.IfStatContext):
        cond = self.visit(ctx.expression())
        then_b = self.visit(ctx.block(0))
        else_b = self.visit(ctx.block(1)) if ctx.block(1) else None
        node = IfNode(condition=cond, then_block=then_b, else_block=else_b)
        return self.set_metadata(node, ctx)

    def visitWhileStat(self, ctx: ArArduinoParser.WhileStatContext):
        cond = self.visit(ctx.expression())
        body = self.visit(ctx.block())
        node = WhileNode(condition=cond, body=body)
        return self.set_metadata(node, ctx)

    def visitReturnStat(self, ctx: ArArduinoParser.ReturnStatContext):
        val = self.visit(ctx.expression()) if ctx.expression() else None
        node = ReturnNode(value=val)
        return self.set_metadata(node, ctx)

    def visitExpression(self, ctx: ArArduinoParser.ExpressionContext):
        return self.visit(ctx.orExpr())

    def visitOrExpr(self, ctx: ArArduinoParser.OrExprContext):
        left = self.visit(ctx.andExpr(0))
        for i in range(1, len(ctx.andExpr())):
            right = self.visit(ctx.andExpr(i))
            left = BinOpNode(left=left, op='أو', right=right)
        return self.set_metadata(left, ctx)

    def visitAndExpr(self, ctx: ArArduinoParser.AndExprContext):
        left = self.visit(ctx.bwOrExpr(0))
        for i in range(1, len(ctx.bwOrExpr())):
            right = self.visit(ctx.bwOrExpr(i))
            left = BinOpNode(left=left, op='و', right=right)
        return self.set_metadata(left, ctx)

    def visitBwOrExpr(self, ctx: ArArduinoParser.BwOrExprContext):
        left = self.visit(ctx.bwXorExpr(0))
        for i in range(1, len(ctx.bwXorExpr())):
            right = self.visit(ctx.bwXorExpr(i))
            left = BinOpNode(left=left, op='|', right=right)
        return self.set_metadata(left, ctx)

    def visitBwXorExpr(self, ctx: ArArduinoParser.BwXorExprContext):
        left = self.visit(ctx.bwAndExpr(0))
        for i in range(1, len(ctx.bwAndExpr())):
            right = self.visit(ctx.bwAndExpr(i))
            left = BinOpNode(left=left, op='^', right=right)
        return self.set_metadata(left, ctx)

    def visitBwAndExpr(self, ctx: ArArduinoParser.BwAndExprContext):
        left = self.visit(ctx.relExpr(0))
        for i in range(1, len(ctx.relExpr())):
            right = self.visit(ctx.relExpr(i))
            left = BinOpNode(left=left, op='&', right=right)
        return self.set_metadata(left, ctx)

    def visitRelExpr(self, ctx: ArArduinoParser.RelExprContext):
        left = self.visit(ctx.addExpr(0))
        for i in range(1, len(ctx.addExpr())):
            right = self.visit(ctx.addExpr(i))
            op = ctx.relOp(i-1).getText()
            left = BinOpNode(left=left, op=op, right=right)
        return self.set_metadata(left, ctx)

    def visitAddExpr(self, ctx: ArArduinoParser.AddExprContext):
        left = self.visit(ctx.mulExpr(0))
        for i in range(1, len(ctx.mulExpr())):
            right = self.visit(ctx.mulExpr(i))
            op_ctx = ctx.getChild(2 * i - 1)
            op = op_ctx.getText()
            left = BinOpNode(left=left, op=op, right=right)
        return self.set_metadata(left, ctx)

    def visitMulExpr(self, ctx: ArArduinoParser.MulExprContext):
        left = self.visit(ctx.unaryExpr(0))
        for i in range(1, len(ctx.unaryExpr())):
            right = self.visit(ctx.unaryExpr(i))
            op_ctx = ctx.getChild(2 * i - 1)
            op = op_ctx.getText()
            left = BinOpNode(left=left, op=op, right=right)
        return self.set_metadata(left, ctx)

    def visitUnaryExpr(self, ctx: ArArduinoParser.UnaryExprContext):
        if ctx.primary():
            return self.visit(ctx.primary())
        op = ctx.getChild(0).getText()
        expr = self.visit(ctx.unaryExpr())
        node = UnaryOpNode(op=op, expr=expr)
        return self.set_metadata(node, ctx)

    def visitPrimary(self, ctx: ArArduinoParser.PrimaryContext):
        node = None
        if ctx.NUMBER():
            val = float(ctx.NUMBER().getText())
            node = NumberNode(value=val)
        elif ctx.TRUE():
            node = BoolNode(value=True)
        elif ctx.FALSE():
            node = BoolNode(value=False)
        elif ctx.STRING():
            text = ctx.STRING().getText()[1:-1]
            node = StringNode(value=text)
        elif ctx.CHAR():
            char_val = ctx.CHAR().getText()[1:-1]
            node = CharNode(value=char_val)
        elif ctx.LPAREN():
            return self.visit(ctx.expression())
        elif ctx.ID():
            name = ctx.ID().getText()
            suffix = ctx.primaryIdSuffix()
            if suffix.LPAREN():
                args = self.visit(suffix.args()) if suffix.args() else []
                node = FuncCallNode(name=name, args=args)
            else:
                node = IdNode(name=name)
        return self.set_metadata(node, ctx)
    
    def visitImportStmt(self, ctx: ArArduinoParser.ImportStmtContext):
        lib_name = ctx.STRING().getText()[1:-1]
        node = ImportNode(library_name=lib_name)
        return self.set_metadata(node, ctx)

    def visitBreakStat(self, ctx: ArArduinoParser.BreakStatContext):
        node = BreakNode()
        return self.set_metadata(node, ctx)

    def visitContinueStat(self, ctx: ArArduinoParser.ContinueStatContext):
        node = ContinueNode()
        return self.set_metadata(node, ctx)