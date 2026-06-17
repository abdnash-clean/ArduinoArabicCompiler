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
        4,1,58,303,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,5,0,66,8,0,
        10,0,12,0,69,9,0,1,0,5,0,72,8,0,10,0,12,0,75,9,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,2,1,2,3,2,85,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,
        4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,3,5,113,8,5,1,5,1,5,1,5,1,5,1,5,3,5,120,8,5,1,6,1,6,1,6,5,6,125,
        8,6,10,6,12,6,128,9,6,1,7,1,7,1,7,1,7,1,8,1,8,5,8,136,8,8,10,8,12,
        8,139,9,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,3,9,156,8,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,3,11,168,8,11,1,11,3,11,171,8,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,3,12,180,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,
        1,15,1,15,1,15,1,16,1,16,3,16,196,8,16,1,17,1,17,1,17,5,17,201,8,
        17,10,17,12,17,204,9,17,1,18,1,18,1,19,1,19,1,19,5,19,211,8,19,10,
        19,12,19,214,9,19,1,20,1,20,1,20,5,20,219,8,20,10,20,12,20,222,9,
        20,1,21,1,21,1,21,5,21,227,8,21,10,21,12,21,230,9,21,1,22,1,22,1,
        22,5,22,235,8,22,10,22,12,22,238,9,22,1,23,1,23,1,23,5,23,243,8,
        23,10,23,12,23,246,9,23,1,24,1,24,1,24,1,24,5,24,252,8,24,10,24,
        12,24,255,9,24,1,25,1,25,1,26,1,26,1,26,5,26,262,8,26,10,26,12,26,
        265,9,26,1,27,1,27,1,27,5,27,270,8,27,10,27,12,27,273,9,27,1,28,
        1,28,1,28,3,28,278,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,
        1,29,1,29,1,29,3,29,291,8,29,1,30,1,30,3,30,295,8,30,1,30,1,30,3,
        30,299,8,30,1,31,1,31,1,31,0,0,32,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,0,7,
        1,0,26,27,1,0,24,25,1,0,29,34,1,0,20,21,1,0,22,23,3,0,21,21,37,37,
        48,48,3,0,7,9,14,14,49,50,310,0,67,1,0,0,0,2,78,1,0,0,0,4,84,1,0,
        0,0,6,86,1,0,0,0,8,94,1,0,0,0,10,119,1,0,0,0,12,121,1,0,0,0,14,129,
        1,0,0,0,16,133,1,0,0,0,18,155,1,0,0,0,20,157,1,0,0,0,22,170,1,0,
        0,0,24,172,1,0,0,0,26,181,1,0,0,0,28,187,1,0,0,0,30,190,1,0,0,0,
        32,193,1,0,0,0,34,197,1,0,0,0,36,205,1,0,0,0,38,207,1,0,0,0,40,215,
        1,0,0,0,42,223,1,0,0,0,44,231,1,0,0,0,46,239,1,0,0,0,48,247,1,0,
        0,0,50,256,1,0,0,0,52,258,1,0,0,0,54,266,1,0,0,0,56,277,1,0,0,0,
        58,290,1,0,0,0,60,298,1,0,0,0,62,300,1,0,0,0,64,66,3,2,1,0,65,64,
        1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,73,1,0,0,0,
        69,67,1,0,0,0,70,72,3,4,2,0,71,70,1,0,0,0,72,75,1,0,0,0,73,71,1,
        0,0,0,73,74,1,0,0,0,74,76,1,0,0,0,75,73,1,0,0,0,76,77,5,0,0,1,77,
        1,1,0,0,0,78,79,5,53,0,0,79,80,5,51,0,0,80,81,5,43,0,0,81,3,1,0,
        0,0,82,85,3,6,3,0,83,85,3,8,4,0,84,82,1,0,0,0,84,83,1,0,0,0,85,5,
        1,0,0,0,86,87,5,1,0,0,87,88,5,55,0,0,88,89,5,42,0,0,89,90,3,62,31,
        0,90,91,5,19,0,0,91,92,3,36,18,0,92,93,5,43,0,0,93,7,1,0,0,0,94,
        95,5,10,0,0,95,96,3,10,5,0,96,9,1,0,0,0,97,98,5,12,0,0,98,99,5,38,
        0,0,99,100,5,39,0,0,100,101,5,42,0,0,101,102,5,9,0,0,102,120,3,16,
        8,0,103,104,5,13,0,0,104,105,5,38,0,0,105,106,5,39,0,0,106,107,5,
        42,0,0,107,108,5,9,0,0,108,120,3,16,8,0,109,110,5,55,0,0,110,112,
        5,38,0,0,111,113,3,12,6,0,112,111,1,0,0,0,112,113,1,0,0,0,113,114,
        1,0,0,0,114,115,5,39,0,0,115,116,5,42,0,0,116,117,3,62,31,0,117,
        118,3,16,8,0,118,120,1,0,0,0,119,97,1,0,0,0,119,103,1,0,0,0,119,
        109,1,0,0,0,120,11,1,0,0,0,121,126,3,14,7,0,122,123,5,44,0,0,123,
        125,3,14,7,0,124,122,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,
        127,1,0,0,0,127,13,1,0,0,0,128,126,1,0,0,0,129,130,5,55,0,0,130,
        131,5,42,0,0,131,132,3,62,31,0,132,15,1,0,0,0,133,137,5,40,0,0,134,
        136,3,18,9,0,135,134,1,0,0,0,136,139,1,0,0,0,137,135,1,0,0,0,137,
        138,1,0,0,0,138,140,1,0,0,0,139,137,1,0,0,0,140,141,5,41,0,0,141,
        17,1,0,0,0,142,156,3,6,3,0,143,144,3,20,10,0,144,145,5,43,0,0,145,
        156,1,0,0,0,146,156,3,24,12,0,147,156,3,26,13,0,148,149,3,32,16,
        0,149,150,5,43,0,0,150,156,1,0,0,0,151,156,3,28,14,0,152,156,3,30,
        15,0,153,156,3,16,8,0,154,156,5,43,0,0,155,142,1,0,0,0,155,143,1,
        0,0,0,155,146,1,0,0,0,155,147,1,0,0,0,155,148,1,0,0,0,155,151,1,
        0,0,0,155,152,1,0,0,0,155,153,1,0,0,0,155,154,1,0,0,0,156,19,1,0,
        0,0,157,158,5,55,0,0,158,159,3,22,11,0,159,21,1,0,0,0,160,161,5,
        19,0,0,161,171,3,36,18,0,162,163,7,0,0,0,163,171,3,36,18,0,164,171,
        7,1,0,0,165,167,5,38,0,0,166,168,3,34,17,0,167,166,1,0,0,0,167,168,
        1,0,0,0,168,169,1,0,0,0,169,171,5,39,0,0,170,160,1,0,0,0,170,162,
        1,0,0,0,170,164,1,0,0,0,170,165,1,0,0,0,171,23,1,0,0,0,172,173,5,
        2,0,0,173,174,5,38,0,0,174,175,3,36,18,0,175,176,5,39,0,0,176,179,
        3,16,8,0,177,178,5,3,0,0,178,180,3,16,8,0,179,177,1,0,0,0,179,180,
        1,0,0,0,180,25,1,0,0,0,181,182,5,4,0,0,182,183,5,38,0,0,183,184,
        3,36,18,0,184,185,5,39,0,0,185,186,3,16,8,0,186,27,1,0,0,0,187,188,
        5,15,0,0,188,189,5,43,0,0,189,29,1,0,0,0,190,191,5,16,0,0,191,192,
        5,43,0,0,192,31,1,0,0,0,193,195,5,11,0,0,194,196,3,36,18,0,195,194,
        1,0,0,0,195,196,1,0,0,0,196,33,1,0,0,0,197,202,3,36,18,0,198,199,
        5,44,0,0,199,201,3,36,18,0,200,198,1,0,0,0,201,204,1,0,0,0,202,200,
        1,0,0,0,202,203,1,0,0,0,203,35,1,0,0,0,204,202,1,0,0,0,205,206,3,
        38,19,0,206,37,1,0,0,0,207,212,3,40,20,0,208,209,5,35,0,0,209,211,
        3,40,20,0,210,208,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,213,
        1,0,0,0,213,39,1,0,0,0,214,212,1,0,0,0,215,220,3,42,21,0,216,217,
        5,36,0,0,217,219,3,42,21,0,218,216,1,0,0,0,219,222,1,0,0,0,220,218,
        1,0,0,0,220,221,1,0,0,0,221,41,1,0,0,0,222,220,1,0,0,0,223,228,3,
        44,22,0,224,225,5,45,0,0,225,227,3,44,22,0,226,224,1,0,0,0,227,230,
        1,0,0,0,228,226,1,0,0,0,228,229,1,0,0,0,229,43,1,0,0,0,230,228,1,
        0,0,0,231,236,3,46,23,0,232,233,5,47,0,0,233,235,3,46,23,0,234,232,
        1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,45,1,
        0,0,0,238,236,1,0,0,0,239,244,3,48,24,0,240,241,5,46,0,0,241,243,
        3,48,24,0,242,240,1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,245,
        1,0,0,0,245,47,1,0,0,0,246,244,1,0,0,0,247,253,3,52,26,0,248,249,
        3,50,25,0,249,250,3,52,26,0,250,252,1,0,0,0,251,248,1,0,0,0,252,
        255,1,0,0,0,253,251,1,0,0,0,253,254,1,0,0,0,254,49,1,0,0,0,255,253,
        1,0,0,0,256,257,7,2,0,0,257,51,1,0,0,0,258,263,3,54,27,0,259,260,
        7,3,0,0,260,262,3,54,27,0,261,259,1,0,0,0,262,265,1,0,0,0,263,261,
        1,0,0,0,263,264,1,0,0,0,264,53,1,0,0,0,265,263,1,0,0,0,266,271,3,
        56,28,0,267,268,7,4,0,0,268,270,3,56,28,0,269,267,1,0,0,0,270,273,
        1,0,0,0,271,269,1,0,0,0,271,272,1,0,0,0,272,55,1,0,0,0,273,271,1,
        0,0,0,274,275,7,5,0,0,275,278,3,56,28,0,276,278,3,58,29,0,277,274,
        1,0,0,0,277,276,1,0,0,0,278,57,1,0,0,0,279,291,5,54,0,0,280,291,
        5,5,0,0,281,291,5,52,0,0,282,291,5,51,0,0,283,291,5,6,0,0,284,285,
        5,38,0,0,285,286,3,36,18,0,286,287,5,39,0,0,287,291,1,0,0,0,288,
        289,5,55,0,0,289,291,3,60,30,0,290,279,1,0,0,0,290,280,1,0,0,0,290,
        281,1,0,0,0,290,282,1,0,0,0,290,283,1,0,0,0,290,284,1,0,0,0,290,
        288,1,0,0,0,291,59,1,0,0,0,292,294,5,38,0,0,293,295,3,34,17,0,294,
        293,1,0,0,0,294,295,1,0,0,0,295,296,1,0,0,0,296,299,5,39,0,0,297,
        299,1,0,0,0,298,292,1,0,0,0,298,297,1,0,0,0,299,61,1,0,0,0,300,301,
        7,6,0,0,301,63,1,0,0,0,25,67,73,84,112,119,126,137,155,167,170,179,
        195,202,212,220,228,236,244,253,263,271,277,290,294,298
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
                     "'+='", "'-='", "'%'", "'>='", "'<='", "'=='", "'!='", 
                     "'>'", "'<'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "':'", "'\\u061B'", "'\\u060C'", 
                     "'|'", "'&'", "'^'", "'~'", "'\\u0646\\u0635'", "'\\u062D\\u0631\\u0641'" ]

    symbolicNames = [ "<INVALID>", "VAR", "IF", "ELSE", "WHILE", "TRUE", 
                      "FALSE", "INT_T", "FLOAT_T", "VOID", "FUNCTION", "RETURN", 
                      "SETUP", "LOOP", "BOOL", "BREAK", "CONTINUE", "DO", 
                      "PRINT", "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", 
                      "INC", "DEC", "ADD_ASSIGN", "SUB_ASSIGN", "MOD", "GTE", 
                      "LTE", "EQ", "NEQ", "GT", "LT", "OR", "AND", "NOT", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "COLON", "SEMI", 
                      "COMA", "BW_OR", "BW_AND", "BW_XOR", "BW_NOT", "STRING_T", 
                      "CHAR_T", "STRING", "CHAR", "IMPORT", "NUMBER", "ID", 
                      "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

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
    RULE_addExpr = 26
    RULE_mulExpr = 27
    RULE_unaryExpr = 28
    RULE_primary = 29
    RULE_primaryIdSuffix = 30
    RULE_type = 31

    ruleNames =  [ "program", "importStmt", "declaration", "varDecl", "funDecl", 
                   "funcBody", "params", "param", "block", "statement", 
                   "idStatement", "idSuffix", "ifStat", "whileStat", "breakStat", 
                   "continueStat", "returnStat", "args", "expression", "orExpr", 
                   "andExpr", "bwOrExpr", "bwXorExpr", "bwAndExpr", "relExpr", 
                   "relOp", "addExpr", "mulExpr", "unaryExpr", "primary", 
                   "primaryIdSuffix", "type" ]

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
    GTE=29
    LTE=30
    EQ=31
    NEQ=32
    GT=33
    LT=34
    OR=35
    AND=36
    NOT=37
    LPAREN=38
    RPAREN=39
    LBRACE=40
    RBRACE=41
    COLON=42
    SEMI=43
    COMA=44
    BW_OR=45
    BW_AND=46
    BW_XOR=47
    BW_NOT=48
    STRING_T=49
    CHAR_T=50
    STRING=51
    CHAR=52
    IMPORT=53
    NUMBER=54
    ID=55
    WS=56
    LINE_COMMENT=57
    BLOCK_COMMENT=58

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
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 64
                self.importStmt()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==10:
                self.state = 70
                self.declaration()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
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
            self.state = 78
            self.match(ArArduinoParser.IMPORT)
            self.state = 79
            self.match(ArArduinoParser.STRING)
            self.state = 80
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
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.varDecl()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
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
            self.state = 86
            self.match(ArArduinoParser.VAR)
            self.state = 87
            self.match(ArArduinoParser.ID)
            self.state = 88
            self.match(ArArduinoParser.COLON)
            self.state = 89
            self.type_()
            self.state = 90
            self.match(ArArduinoParser.ASSIGN)
            self.state = 91
            self.expression()
            self.state = 92
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
            self.state = 94
            self.match(ArArduinoParser.FUNCTION)
            self.state = 95
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
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.match(ArArduinoParser.SETUP)
                self.state = 98
                self.match(ArArduinoParser.LPAREN)
                self.state = 99
                self.match(ArArduinoParser.RPAREN)
                self.state = 100
                self.match(ArArduinoParser.COLON)
                self.state = 101
                self.match(ArArduinoParser.VOID)
                self.state = 102
                self.block()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.match(ArArduinoParser.LOOP)
                self.state = 104
                self.match(ArArduinoParser.LPAREN)
                self.state = 105
                self.match(ArArduinoParser.RPAREN)
                self.state = 106
                self.match(ArArduinoParser.COLON)
                self.state = 107
                self.match(ArArduinoParser.VOID)
                self.state = 108
                self.block()
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 3)
                self.state = 109
                self.match(ArArduinoParser.ID)
                self.state = 110
                self.match(ArArduinoParser.LPAREN)
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==55:
                    self.state = 111
                    self.params()


                self.state = 114
                self.match(ArArduinoParser.RPAREN)
                self.state = 115
                self.match(ArArduinoParser.COLON)
                self.state = 116
                self.type_()
                self.state = 117
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
            self.state = 121
            self.param()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 122
                self.match(ArArduinoParser.COMA)
                self.state = 123
                self.param()
                self.state = 128
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
            self.state = 129
            self.match(ArArduinoParser.ID)
            self.state = 130
            self.match(ArArduinoParser.COLON)
            self.state = 131
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
            self.state = 133
            self.match(ArArduinoParser.LBRACE)
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 36038692623714326) != 0):
                self.state = 134
                self.statement()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
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
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.varDecl()
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.idStatement()
                self.state = 144
                self.match(ArArduinoParser.SEMI)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 146
                self.ifStat()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 147
                self.whileStat()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 148
                self.returnStat()
                self.state = 149
                self.match(ArArduinoParser.SEMI)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 6)
                self.state = 151
                self.breakStat()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 7)
                self.state = 152
                self.continueStat()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 8)
                self.state = 153
                self.block()
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 9)
                self.state = 154
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
            self.state = 157
            self.match(ArArduinoParser.ID)
            self.state = 158
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
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(ArArduinoParser.ASSIGN)
                self.state = 161
                self.expression()
                pass
            elif token in [26, 27]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                _la = self._input.LA(1)
                if not(_la==26 or _la==27):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 163
                self.expression()
                pass
            elif token in [24, 25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 4)
                self.state = 165
                self.match(ArArduinoParser.LPAREN)
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 61080482265170016) != 0):
                    self.state = 166
                    self.args()


                self.state = 169
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
            self.state = 172
            self.match(ArArduinoParser.IF)
            self.state = 173
            self.match(ArArduinoParser.LPAREN)
            self.state = 174
            self.expression()
            self.state = 175
            self.match(ArArduinoParser.RPAREN)
            self.state = 176
            self.block()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 177
                self.match(ArArduinoParser.ELSE)
                self.state = 178
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
            self.state = 181
            self.match(ArArduinoParser.WHILE)
            self.state = 182
            self.match(ArArduinoParser.LPAREN)
            self.state = 183
            self.expression()
            self.state = 184
            self.match(ArArduinoParser.RPAREN)
            self.state = 185
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
            self.state = 187
            self.match(ArArduinoParser.BREAK)
            self.state = 188
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
            self.state = 190
            self.match(ArArduinoParser.CONTINUE)
            self.state = 191
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
            self.state = 193
            self.match(ArArduinoParser.RETURN)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 61080482265170016) != 0):
                self.state = 194
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
            self.state = 197
            self.expression()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 198
                self.match(ArArduinoParser.COMA)
                self.state = 199
                self.expression()
                self.state = 204
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
            self.state = 205
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
            self.state = 207
            self.andExpr()
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 208
                self.match(ArArduinoParser.OR)
                self.state = 209
                self.andExpr()
                self.state = 214
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
            self.state = 215
            self.bwOrExpr()
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 216
                self.match(ArArduinoParser.AND)
                self.state = 217
                self.bwOrExpr()
                self.state = 222
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
            self.state = 223
            self.bwXorExpr()
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 224
                self.match(ArArduinoParser.BW_OR)
                self.state = 225
                self.bwXorExpr()
                self.state = 230
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
            self.state = 231
            self.bwAndExpr()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 232
                self.match(ArArduinoParser.BW_XOR)
                self.state = 233
                self.bwAndExpr()
                self.state = 238
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
            self.state = 239
            self.relExpr()
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 240
                self.match(ArArduinoParser.BW_AND)
                self.state = 241
                self.relExpr()
                self.state = 246
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

        def addExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArArduinoParser.AddExprContext)
            else:
                return self.getTypedRuleContext(ArArduinoParser.AddExprContext,i)


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
            self.state = 247
            self.addExpr()
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33822867456) != 0):
                self.state = 248
                self.relOp()
                self.state = 249
                self.addExpr()
                self.state = 255
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
            self.state = 256
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33822867456) != 0)):
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
        self.enterRule(localctx, 52, self.RULE_addExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.mulExpr()
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20 or _la==21:
                self.state = 259
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 260
                self.mulExpr()
                self.state = 265
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
        self.enterRule(localctx, 54, self.RULE_mulExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.unaryExpr()
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==23:
                self.state = 267
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 268
                self.unaryExpr()
                self.state = 273
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
        self.enterRule(localctx, 56, self.RULE_unaryExpr)
        self._la = 0 # Token type
        try:
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 37, 48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 281612417761280) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 275
                self.unaryExpr()
                pass
            elif token in [5, 6, 38, 51, 52, 54, 55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
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
        self.enterRule(localctx, 58, self.RULE_primary)
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [54]:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.match(ArArduinoParser.NUMBER)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.match(ArArduinoParser.TRUE)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 3)
                self.state = 281
                self.match(ArArduinoParser.CHAR)
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 4)
                self.state = 282
                self.match(ArArduinoParser.STRING)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 283
                self.match(ArArduinoParser.FALSE)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 6)
                self.state = 284
                self.match(ArArduinoParser.LPAREN)
                self.state = 285
                self.expression()
                self.state = 286
                self.match(ArArduinoParser.RPAREN)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 7)
                self.state = 288
                self.match(ArArduinoParser.ID)
                self.state = 289
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
        self.enterRule(localctx, 60, self.RULE_primaryIdSuffix)
        self._la = 0 # Token type
        try:
            self.state = 298
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(ArArduinoParser.LPAREN)
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 61080482265170016) != 0):
                    self.state = 293
                    self.args()


                self.state = 296
                self.match(ArArduinoParser.RPAREN)
                pass
            elif token in [20, 21, 22, 23, 29, 30, 31, 32, 33, 34, 35, 36, 39, 43, 44, 45, 46, 47]:
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
        self.enterRule(localctx, 62, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1688849860281216) != 0)):
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





