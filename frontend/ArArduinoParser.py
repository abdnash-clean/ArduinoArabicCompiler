# Generated from ArArduinoParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,61,314,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        5,0,68,8,0,10,0,12,0,71,9,0,1,0,5,0,74,8,0,10,0,12,0,77,9,0,1,0,
        1,0,1,1,1,1,1,1,1,1,1,2,1,2,3,2,87,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,3,5,115,8,5,1,5,1,5,1,5,1,5,1,5,3,5,122,8,5,1,6,1,
        6,1,6,5,6,127,8,6,10,6,12,6,130,9,6,1,7,1,7,1,7,1,7,1,8,1,8,5,8,
        138,8,8,10,8,12,8,141,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,3,9,158,8,9,1,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,3,11,170,8,11,1,11,3,11,173,8,11,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,3,12,182,8,12,1,13,1,13,1,13,1,13,1,13,1,
        13,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,3,16,198,8,16,1,17,1,
        17,1,17,5,17,203,8,17,10,17,12,17,206,9,17,1,18,1,18,1,19,1,19,1,
        19,5,19,213,8,19,10,19,12,19,216,9,19,1,20,1,20,1,20,5,20,221,8,
        20,10,20,12,20,224,9,20,1,21,1,21,1,21,5,21,229,8,21,10,21,12,21,
        232,9,21,1,22,1,22,1,22,5,22,237,8,22,10,22,12,22,240,9,22,1,23,
        1,23,1,23,5,23,245,8,23,10,23,12,23,248,9,23,1,24,1,24,1,24,1,24,
        5,24,254,8,24,10,24,12,24,257,9,24,1,25,1,25,1,26,1,26,1,26,5,26,
        264,8,26,10,26,12,26,267,9,26,1,27,1,27,1,27,5,27,272,8,27,10,27,
        12,27,275,9,27,1,28,1,28,1,28,5,28,280,8,28,10,28,12,28,283,9,28,
        1,29,1,29,1,29,3,29,288,8,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,
        1,30,1,30,1,30,1,30,1,30,3,30,302,8,30,1,31,1,31,3,31,306,8,31,1,
        31,1,31,3,31,310,8,31,1,32,1,32,1,32,0,0,33,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,0,8,1,0,26,27,1,0,24,25,1,0,31,36,1,0,29,30,1,0,20,21,1,0,
        22,23,3,0,21,21,39,39,50,50,3,0,7,9,14,14,51,52,322,0,69,1,0,0,0,
        2,80,1,0,0,0,4,86,1,0,0,0,6,88,1,0,0,0,8,96,1,0,0,0,10,121,1,0,0,
        0,12,123,1,0,0,0,14,131,1,0,0,0,16,135,1,0,0,0,18,157,1,0,0,0,20,
        159,1,0,0,0,22,172,1,0,0,0,24,174,1,0,0,0,26,183,1,0,0,0,28,189,
        1,0,0,0,30,192,1,0,0,0,32,195,1,0,0,0,34,199,1,0,0,0,36,207,1,0,
        0,0,38,209,1,0,0,0,40,217,1,0,0,0,42,225,1,0,0,0,44,233,1,0,0,0,
        46,241,1,0,0,0,48,249,1,0,0,0,50,258,1,0,0,0,52,260,1,0,0,0,54,268,
        1,0,0,0,56,276,1,0,0,0,58,287,1,0,0,0,60,301,1,0,0,0,62,309,1,0,
        0,0,64,311,1,0,0,0,66,68,3,2,1,0,67,66,1,0,0,0,68,71,1,0,0,0,69,
        67,1,0,0,0,69,70,1,0,0,0,70,75,1,0,0,0,71,69,1,0,0,0,72,74,3,4,2,
        0,73,72,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,
        1,0,0,0,77,75,1,0,0,0,78,79,5,0,0,1,79,1,1,0,0,0,80,81,5,55,0,0,
        81,82,5,53,0,0,82,83,5,45,0,0,83,3,1,0,0,0,84,87,3,6,3,0,85,87,3,
        8,4,0,86,84,1,0,0,0,86,85,1,0,0,0,87,5,1,0,0,0,88,89,5,1,0,0,89,
        90,5,58,0,0,90,91,5,44,0,0,91,92,3,64,32,0,92,93,5,19,0,0,93,94,
        3,36,18,0,94,95,5,45,0,0,95,7,1,0,0,0,96,97,5,10,0,0,97,98,3,10,
        5,0,98,9,1,0,0,0,99,100,5,12,0,0,100,101,5,40,0,0,101,102,5,41,0,
        0,102,103,5,44,0,0,103,104,5,9,0,0,104,122,3,16,8,0,105,106,5,13,
        0,0,106,107,5,40,0,0,107,108,5,41,0,0,108,109,5,44,0,0,109,110,5,
        9,0,0,110,122,3,16,8,0,111,112,5,58,0,0,112,114,5,40,0,0,113,115,
        3,12,6,0,114,113,1,0,0,0,114,115,1,0,0,0,115,116,1,0,0,0,116,117,
        5,41,0,0,117,118,5,44,0,0,118,119,3,64,32,0,119,120,3,16,8,0,120,
        122,1,0,0,0,121,99,1,0,0,0,121,105,1,0,0,0,121,111,1,0,0,0,122,11,
        1,0,0,0,123,128,3,14,7,0,124,125,5,46,0,0,125,127,3,14,7,0,126,124,
        1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,13,1,
        0,0,0,130,128,1,0,0,0,131,132,5,58,0,0,132,133,5,44,0,0,133,134,
        3,64,32,0,134,15,1,0,0,0,135,139,5,42,0,0,136,138,3,18,9,0,137,136,
        1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,142,
        1,0,0,0,141,139,1,0,0,0,142,143,5,43,0,0,143,17,1,0,0,0,144,158,
        3,6,3,0,145,146,3,20,10,0,146,147,5,45,0,0,147,158,1,0,0,0,148,158,
        3,24,12,0,149,158,3,26,13,0,150,151,3,32,16,0,151,152,5,45,0,0,152,
        158,1,0,0,0,153,158,3,28,14,0,154,158,3,30,15,0,155,158,3,16,8,0,
        156,158,5,45,0,0,157,144,1,0,0,0,157,145,1,0,0,0,157,148,1,0,0,0,
        157,149,1,0,0,0,157,150,1,0,0,0,157,153,1,0,0,0,157,154,1,0,0,0,
        157,155,1,0,0,0,157,156,1,0,0,0,158,19,1,0,0,0,159,160,5,58,0,0,
        160,161,3,22,11,0,161,21,1,0,0,0,162,163,5,19,0,0,163,173,3,36,18,
        0,164,165,7,0,0,0,165,173,3,36,18,0,166,173,7,1,0,0,167,169,5,40,
        0,0,168,170,3,34,17,0,169,168,1,0,0,0,169,170,1,0,0,0,170,171,1,
        0,0,0,171,173,5,41,0,0,172,162,1,0,0,0,172,164,1,0,0,0,172,166,1,
        0,0,0,172,167,1,0,0,0,173,23,1,0,0,0,174,175,5,2,0,0,175,176,5,40,
        0,0,176,177,3,36,18,0,177,178,5,41,0,0,178,181,3,16,8,0,179,180,
        5,3,0,0,180,182,3,16,8,0,181,179,1,0,0,0,181,182,1,0,0,0,182,25,
        1,0,0,0,183,184,5,4,0,0,184,185,5,40,0,0,185,186,3,36,18,0,186,187,
        5,41,0,0,187,188,3,16,8,0,188,27,1,0,0,0,189,190,5,15,0,0,190,191,
        5,45,0,0,191,29,1,0,0,0,192,193,5,16,0,0,193,194,5,45,0,0,194,31,
        1,0,0,0,195,197,5,11,0,0,196,198,3,36,18,0,197,196,1,0,0,0,197,198,
        1,0,0,0,198,33,1,0,0,0,199,204,3,36,18,0,200,201,5,46,0,0,201,203,
        3,36,18,0,202,200,1,0,0,0,203,206,1,0,0,0,204,202,1,0,0,0,204,205,
        1,0,0,0,205,35,1,0,0,0,206,204,1,0,0,0,207,208,3,38,19,0,208,37,
        1,0,0,0,209,214,3,40,20,0,210,211,5,37,0,0,211,213,3,40,20,0,212,
        210,1,0,0,0,213,216,1,0,0,0,214,212,1,0,0,0,214,215,1,0,0,0,215,
        39,1,0,0,0,216,214,1,0,0,0,217,222,3,42,21,0,218,219,5,38,0,0,219,
        221,3,42,21,0,220,218,1,0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,222,
        223,1,0,0,0,223,41,1,0,0,0,224,222,1,0,0,0,225,230,3,44,22,0,226,
        227,5,47,0,0,227,229,3,44,22,0,228,226,1,0,0,0,229,232,1,0,0,0,230,
        228,1,0,0,0,230,231,1,0,0,0,231,43,1,0,0,0,232,230,1,0,0,0,233,238,
        3,46,23,0,234,235,5,49,0,0,235,237,3,46,23,0,236,234,1,0,0,0,237,
        240,1,0,0,0,238,236,1,0,0,0,238,239,1,0,0,0,239,45,1,0,0,0,240,238,
        1,0,0,0,241,246,3,48,24,0,242,243,5,48,0,0,243,245,3,48,24,0,244,
        242,1,0,0,0,245,248,1,0,0,0,246,244,1,0,0,0,246,247,1,0,0,0,247,
        47,1,0,0,0,248,246,1,0,0,0,249,255,3,52,26,0,250,251,3,50,25,0,251,
        252,3,52,26,0,252,254,1,0,0,0,253,250,1,0,0,0,254,257,1,0,0,0,255,
        253,1,0,0,0,255,256,1,0,0,0,256,49,1,0,0,0,257,255,1,0,0,0,258,259,
        7,2,0,0,259,51,1,0,0,0,260,265,3,54,27,0,261,262,7,3,0,0,262,264,
        3,54,27,0,263,261,1,0,0,0,264,267,1,0,0,0,265,263,1,0,0,0,265,266,
        1,0,0,0,266,53,1,0,0,0,267,265,1,0,0,0,268,273,3,56,28,0,269,270,
        7,4,0,0,270,272,3,56,28,0,271,269,1,0,0,0,272,275,1,0,0,0,273,271,
        1,0,0,0,273,274,1,0,0,0,274,55,1,0,0,0,275,273,1,0,0,0,276,281,3,
        58,29,0,277,278,7,5,0,0,278,280,3,58,29,0,279,277,1,0,0,0,280,283,
        1,0,0,0,281,279,1,0,0,0,281,282,1,0,0,0,282,57,1,0,0,0,283,281,1,
        0,0,0,284,285,7,6,0,0,285,288,3,58,29,0,286,288,3,60,30,0,287,284,
        1,0,0,0,287,286,1,0,0,0,288,59,1,0,0,0,289,302,5,57,0,0,290,302,
        5,56,0,0,291,302,5,5,0,0,292,302,5,54,0,0,293,302,5,53,0,0,294,302,
        5,6,0,0,295,296,5,40,0,0,296,297,3,36,18,0,297,298,5,41,0,0,298,
        302,1,0,0,0,299,300,5,58,0,0,300,302,3,62,31,0,301,289,1,0,0,0,301,
        290,1,0,0,0,301,291,1,0,0,0,301,292,1,0,0,0,301,293,1,0,0,0,301,
        294,1,0,0,0,301,295,1,0,0,0,301,299,1,0,0,0,302,61,1,0,0,0,303,305,
        5,40,0,0,304,306,3,34,17,0,305,304,1,0,0,0,305,306,1,0,0,0,306,307,
        1,0,0,0,307,310,5,41,0,0,308,310,1,0,0,0,309,303,1,0,0,0,309,308,
        1,0,0,0,310,63,1,0,0,0,311,312,7,7,0,0,312,65,1,0,0,0,26,69,75,86,
        114,121,128,139,157,169,172,181,197,204,214,222,230,238,246,255,
        265,273,281,287,301,305,309
    ]

