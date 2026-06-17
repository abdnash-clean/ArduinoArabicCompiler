lexer grammar ArArduinoLexer;

VAR     : 'متغير' ;
IF      : 'لو' | 'اذا' ;
ELSE    : 'والا'  ;
WHILE   : 'طالما' ;
TRUE    : 'صح' ;
FALSE   : 'غلط' ;
INT_T   : 'صحيح' | 'رقم';
FLOAT_T : 'عشري' | 'كسري';
VOID    : 'فارغ' ;
FUNCTION : 'دالة' | 'مهمة' | 'امر';
RETURN  : 'ارجع' ;
SETUP   : 'اعداد' ;
LOOP    : 'تكرار' | 'حلقة' ;
BOOL    : 'منطقي' ;
BREAK   : 'اقطع' ;
CONTINUE : 'تجاوز'  ;
DO      : 'نفذ';
PRINT   : 'اكتب' ;
ASSIGN  : '=' ;
PLUS    : '+' ;
MINUS   : '-' ;
MUL     : '*' ;
DIV     : '/' ;
INC     : '++' ;
DEC     : '--' ;
ADD_ASSIGN : '+=' ;
SUB_ASSIGN : '-=' ;
MOD     : '%' ;
GTE : '>=' ;
LTE : '<=' ;
EQ  : '==' ;
NEQ : '!=' ;
GT      : '>' ;
LT      : '<' ;
OR      : 'او' | '||';
AND     : 'و' | '&&' ;
NOT     : 'ليس' | '!' ;
LPAREN  : '(' ;
RPAREN  : ')' ;
LBRACE  : '{' ;
RBRACE  : '}' ;
COLON   : ':' ;
SEMI    : '؛' ;
COMA    : '،' ;
BW_OR   : '|' ;
BW_AND  : '&' ;
BW_XOR  : '^' ;
BW_NOT  : '~' ;
// إضافة نوع البيانات في الكلمات المفتاحية
STRING_T : 'نص' ;
CHAR_T   : 'حرف' ;
// قواعد النص والحرف في الأسفل
STRING   : '"' ~["\r\n]* '"' ;
CHAR     : '’' . '’' ;
IMPORT : 'اضافة'| 'مكتبة' | 'استيراد' ;



fragment DIGIT : [0-9] | [\u0660-\u0669] ;
NUMBER  : DIGIT+ ('.' DIGIT+)? ;
ID      : [\u0621-\u064A] [\u0621-\u064A\u0660-\u06690-9_]* ;
WS      : [ \t\r\n]+ -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;