@echo offتعيين المتغير للجلسة الحالية ::

set "ANTLR_JAR=E:\ArabicCompilerProject\tools\antlr-4.13.2-complete.jar"


doskey antlr4=java -jar "%ANTLR_JAR%" $*
doskey grun=java -cp ".;%ANTLR_JAR%" org.antlr.v4.gui.TestRig $*