# ast_nodes.py
from dataclasses import dataclass, field
from typing import Any, List, Optional, Tuple
from abc import ABC, abstractmethod
from ast_dir.visitor_interface import ASTVisitor

@dataclass
class ASTNode(ABC):
    line: int = 0
    column: int = 0
    resolved_type: Any = None  # نوع البيانات بعد التحليل الدلالي
    @abstractmethod
    def accept(self, visitor: 'ASTVisitor'):
        pass

@dataclass
class ProgramNode(ASTNode):
    imports: List[ASTNode] = field(default_factory=list)
    declarations: List[ASTNode] = field(default_factory=list)
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_ProgramNode(self)

@dataclass
class VarDeclNode(ASTNode):
    name: str = ""
    var_type: str = ""
    value: Optional[ASTNode] = None
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_VarDeclNode(self)

@dataclass
class FuncDeclNode(ASTNode):
    name: str = ""
    params: List[Tuple[str, str]] = field(default_factory=list)
    return_type: str = ""
    body: Optional[ASTNode] = None
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_FuncDeclNode(self)

@dataclass
class BlockNode(ASTNode):
    statements: List[ASTNode] = field(default_factory=list)
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_BlockNode(self)

@dataclass
class AssignNode(ASTNode):
    name: str = ""
    op: str = "="
    value: Optional[ASTNode] = None
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_AssignNode(self)

@dataclass
class FuncCallNode(ASTNode):
    name: str = ""
    args: List[ASTNode] = field(default_factory=list)
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_FuncCallNode(self)

@dataclass
class IfNode(ASTNode):
    condition: Optional[ASTNode] = None
    then_block: Optional[ASTNode] = None
    else_block: Optional[ASTNode] = None
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_IfNode(self)

@dataclass
class WhileNode(ASTNode):
    condition: Optional[ASTNode] = None
    body: Optional[ASTNode] = None
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_WhileNode(self)

@dataclass
class ReturnNode(ASTNode):
    value: Optional[ASTNode] = None
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_ReturnNode(self)

@dataclass
class BinOpNode(ASTNode):
    left: Optional[ASTNode] = None
    op: str = ""
    right: Optional[ASTNode] = None
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_BinOpNode(self)

@dataclass
class UnaryOpNode(ASTNode):
    op: str = ""
    expr: Optional[ASTNode] = None
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_UnaryOpNode(self)

@dataclass
class NumberNode(ASTNode):
    value: float = 0.0
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_NumberNode(self)

@dataclass
class StringNode(ASTNode):
    value: str = ""
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_StringNode(self)

@dataclass
class CharNode(ASTNode):
    value: str = ""
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_CharNode(self)

@dataclass
class BoolNode(ASTNode):
    value: bool = False
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_BoolNode(self)

@dataclass
class IdNode(ASTNode):
    name: str = ""
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_IdNode(self)
    

@dataclass
class ImportNode(ASTNode):
    library_name: str = ""
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_ImportNode(self)

@dataclass
class BreakNode(ASTNode):
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_BreakNode(self)

@dataclass
class ContinueNode(ASTNode):
    def accept(self, visitor: 'ASTVisitor'):
        return visitor.visit_ContinueNode(self)