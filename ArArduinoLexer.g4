lexer grammar ArArduinoLexer;

VAR     : 'متغير' ;
IF      : 'لو' | 'إذا' | 'اذا' ;
ELSE    : 'والا' | 'وإلا' ;
WHILE   : 'طالما' ;
TRUE    : 'صح' ;
FALSE   : 'غلط' ;
INT_T   : 'صحيح' ;
FLOAT_T : 'عشري' ;
VOID    : 'فارغ' ;
FUNCTION : 'دالة' ;
RETURN  : 'ارجع' ;
SETUP   : 'إعداد' ;
LOOP    : 'تكرار' ;
BOOL    : 'منطقي' ;
GTE : '>=' ;
LTE : '<=' ;
EQ  : '==' ;
NEQ : '!=' ;
ASSIGN  : '=' ;
PLUS    : '+' ;
MINUS   : '-' ;
MUL     : '*' ;
DIV     : '/' ;
GT      : '>' ;
LT      : '<' ;
OR      : 'أو' ;
AND     : 'و' ;
LPAREN  : '(' ;
RPAREN  : ')' ;
LBRACE  : '{' ;
RBRACE  : '}' ;
COLON   : ':' ;
SEMI    : '؛' ;
COMA    : ',' ;



fragment DIGIT : [0-9] | [\u0660-\u0669] ;
NUMBER  : DIGIT+ ('.' DIGIT+)? ;
ID      : [\u0621-\u064A] [\u0621-\u064A\u0660-\u06690-9_]* ;
WS      : [ \t\r\n]+ -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
