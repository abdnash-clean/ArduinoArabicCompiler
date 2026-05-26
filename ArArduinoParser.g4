parser grammar ArArduinoParser;

options {
    tokenVocab = ArArduinoLexer;
}

// نقطة البداية للبرنامج (يتكون من مجموعة من التعريفات)
program : declaration* EOF ;

// التعريف إما أن يكون لمتغير أو لدالة
// التعريف إما متغير، أو دالة عادية، أو إعداد، أو تكرار
declaration 
    : varDecl  
    | setupDec 
    | loopDec 
    | funDecl
    ;

// قاعدة دالة الإعداد (تُجبر المستخدم على أن يكون اسمها إعداد، وبدون معاملات، وترجع فارغ)
setupDec : FUNCTION SETUP LPAREN RPAREN COLON VOID block ;

// قاعدة دالة التكرار (نفس الشيء، اسمها تكرار، وترجع فارغ)
loopDec : FUNCTION LOOP LPAREN RPAREN COLON VOID block ;

// قاعدة الدوال العادية (أي اسم آخر غير إعداد وتكرار)
funDecl : FUNCTION ID LPAREN params? RPAREN COLON type block ;

// قاعدة تعريف المتغيرات (على طريقة Kotlin)
// مثال: متغير ليد : صحيح = 9؛
varDecl : VAR ID COLON type ASSIGN expression SEMI ;



// معاملات الدالة (مفصولة بفاصلة)
params : param (COMA param)* ;

// معامل الدالة الواحد (الاسم : النوع)
param : ID COLON type ;

// كتلة الأكواد
block : LBRACE statement* RBRACE ;

// الجمل البرمجية المتاحة داخل الدوال
statement
    : varDecl                        // تعريف متغير محلي
    | assignment SEMI                // عملية إسناد
    | funcCall SEMI                  // استدعاء دالة
    | ifStat                         // جملة شرطية
    | whileStat                      // حلقة طالما
    | returnStat SEMI                // جملة إرجاع
    ;

// الإسناد: إعطاء قيمة جديدة لمتغير موجود
assignment : ID ASSIGN expression ;

// الجملة الشرطية
ifStat : IF LPAREN expression RPAREN block (ELSE block)? ;

// حلقة التكرار (طالما)
whileStat : WHILE LPAREN expression RPAREN block ;

// جملة الإرجاع
returnStat : RETURN expression? ;

// استدعاء الدوال
funcCall : ID LPAREN args? RPAREN ;

// المعاملات الممررة عند استدعاء دالة
args : expression (COMA expression)* ;

// قاعدة التعابير (Expressions) مع مراعاة أولويات العمليات الحسابية والمنطقية
expression
    : primary                                # primaryExpr
    | ID LPAREN args? RPAREN                 # funcCallExpr
    | LPAREN expression RPAREN               # parensExpr
    | MINUS expression                       # unaryMinusExpr
    | expression (MUL | DIV) expression      # mulDivExpr
    | expression (PLUS | MINUS) expression   # plusMinusExpr
    | expression (GT | LT) expression        # relOpExpr
    | expression AND expression              # andExpr
    | expression OR expression               # orExpr
    ;

// القيم الأساسية
primary
    : NUMBER
    | ID
    | TRUE
    | FALSE
    ;

// الأنواع المدعومة
type : INT_T | FLOAT_T | VOID | BOOL ;