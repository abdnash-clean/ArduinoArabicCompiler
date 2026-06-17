# ast_visualizer.py
import graphviz
from ast_dir.visitor_interface import ASTVisitor
class ASTVisualizerVisitor(ASTVisitor):
    def __init__(self):
        # إنشاء كائن الرسم البياني الموجه
        self.dot = graphviz.Digraph(comment='ArArduino AST', format='png')
        self.dot.attr('node', shape='box', style='rounded,filled', 
                      fillcolor='lightblue', fontname='Arial')

    def render(self, output_filename='ast_output'):
        # توليد وحفظ وعرض الرسمة البيانية بصيغة PNG
        self.dot.render(output_filename, view=True, cleanup=True)

    def add_node_and_edge(self, parent_node, child_node, edge_label=""):
        if child_node is not None:
            # استدعاء زائر العقدة الابن ليرسم نفسه أولاً
            child_node.accept(self)
            # رسم خط يربط بين الأب والابن بالاعتماد على الـ ID الفريد
            self.dot.edge(str(id(parent_node)), str(id(child_node)), label=edge_label)

    def visit_ProgramNode(self, node):
        label = f"Program\n(البرنامج)"
        self.dot.node(str(id(node)), label, fillcolor='lightgray')
        for imp in node.imports:
            self.add_node_and_edge(node, imp)
        for decl in node.declarations:
            self.add_node_and_edge(node, decl)

    def visit_VarDeclNode(self, node):
        label = f"VarDecl\n{node.name} : {node.var_type}\n[سطر: {node.line+1}]"
        self.dot.node(str(id(node)), label, fillcolor='lightgreen')
        self.add_node_and_edge(node, node.value, "value")

    def visit_FuncDeclNode(self, node):
        label = f"FuncDecl\n{node.name} : {node.return_type}\n[سطر: {node.line+1}]"
        self.dot.node(str(id(node)), label, fillcolor='violet')
        self.add_node_and_edge(node, node.body, "body")

    def visit_BlockNode(self, node):
        label = f"Block\n{{...}}"
        self.dot.node(str(id(node)), label, fillcolor='wheat')
        for stmt in node.statements:
            self.add_node_and_edge(node, stmt)

    def visit_AssignNode(self, node):
        label = f"Assign\n{node.name} {node.op}\n[سطر: {node.line+1}]"
        self.dot.node(str(id(node)), label, fillcolor='lightyellow')
        self.add_node_and_edge(node, node.value, "value")

    def visit_FuncCallNode(self, node):
        label = f"Call\n{node.name}()\n[سطر: {node.line+1}]"
        self.dot.node(str(id(node)), label, fillcolor='pink')
        for arg in node.args:
            self.add_node_and_edge(node, arg, "arg")

    def visit_IfNode(self, node):
        label = f"If\n[سطر: {node.line+1}]"
        self.dot.node(str(id(node)), label, fillcolor='orange')
        self.add_node_and_edge(node, node.condition, "condition")
        self.add_node_and_edge(node, node.then_block, "then")
        if node.else_block:
            self.add_node_and_edge(node, node.else_block, "else")

    def visit_WhileNode(self, node):
        label = f"While\n[سطر: {node.line+1}]"
        self.dot.node(str(id(node)), label, fillcolor='orange')
        self.add_node_and_edge(node, node.condition, "condition")
        self.add_node_and_edge(node, node.body, "body")

    def visit_ReturnNode(self, node):
        label = f"Return\n[سطر: {node.line+1}]"
        self.dot.node(str(id(node)), label, fillcolor='red')
        if node.value:
            self.add_node_and_edge(node, node.value, "val")

    def visit_BinOpNode(self, node):
        label = f"BinOp\n'{node.op}'"
        self.dot.node(str(id(node)), label, fillcolor='lightyellow')
        self.add_node_and_edge(node, node.left, "left")
        self.add_node_and_edge(node, node.right, "right")

    def visit_UnaryOpNode(self, node):
        label = f"UnaryOp\n'{node.op}'"
        self.dot.node(str(id(node)), label, fillcolor='lightyellow')
        self.add_node_and_edge(node, node.expr, "expr")

    def visit_NumberNode(self, node):
        label = f"Num: {node.value}"
        self.dot.node(str(id(node)), label, fillcolor='white')

    def visit_StringNode(self, node):
        label = f"Str: \"{node.value}\""
        self.dot.node(str(id(node)), label, fillcolor='white')

    def visit_CharNode(self, node):
        label = f"Char: '{node.value}'"
        self.dot.node(str(id(node)), label, fillcolor='white')

    def visit_BoolNode(self, node):
        label = f"Bool: {node.value}"
        self.dot.node(str(id(node)), label, fillcolor='white')

    def visit_IdNode(self, node):
        label = f"Id: {node.name}"
        self.dot.node(str(id(node)), label, fillcolor='white')


    def visit_ImportNode(self, node):
        label = f"Import\n\"{node.library_name}\"\n[سطر: {node.line+1}]"
        self.dot.node(str(id(node)), label, fillcolor='lightblue')

    def visit_BreakNode(self, node):
        label = f"Break\n(اقطع)\n[سطر: {node.line+1}]"
        self.dot.node(str(id(node)), label, fillcolor='tomato')

    def visit_ContinueNode(self, node):
        label = f"Continue\n(استمر)\n[سطر: {node.line+1}]"
        self.dot.node(str(id(node)), label, fillcolor='lightsalmon')