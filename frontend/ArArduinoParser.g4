parser grammar ArArduinoParser;

options {
    tokenVocab = ArArduinoLexer;
}

// نقطة البداية
program : importStmt* declaration* EOF ;

// قاعدة الاستيراد
importStmt : IMPORT STRING SEMI ;

// التعريف إما لمتغير أو دالة
declaration 
    : varDecl 
    | funDecl 
    ;

// تعريف المتغير
varDecl : VAR ID COLON type ASSIGN expression SEMI ;

// --- Left Factoring for Functions ---
funDecl : FUNCTION funcBody ;

funcBody
    : SETUP LPAREN RPAREN COLON VOID block
    | LOOP LPAREN RPAREN COLON VOID block
    | ID LPAREN params? RPAREN COLON type block
    ;

params : param (COMA param)* ;
param : ID COLON type ;
block : LBRACE statement* RBRACE ;

// --- Left Factoring for Statements ---
statement
    : varDecl
    | idStatement SEMI
    | ifStat
    | whileStat
    | returnStat SEMI
    | breakStat       
    | continueStat  
    | block
    | SEMI
    ;

// الجمل التي تبدأ بـ ID (إما إسناد أو استدعاء دالة)
idStatement : ID idSuffix ;

idSuffix
    : ASSIGN expression                     // س = 5؛
    | (ADD_ASSIGN | SUB_ASSIGN) expression   // س += 5؛
    | (INC | DEC)                           // س++؛
    | LPAREN args? RPAREN                   // دالة()؛
    ;

ifStat : IF LPAREN expression RPAREN block (ELSE block)? ;
whileStat : WHILE LPAREN expression RPAREN block ;
breakStat : BREAK SEMI ;
continueStat : CONTINUE SEMI ;
returnStat : RETURN expression? ;

args : expression (COMA expression)* ;

// ==========================================
// --- Eliminating Left Recursion (LL1) ---
// ==========================================

expression : orExpr ;

// 1. "أو" المنطقية
orExpr : andExpr (OR andExpr)* ;

// 2. "و" المنطقية
andExpr : bwOrExpr (AND bwOrExpr)* ;

// 3. Bitwise OR
bwOrExpr : bwXorExpr (BW_OR bwXorExpr)* ;

// 4. Bitwise XOR
bwXorExpr : bwAndExpr (BW_XOR bwAndExpr)* ;

// 5. Bitwise AND
bwAndExpr : relExpr (BW_AND relExpr)* ;

// 6. المقارنات النسبية والمتساوية تليها الإزاحة
relExpr : shiftExpr (relOp shiftExpr)* ;

// معاملات المقارنة
relOp :  GT | LT | LTE | GTE | EQ | NEQ ; 

// 7. عوامل الإزاحة الثنائية (<< >>) تليها الجمع والطرح
shiftExpr : addExpr ((SHL | SHR) addExpr)* ;

addExpr : mulExpr ((PLUS | MINUS) mulExpr)* ;

mulExpr : unaryExpr ((MUL | DIV) unaryExpr)* ;

// المعاملات الأحادية تشمل النفي الثنائي (BW_NOT) والنفي المنطقي (NOT)
unaryExpr 
    : (MINUS | NOT | BW_NOT) unaryExpr 
    | primary 
    ;

// --- Left Factoring for Primary ---
primary
    : NUMBER
    | BIN_NUMBER
    | TRUE
    | CHAR
    | STRING
    | FALSE
    | LPAREN expression RPAREN
    | ID primaryIdSuffix  // المعرف قد يكون متغيراً أو استدعاء دالة
    ;

primaryIdSuffix
    : LPAREN args? RPAREN  // استدعاء دالة
    | /* Epsilon (فارغ) */ // مجرد متغير عادي
    ;

// الأنواع
type : INT_T | FLOAT_T | VOID | BOOL | STRING_T | CHAR_T;
