# main.py
import sys
from antlr4 import *
from frontend.ArArduinoLexer import ArArduinoLexer
from frontend.ArArduinoParser import ArArduinoParser
from frontend.ast_builder import ASTBuilderVisitor
from semantic.semantic_analyzer import SemanticAnalyzerVisitor

def main():
    # 1. قراءة الكود
    try:
        input_stream = FileStream('test_arduino.txt', encoding='utf-8')
    except FileNotFoundError:
        print("خطأ: لم يتم العثور على الملف test_arduino.txt")
        sys.exit(1)

    # 2. الواجهة الأمامية وبناء الشجرة
    lexer = ArArduinoLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ArArduinoParser(token_stream)
    parse_tree = parser.program()

    builder = ASTBuilderVisitor()
    ast = builder.visit(parse_tree)

    # 3. تشغيل التحليل الدلالي وفحص الأنواع (Type Checking)
    print("\n" + "=" * 60)
    print("--- جاري التحليل الدلالي وفحص توافق الأنواع (Type Checking) ---")
    print("=" * 60)
    
    analyzer = SemanticAnalyzerVisitor()
    ast.accept(analyzer) # انطلاق المحلل الدلالي للأنواع

    # 4. تقرير الأخطاء الهندسية
    if analyzer.errors:
        print(f"❌ تم العثور على أخطاء دلالية ({len(analyzer.errors)} أخطاء):")
        for err in analyzer.errors:
            print(f"   ❌ {err}")
        print("\nفشلت عملية الترجمة. الرجاء إصلاح الأخطاء أعلاه.")
    else:
        print("✅ الكود سليم دلالياً ونحوياً 100%! جاهز لتوليد كود الآلة.")

if __name__ == '__main__':
    main()