# visitor_interface.py
from abc import ABC, abstractmethod

class ASTVisitor(ABC):
    @abstractmethod
    def visit_ProgramNode(self, node): pass
    @abstractmethod
    def visit_VarDeclNode(self, node): pass
    @abstractmethod
    def visit_FuncDeclNode(self, node): pass
    @abstractmethod
    def visit_BlockNode(self, node): pass
    @abstractmethod
    def visit_AssignNode(self, node): pass
    @abstractmethod
    def visit_FuncCallNode(self, node): pass
    @abstractmethod
    def visit_IfNode(self, node): pass
    @abstractmethod
    def visit_WhileNode(self, node): pass
    @abstractmethod
    def visit_ReturnNode(self, node): pass
    @abstractmethod
    def visit_BinOpNode(self, node): pass
    @abstractmethod
    def visit_UnaryOpNode(self, node): pass
    @abstractmethod
    def visit_NumberNode(self, node): pass
    @abstractmethod
    def visit_StringNode(self, node): pass
    @abstractmethod
    def visit_CharNode(self, node): pass
    @abstractmethod
    def visit_BoolNode(self, node): pass
    @abstractmethod
    def visit_IdNode(self, node): pass
    @abstractmethod
    def visit_ImportNode(self, node): pass
    @abstractmethod
    def visit_BreakNode(self, node): pass
    @abstractmethod
    def visit_ContinueNode(self, node): pass