class ArArduinoParser ( Parser ):

    grammarFileName = "ArArduinoParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\u0645\\u062A\\u063A\\u064A\\u0631'", 
                     "<INVALID>", "'\\u0648\\u0627\\u0644\\u0627'", "'\\u0637\\u0627\\u0644\\u0645\\u0627'", 
                     "'\\u0635\\u062D'", "'\\u063A\\u0644\\u0637'", "<INVALID>", 
                     "<INVALID>", "'\\u0641\\u0627\\u0631\\u063A'", "<INVALID>", 
                     "'\\u0627\\u0631\\u062C\\u0639'", "'\\u0627\\u0639\\u062F\\u0627\\u062F'", 
                     "<INVALID>", "'\\u0645\\u0646\\u0637\\u0642\\u064A'", 
                     "'\\u0627\\u0642\\u0637\\u0639'", "'\\u062A\\u062C\\u0627\\u0648\\u0632'", 
                     "'\\u0646\\u0641\\u0630'", "'\\u0627\\u0643\\u062A\\u0628'", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'++'", "'--'", 
                     "'+='", "'-='", "'%'", "'<<'", "'>>'", "'>='", "'<='", 
                     "'=='", "'!='", "'>'", "'<'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "':'", "'\\u061B'", 
                     "'\\u060C'", "'|'", "'&'", "'^'", "'~'", "'\\u0646\\u0635'", 
                     "'\\u062D\\u0631\\u0641'" ]

    symbolicNames = [ "<INVALID>", "VAR", "IF", "ELSE", "WHILE", "TRUE", 
                      "FALSE", "INT_T", "FLOAT_T", "VOID", "FUNCTION", "RETURN", 
                      "SETUP", "LOOP", "BOOL", "BREAK", "CONTINUE", "DO", 
                      "PRINT", "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", 
                      "INC", "DEC", "ADD_ASSIGN", "SUB_ASSIGN", "MOD", "SHL", 
                      "SHR", "GTE", "LTE", "EQ", "NEQ", "GT", "LT", "OR", 
                      "AND", "NOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "COLON", "SEMI", "COMA", "BW_OR", "BW_AND", "BW_XOR", 
                      "BW_NOT", "STRING_T", "CHAR_T", "STRING", "CHAR", 
                      "IMPORT", "BIN_NUMBER", "NUMBER", "ID", "WS", "LINE_COMMENT", 
                      "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_importStmt = 1
    RULE_declaration = 2
    RULE_varDecl = 3
    RULE_funDecl = 4
    RULE_funcBody = 5
    RULE_params = 6
    RULE_param = 7
    RULE_block = 8
    RULE_statement = 9
    RULE_idStatement = 10
    RULE_idSuffix = 11
    RULE_ifStat = 12
    RULE_whileStat = 13
    RULE_breakStat = 14
    RULE_continueStat = 15
    RULE_returnStat = 16
    RULE_args = 17
    RULE_expression = 18
    RULE_orExpr = 19
    RULE_andExpr = 20
    RULE_bwOrExpr = 21
    RULE_bwXorExpr = 22
    RULE_bwAndExpr = 23
    RULE_relExpr = 24
    RULE_relOp = 25
    RULE_shiftExpr = 26
    RULE_addExpr = 27
    RULE_mulExpr = 28
    RULE_unaryExpr = 29
    RULE_primary = 30
    RULE_primaryIdSuffix = 31
    RULE_type = 32

    ruleNames =  [ "program", "importStmt", "declaration", "varDecl", "funDecl", 
                   "funcBody", "params", "param", "block", "statement", 
                   "idStatement", "idSuffix", "ifStat", "whileStat", "breakStat", 
                   "continueStat", "returnStat", "args", "expression", "orExpr", 
                   "andExpr", "bwOrExpr", "bwXorExpr", "bwAndExpr", "relExpr", 
                   "relOp", "shiftExpr", "addExpr", "mulExpr", "unaryExpr", 
                   "primary", "primaryIdSuffix", "type" ]

    EOF = Token.EOF
    VAR=1
    IF=2
    ELSE=3
    WHILE=4
    TRUE=5
    FALSE=6
    INT_T=7
    FLOAT_T=8
    VOID=9
    FUNCTION=10
    RETURN=11
    SETUP=12
    LOOP=13
    BOOL=14
    BREAK=15
    CONTINUE=16
    DO=17
    PRINT=18
    ASSIGN=19
    PLUS=20
    MINUS=21
    MUL=22
    DIV=23
    INC=24
    DEC=25
    ADD_ASSIGN=26
    SUB_ASSIGN=27
    MOD=28
    SHL=29
    SHR=30
    GTE=31
    LTE=32
    EQ=33
    NEQ=34
    GT=35
    LT=36
    OR=37
    AND=38
    NOT=39
    LPAREN=40
    RPAREN=41
    LBRACE=42
    RBRACE=43
    COLON=44
    SEMI=45
    COMA=46
    BW_OR=47
    BW_AND=48
    BW_XOR=49
    BW_NOT=50
    STRING_T=51
    CHAR_T=52
    STRING=53
    CHAR=54
    IMPORT=55
    BIN_NUMBER=56
    NUMBER=57
    ID=58
    WS=59
    LINE_COMMENT=60
    BLOCK_COMMENT=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ArArduinoParser.EOF, 0)

        def importStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArArduinoParser.ImportStmtContext)
            else:
                return self.getTypedRuleContext(ArArduinoParser.ImportStmtContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArArduinoParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(ArArduinoParser.DeclarationContext,i)


        def getRuleIndex(self):
            return ArArduinoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ArArduinoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==55:
                self.state = 66
                self.importStmt()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==10:
                self.state = 72
                self.declaration()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(ArArduinoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(ArArduinoParser.IMPORT, 0)

        def STRING(self):
            return self.getToken(ArArduinoParser.STRING, 0)

        def SEMI(self):
            return self.getToken(ArArduinoParser.SEMI, 0)

        def getRuleIndex(self):
            return ArArduinoParser.RULE_importStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportStmt" ):
                listener.enterImportStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportStmt" ):
                listener.exitImportStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportStmt" ):
                return visitor.visitImportStmt(self)
            else:
                return visitor.visitChildren(self)




    def importStmt(self):

        localctx = ArArduinoParser.ImportStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_importStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(ArArduinoParser.IMPORT)
            self.state = 81
            self.match(ArArduinoParser.STRING)
            self.state = 82
            self.match(ArArduinoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(ArArduinoParser.VarDeclContext,0)


        def funDecl(self):
            return self.getTypedRuleContext(ArArduinoParser.FunDeclContext,0)


        def getRuleIndex(self):
            return ArArduinoParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = ArArduinoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.varDecl()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.funDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ArArduinoParser.VAR, 0)

        def ID(self):
            return self.getToken(ArArduinoParser.ID, 0)

        def COLON(self):
            return self.getToken(ArArduinoParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(ArArduinoParser.TypeContext,0)


        def ASSIGN(self):
            return self.getToken(ArArduinoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ArArduinoParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(ArArduinoParser.SEMI, 0)

        def getRuleIndex(self):
            return ArArduinoParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = ArArduinoParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(ArArduinoParser.VAR)
            self.state = 89
            self.match(ArArduinoParser.ID)
            self.state = 90
            self.match(ArArduinoParser.COLON)
            self.state = 91
            self.type_()
            self.state = 92
            self.match(ArArduinoParser.ASSIGN)
            self.state = 93
            self.expression()
            self.state = 94
            self.match(ArArduinoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(ArArduinoParser.FUNCTION, 0)

        def funcBody(self):
            return self.getTypedRuleContext(ArArduinoParser.FuncBodyContext,0)


        def getRuleIndex(self):
            return ArArduinoParser.RULE_funDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunDecl" ):
                listener.enterFunDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunDecl" ):
                listener.exitFunDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunDecl" ):
                return visitor.visitFunDecl(self)
            else:
                return visitor.visitChildren(self)




    def funDecl(self):

        localctx = ArArduinoParser.FunDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(ArArduinoParser.FUNCTION)
            self.state = 97
            self.funcBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SETUP(self):
            return self.getToken(ArArduinoParser.SETUP, 0)

        def LPAREN(self):
            return self.getToken(ArArduinoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ArArduinoParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(ArArduinoParser.COLON, 0)

        def VOID(self):
            return self.getToken(ArArduinoParser.VOID, 0)

        def block(self):
            return self.getTypedRuleContext(ArArduinoParser.BlockContext,0)


        def LOOP(self):
            return self.getToken(ArArduinoParser.LOOP, 0)

        def ID(self):
            return self.getToken(ArArduinoParser.ID, 0)

        def type_(self):
            return self.getTypedRuleContext(ArArduinoParser.TypeContext,0)


        def params(self):
            return self.getTypedRuleContext(ArArduinoParser.ParamsContext,0)


        def getRuleIndex(self):
            return ArArduinoParser.RULE_funcBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncBody" ):
                listener.enterFuncBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncBody" ):
                listener.exitFuncBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncBody" ):
                return visitor.visitFuncBody(self)
            else:
                return visitor.visitChildren(self)




    def funcBody(self):

        localctx = ArArduinoParser.FuncBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_funcBody)
        self._la = 0 # Token type
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.match(ArArduinoParser.SETUP)
                self.state = 100
                self.match(ArArduinoParser.LPAREN)
                self.state = 101
                self.match(ArArduinoParser.RPAREN)
                self.state = 102
                self.match(ArArduinoParser.COLON)
                self.state = 103
                self.match(ArArduinoParser.VOID)
                self.state = 104
                self.block()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(ArArduinoParser.LOOP)
                self.state = 106
                self.match(ArArduinoParser.LPAREN)
                self.state = 107
                self.match(ArArduinoParser.RPAREN)
                self.state = 108
                self.match(ArArduinoParser.COLON)
                self.state = 109
                self.match(ArArduinoParser.VOID)
                self.state = 110
                self.block()
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
                self.match(ArArduinoParser.ID)
                self.state = 112
                self.match(ArArduinoParser.LPAREN)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==58:
                    self.state = 113
                    self.params()


                self.state = 116
                self.match(ArArduinoParser.RPAREN)
                self.state = 117
                self.match(ArArduinoParser.COLON)
                self.state = 118
                self.type_()
                self.state = 119
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArArduinoParser.ParamContext)
            else:
                return self.getTypedRuleContext(ArArduinoParser.ParamContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ArArduinoParser.COMA)
            else:
                return self.getToken(ArArduinoParser.COMA, i)

        def getRuleIndex(self):
            return ArArduinoParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = ArArduinoParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.param()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 124
                self.match(ArArduinoParser.COMA)
                self.state = 125
                self.param()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ArArduinoParser.ID, 0)

        def COLON(self):
            return self.getToken(ArArduinoParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(ArArduinoParser.TypeContext,0)


        def getRuleIndex(self):
            return ArArduinoParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = ArArduinoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(ArArduinoParser.ID)
            self.state = 132
            self.match(ArArduinoParser.COLON)
            self.state = 133
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ArArduinoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ArArduinoParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArArduinoParser.StatementContext)
            else:
                return self.getTypedRuleContext(ArArduinoParser.StatementContext,i)


        def getRuleIndex(self):
            return ArArduinoParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ArArduinoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(ArArduinoParser.LBRACE)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 288269958570412054) != 0):
                self.state = 136
                self.statement()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.match(ArArduinoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(ArArduinoParser.VarDeclContext,0)


        def idStatement(self):
            return self.getTypedRuleContext(ArArduinoParser.IdStatementContext,0)


        def SEMI(self):
            return self.getToken(ArArduinoParser.SEMI, 0)

        def ifStat(self):
            return self.getTypedRuleContext(ArArduinoParser.IfStatContext,0)


        def whileStat(self):
            return self.getTypedRuleContext(ArArduinoParser.WhileStatContext,0)


        def returnStat(self):
            return self.getTypedRuleContext(ArArduinoParser.ReturnStatContext,0)


        def breakStat(self):
            return self.getTypedRuleContext(ArArduinoParser.BreakStatContext,0)


        def continueStat(self):
            return self.getTypedRuleContext(ArArduinoParser.ContinueStatContext,0)


        def block(self):
            return self.getTypedRuleContext(ArArduinoParser.BlockContext,0)


        def getRuleIndex(self):
            return ArArduinoParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ArArduinoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.varDecl()
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 2)
                self.state = 145
                self.idStatement()
                self.state = 146
                self.match(ArArduinoParser.SEMI)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.ifStat()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 149
                self.whileStat()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 150
                self.returnStat()
                self.state = 151
                self.match(ArArduinoParser.SEMI)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 6)
                self.state = 153
                self.breakStat()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 7)
                self.state = 154
                self.continueStat()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 8)
                self.state = 155
                self.block()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 9)
                self.state = 156
                self.match(ArArduinoParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ArArduinoParser.ID, 0)

        def idSuffix(self):
            return self.getTypedRuleContext(ArArduinoParser.IdSuffixContext,0)


        def getRuleIndex(self):
            return ArArduinoParser.RULE_idStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdStatement" ):
                listener.enterIdStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdStatement" ):
                listener.exitIdStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdStatement" ):
                return visitor.visitIdStatement(self)
            else:
                return visitor.visitChildren(self)




    def idStatement(self):

        localctx = ArArduinoParser.IdStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_idStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(ArArduinoParser.ID)
            self.state = 160
            self.idSuffix()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdSuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ArArduinoParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ArArduinoParser.ExpressionContext,0)


        def ADD_ASSIGN(self):
            return self.getToken(ArArduinoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(ArArduinoParser.SUB_ASSIGN, 0)

        def INC(self):
            return self.getToken(ArArduinoParser.INC, 0)

        def DEC(self):
            return self.getToken(ArArduinoParser.DEC, 0)

        def LPAREN(self):
            return self.getToken(ArArduinoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ArArduinoParser.RPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(ArArduinoParser.ArgsContext,0)


        def getRuleIndex(self):
            return ArArduinoParser.RULE_idSuffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdSuffix" ):
                listener.enterIdSuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdSuffix" ):
                listener.exitIdSuffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdSuffix" ):
                return visitor.visitIdSuffix(self)
            else:
                return visitor.visitChildren(self)




    def idSuffix(self):

        localctx = ArArduinoParser.IdSuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_idSuffix)
        self._la = 0 # Token type
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(ArArduinoParser.ASSIGN)
                self.state = 163
                self.expression()
                pass
            elif token in [26, 27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                _la = self._input.LA(1)
                if not(_la==26 or _la==27):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 165
                self.expression()
                pass
            elif token in [24, 25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 166
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 4)
                self.state = 167
                self.match(ArArduinoParser.LPAREN)
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 532552305206100064) != 0):
                    self.state = 168
                    self.args()


                self.state = 171
                self.match(ArArduinoParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ArArduinoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ArArduinoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ArArduinoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ArArduinoParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArArduinoParser.BlockContext)
            else:
                return self.getTypedRuleContext(ArArduinoParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(ArArduinoParser.ELSE, 0)

        def getRuleIndex(self):
            return ArArduinoParser.RULE_ifStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStat" ):
                listener.enterIfStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStat" ):
                listener.exitIfStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStat" ):
                return visitor.visitIfStat(self)
            else:
                return visitor.visitChildren(self)




    def ifStat(self):

        localctx = ArArduinoParser.IfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ifStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(ArArduinoParser.IF)
            self.state = 175
            self.match(ArArduinoParser.LPAREN)
            self.state = 176
            self.expression()
            self.state = 177
            self.match(ArArduinoParser.RPAREN)
            self.state = 178
            self.block()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 179
                self.match(ArArduinoParser.ELSE)
                self.state = 180
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ArArduinoParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(ArArduinoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ArArduinoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ArArduinoParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(ArArduinoParser.BlockContext,0)


        def getRuleIndex(self):
            return ArArduinoParser.RULE_whileStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStat" ):
                listener.enterWhileStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStat" ):
                listener.exitWhileStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStat" ):
                return visitor.visitWhileStat(self)
            else:
                return visitor.visitChildren(self)




    def whileStat(self):

        localctx = ArArduinoParser.WhileStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_whileStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(ArArduinoParser.WHILE)
            self.state = 184
            self.match(ArArduinoParser.LPAREN)
            self.state = 185
            self.expression()
            self.state = 186
            self.match(ArArduinoParser.RPAREN)
            self.state = 187
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ArArduinoParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(ArArduinoParser.SEMI, 0)

        def getRuleIndex(self):
            return ArArduinoParser.RULE_breakStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStat" ):
                listener.enterBreakStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStat" ):
                listener.exitBreakStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStat" ):
                return visitor.visitBreakStat(self)
            else:
                return visitor.visitChildren(self)




    def breakStat(self):

        localctx = ArArduinoParser.BreakStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_breakStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(ArArduinoParser.BREAK)
            self.state = 190
            self.match(ArArduinoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ArArduinoParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(ArArduinoParser.SEMI, 0)

        def getRuleIndex(self):
            return ArArduinoParser.RULE_continueStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStat" ):
                listener.enterContinueStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStat" ):
                listener.exitContinueStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStat" ):
                return visitor.visitContinueStat(self)
            else:
                return visitor.visitChildren(self)




    def continueStat(self):

        localctx = ArArduinoParser.ContinueStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_continueStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(ArArduinoParser.CONTINUE)
            self.state = 193
            self.match(ArArduinoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ArArduinoParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(ArArduinoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ArArduinoParser.RULE_returnStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStat" ):
                listener.enterReturnStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStat" ):
                listener.exitReturnStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStat" ):
                return visitor.visitReturnStat(self)
            else:
                return visitor.visitChildren(self)




    def returnStat(self):

        localctx = ArArduinoParser.ReturnStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_returnStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(ArArduinoParser.RETURN)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 532552305206100064) != 0):
                self.state = 196
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArArduinoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ArArduinoParser.ExpressionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ArArduinoParser.COMA)
            else:
                return self.getToken(ArArduinoParser.COMA, i)

        def getRuleIndex(self):
            return ArArduinoParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = ArArduinoParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.expression()
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 200
                self.match(ArArduinoParser.COMA)
                self.state = 201
                self.expression()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orExpr(self):
            return self.getTypedRuleContext(ArArduinoParser.OrExprContext,0)


        def getRuleIndex(self):
            return ArArduinoParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ArArduinoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.orExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArArduinoParser.AndExprContext)
            else:
                return self.getTypedRuleContext(ArArduinoParser.AndExprContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ArArduinoParser.OR)
            else:
                return self.getToken(ArArduinoParser.OR, i)

        def getRuleIndex(self):
            return ArArduinoParser.RULE_orExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def orExpr(self):

        localctx = ArArduinoParser.OrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_orExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.andExpr()
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 210
                self.match(ArArduinoParser.OR)
                self.state = 211
                self.andExpr()
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bwOrExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArArduinoParser.BwOrExprContext)
            else:
                return self.getTypedRuleContext(ArArduinoParser.BwOrExprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ArArduinoParser.AND)
            else:
                return self.getToken(ArArduinoParser.AND, i)

        def getRuleIndex(self):
            return ArArduinoParser.RULE_andExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def andExpr(self):

        localctx = ArArduinoParser.AndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_andExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.bwOrExpr()
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 218
                self.match(ArArduinoParser.AND)
                self.state = 219
                self.bwOrExpr()
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BwOrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bwXorExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArArduinoParser.BwXorExprContext)
            else:
                return self.getTypedRuleContext(ArArduinoParser.BwXorExprContext,i)


        def BW_OR(self, i:int=None):
            if i is None:
                return self.getTokens(ArArduinoParser.BW_OR)
            else:
                return self.getToken(ArArduinoParser.BW_OR, i)

        def getRuleIndex(self):
            return ArArduinoParser.RULE_bwOrExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBwOrExpr" ):
                listener.enterBwOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBwOrExpr" ):
                listener.exitBwOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBwOrExpr" ):
                return visitor.visitBwOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def bwOrExpr(self):

        localctx = ArArduinoParser.BwOrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_bwOrExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.bwXorExpr()
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 226
                self.match(ArArduinoParser.BW_OR)
                self.state = 227
                self.bwXorExpr()
                self.state = 232
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BwXorExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bwAndExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArArduinoParser.BwAndExprContext)
            else:
                return self.getTypedRuleContext(ArArduinoParser.BwAndExprContext,i)


        def BW_XOR(self, i:int=None):
            if i is None:
                return self.getTokens(ArArduinoParser.BW_XOR)
            else:
                return self.getToken(ArArduinoParser.BW_XOR, i)

        def getRuleIndex(self):
            return ArArduinoParser.RULE_bwXorExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBwXorExpr" ):
                listener.enterBwXorExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBwXorExpr" ):
                listener.exitBwXorExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBwXorExpr" ):
                return visitor.visitBwXorExpr(self)
            else:
                return visitor.visitChildren(self)




    def bwXorExpr(self):

        localctx = ArArduinoParser.BwXorExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_bwXorExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.bwAndExpr()
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==49:
                self.state = 234
                self.match(ArArduinoParser.BW_XOR)
                self.state = 235
                self.bwAndExpr()
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BwAndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArArduinoParser.RelExprContext)
            else:
                return self.getTypedRuleContext(ArArduinoParser.RelExprContext,i)


        def BW_AND(self, i:int=None):
            if i is None:
                return self.getTokens(ArArduinoParser.BW_AND)
            else:
                return self.getToken(ArArduinoParser.BW_AND, i)

        def getRuleIndex(self):
            return ArArduinoParser.RULE_bwAndExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBwAndExpr" ):
                listener.enterBwAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBwAndExpr" ):
                listener.exitBwAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBwAndExpr" ):
                return visitor.visitBwAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def bwAndExpr(self):

        localctx = ArArduinoParser.BwAndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_bwAndExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.relExpr()
            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 242
                self.match(ArArduinoParser.BW_AND)
                self.state = 243
                self.relExpr()
                self.state = 248
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def shiftExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArArduinoParser.ShiftExprContext)
            else:
                return self.getTypedRuleContext(ArArduinoParser.ShiftExprContext,i)


        def relOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArArduinoParser.RelOpContext)
            else:
                return self.getTypedRuleContext(ArArduinoParser.RelOpContext,i)


        def getRuleIndex(self):
            return ArArduinoParser.RULE_relExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelExpr" ):
                listener.enterRelExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelExpr" ):
                listener.exitRelExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)




    def relExpr(self):

        localctx = ArArduinoParser.RelExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_relExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.shiftExpr()
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 135291469824) != 0):
                self.state = 250
                self.relOp()
                self.state = 251
                self.shiftExpr()
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(ArArduinoParser.GT, 0)

        def LT(self):
            return self.getToken(ArArduinoParser.LT, 0)

        def LTE(self):
            return self.getToken(ArArduinoParser.LTE, 0)

        def GTE(self):
            return self.getToken(ArArduinoParser.GTE, 0)

        def EQ(self):
            return self.getToken(ArArduinoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(ArArduinoParser.NEQ, 0)

        def getRuleIndex(self):
            return ArArduinoParser.RULE_relOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelOp" ):
                listener.enterRelOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelOp" ):
                listener.exitRelOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelOp" ):
                return visitor.visitRelOp(self)
            else:
                return visitor.visitChildren(self)




    def relOp(self):

        localctx = ArArduinoParser.RelOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_relOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 135291469824) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShiftExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArArduinoParser.AddExprContext)
            else:
                return self.getTypedRuleContext(ArArduinoParser.AddExprContext,i)


        def SHL(self, i:int=None):
            if i is None:
                return self.getTokens(ArArduinoParser.SHL)
            else:
                return self.getToken(ArArduinoParser.SHL, i)

        def SHR(self, i:int=None):
            if i is None:
                return self.getTokens(ArArduinoParser.SHR)
            else:
                return self.getToken(ArArduinoParser.SHR, i)

        def getRuleIndex(self):
            return ArArduinoParser.RULE_shiftExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShiftExpr" ):
                listener.enterShiftExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShiftExpr" ):
                listener.exitShiftExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShiftExpr" ):
                return visitor.visitShiftExpr(self)
            else:
                return visitor.visitChildren(self)




    def shiftExpr(self):

        localctx = ArArduinoParser.ShiftExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_shiftExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.addExpr()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29 or _la==30:
                self.state = 261
                _la = self._input.LA(1)
                if not(_la==29 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 262
                self.addExpr()
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mulExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArArduinoParser.MulExprContext)
            else:
                return self.getTypedRuleContext(ArArduinoParser.MulExprContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(ArArduinoParser.PLUS)
            else:
                return self.getToken(ArArduinoParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(ArArduinoParser.MINUS)
            else:
                return self.getToken(ArArduinoParser.MINUS, i)

        def getRuleIndex(self):
            return ArArduinoParser.RULE_addExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)




    def addExpr(self):

        localctx = ArArduinoParser.AddExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_addExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.mulExpr()
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20 or _la==21:
                self.state = 269
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 270
                self.mulExpr()
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArArduinoParser.UnaryExprContext)
            else:
                return self.getTypedRuleContext(ArArduinoParser.UnaryExprContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(ArArduinoParser.MUL)
            else:
                return self.getToken(ArArduinoParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(ArArduinoParser.DIV)
            else:
                return self.getToken(ArArduinoParser.DIV, i)

        def getRuleIndex(self):
            return ArArduinoParser.RULE_mulExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)




    def mulExpr(self):

        localctx = ArArduinoParser.MulExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_mulExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.unaryExpr()
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==23:
                self.state = 277
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 278
                self.unaryExpr()
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self):
            return self.getTypedRuleContext(ArArduinoParser.UnaryExprContext,0)


        def MINUS(self):
            return self.getToken(ArArduinoParser.MINUS, 0)

        def NOT(self):
            return self.getToken(ArArduinoParser.NOT, 0)

        def BW_NOT(self):
            return self.getToken(ArArduinoParser.BW_NOT, 0)

        def primary(self):
            return self.getTypedRuleContext(ArArduinoParser.PrimaryContext,0)


        def getRuleIndex(self):
            return ArArduinoParser.RULE_unaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = ArArduinoParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 39, 50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1126449664753664) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 285
                self.unaryExpr()
                pass
            elif token in [5, 6, 40, 53, 54, 56, 57, 58]:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ArArduinoParser.NUMBER, 0)

        def BIN_NUMBER(self):
            return self.getToken(ArArduinoParser.BIN_NUMBER, 0)

        def TRUE(self):
            return self.getToken(ArArduinoParser.TRUE, 0)

        def CHAR(self):
            return self.getToken(ArArduinoParser.CHAR, 0)

        def STRING(self):
            return self.getToken(ArArduinoParser.STRING, 0)

        def FALSE(self):
            return self.getToken(ArArduinoParser.FALSE, 0)

        def LPAREN(self):
            return self.getToken(ArArduinoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ArArduinoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ArArduinoParser.RPAREN, 0)

        def ID(self):
            return self.getToken(ArArduinoParser.ID, 0)

        def primaryIdSuffix(self):
            return self.getTypedRuleContext(ArArduinoParser.PrimaryIdSuffixContext,0)


        def getRuleIndex(self):
            return ArArduinoParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = ArArduinoParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_primary)
        try:
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.match(ArArduinoParser.NUMBER)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 290
                self.match(ArArduinoParser.BIN_NUMBER)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 291
                self.match(ArArduinoParser.TRUE)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 4)
                self.state = 292
                self.match(ArArduinoParser.CHAR)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 5)
                self.state = 293
                self.match(ArArduinoParser.STRING)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 6)
                self.state = 294
                self.match(ArArduinoParser.FALSE)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 7)
                self.state = 295
                self.match(ArArduinoParser.LPAREN)
                self.state = 296
                self.expression()
                self.state = 297
                self.match(ArArduinoParser.RPAREN)
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 8)
                self.state = 299
                self.match(ArArduinoParser.ID)
                self.state = 300
                self.primaryIdSuffix()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryIdSuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ArArduinoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ArArduinoParser.RPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(ArArduinoParser.ArgsContext,0)


        def getRuleIndex(self):
            return ArArduinoParser.RULE_primaryIdSuffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryIdSuffix" ):
                listener.enterPrimaryIdSuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryIdSuffix" ):
                listener.exitPrimaryIdSuffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryIdSuffix" ):
                return visitor.visitPrimaryIdSuffix(self)
            else:
                return visitor.visitChildren(self)




    def primaryIdSuffix(self):

        localctx = ArArduinoParser.PrimaryIdSuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_primaryIdSuffix)
        self._la = 0 # Token type
        try:
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(ArArduinoParser.LPAREN)
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 532552305206100064) != 0):
                    self.state = 304
                    self.args()


                self.state = 307
                self.match(ArArduinoParser.RPAREN)
                pass
            elif token in [20, 21, 22, 23, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 41, 45, 46, 47, 48, 49]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_T(self):
            return self.getToken(ArArduinoParser.INT_T, 0)

        def FLOAT_T(self):
            return self.getToken(ArArduinoParser.FLOAT_T, 0)

        def VOID(self):
            return self.getToken(ArArduinoParser.VOID, 0)

        def BOOL(self):
            return self.getToken(ArArduinoParser.BOOL, 0)

        def STRING_T(self):
            return self.getToken(ArArduinoParser.STRING_T, 0)

        def CHAR_T(self):
            return self.getToken(ArArduinoParser.CHAR_T, 0)

        def getRuleIndex(self):
            return ArArduinoParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = ArArduinoParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6755399441073024) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





