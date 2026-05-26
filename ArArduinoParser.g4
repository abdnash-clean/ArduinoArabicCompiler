parser grammar ArArduinoParser;

options {
    tokenVocab = ArArduinoLexer;
}

// نقطة البداية
program : declaration* EOF ;

// التعريف إما لمتغير (يبدأ بـ VAR) أو دالة (تبدأ بـ FUNCTION)
declaration 
    : varDecl 
    | funDecl 
    ;

// تعريف المتغير
varDecl : VAR ID COLON type ASSIGN expression SEMI ;

// --- Left Factoring for Functions ---
// أخذنا كلمة "دالة" كعامل مشترك أيسر لمنع التداخل
funDecl : FUNCTION funcBody ;

// ما بعد كلمة "دالة" يحدد نوعها (إعداد، تكرار، أو دالة عادية)
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
    | idStatement SEMI    // الإسناد أو الاستدعاء يبدأ بمعرف
    | ifStat
    | whileStat
    | returnStat SEMI
    ;

// الجمل التي تبدأ بـ ID (إما إسناد أو استدعاء دالة)
idStatement : ID idSuffix ;

idSuffix
    : ASSIGN expression     // إذا وجدنا (=) فهي عملية إسناد
    | LPAREN args? RPAREN   // إذا وجدنا أقواس فهي استدعاء دالة
    ;

ifStat : IF LPAREN expression RPAREN block (ELSE block)? ;
whileStat : WHILE LPAREN expression RPAREN block ;
returnStat : RETURN expression? ;

args : expression (COMA expression)* ;

// ==========================================
// --- Eliminating Left Recursion (LL1) ---
// ==========================================
// بنينا التعابير على شكل هرمي يمثل أولويات العمليات 
// من الأضعف (OR) إلى الأقوى (Primary)
// استخدمنا ()* بدلاً من الاستدعاء الذاتي الأيسر

expression : orExpr ;

orExpr : andExpr (OR andExpr)* ;

andExpr : relExpr (AND relExpr)* ;

relExpr : addExpr (relOp addExpr)* ;

// معاملات المقارنة 
relOp :  GT | LT | LTE | GTE | EQ | NEQ ; 

addExpr : mulExpr ((PLUS | MINUS) mulExpr)* ;

mulExpr : unaryExpr ((MUL | DIV) unaryExpr)* ;

unaryExpr 
    : MINUS unaryExpr 
    | primary 
    ;

// --- Left Factoring for Primary ---
primary
    : NUMBER
    | TRUE
    | FALSE
    | LPAREN expression RPAREN
    | ID primaryIdSuffix  // المعرف قد يكون متغيراً أو استدعاء دالة داخل التعبير
    ;

primaryIdSuffix
    : LPAREN args? RPAREN  // استدعاء دالة
    | /* Epsilon (فارغ) */ // مجرد متغير عادي
    ;

// الأنواع
type : INT_T | FLOAT_T | VOID | BOOL ;