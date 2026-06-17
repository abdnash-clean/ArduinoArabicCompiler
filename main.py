# main.py (النسخة النهائية مع ميزة تنظيف وتسوية النصوص العربية)
import sys
import re
import unicodedata
from antlr4 import *
from frontend.ArArduinoLexer import ArArduinoLexer
from frontend.ArArduinoParser import ArArduinoParser
from frontend.ast_builder import ASTBuilderVisitor
from semantic.semantic_analyzer import SemanticAnalyzerVisitor
from ast_visualizer import ASTVisualizerVisitor

def normalize_arabic_text(text: str) -> str:
    """
    أنبوب معالجة وتسوية النصوص العربية قبل التحليل المعجمي (Normalization Pipeline):
    1. تطبيق التسوية المعيارية NFC لدمج الحروف المركبة كـ (لا).
    2. حذف علامات التشكيل صامتاً (Tashkeel: U+064B to U+065F).
    3. حذف كشيدة التطويل صامتاً (ـ: U+0640).
    4. توحيد الهمزات: استبدال (أ، إ، آ) بألف عادية (ا).
    """
    # 1. التسوية المعيارية لتوحيد أشكال الحروف المركبة
    nfc_text = unicodedata.normalize('NFC', text)
    
    # 2. تعبير نمطي لحذف علامات التشكيل وكشيدة التطويل
    clean_text = re.sub(r'[\u064B-\u065F\u0640]', '', nfc_text)
    
    # 3. توحيد الهمزات: استبدال (أ، إ، آ) بألف عادية (ا) لمرونة تامة في الكتابة
    clean_text = re.sub(r'[أإآ]', 'ا', clean_text)
    
    return clean_text

def main():
    # 1. قراءة محتوى الملف النصي كـ String عادي لتنظيفه أولاً
    try:
        with open('test_arduino.txt', 'r', encoding='utf-8') as f:
            raw_text = f.read()
    except FileNotFoundError:
        print("خطأ: لم يتم العثور على الملف test_arduino.txt")
        sys.exit(1)

    # 2. تطبيق فلتر تنظيف وتسوية النص العربي
    clean_text = normalize_arabic_text(raw_text)

    # 3. تمرير النص النظيف لـ ANTLR عبر InputStream الذاكرة
    input_stream = InputStream(clean_text)

    # 4. التحليل المعجمي والنحوي
    lexer = ArArduinoLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ArArduinoParser(token_stream)
    parse_tree = parser.program()

    builder = ASTBuilderVisitor()
    ast = builder.visit(parse_tree)

    # 5. تشغيل التحليل الدلالي وفحص توافق الأنواع (Type Checking)
    print("\n" + "=" * 60)
    print("--- جاري التحليل الدلالي وفحص توافق الأنواع (Type Checking) ---")
    print("=" * 60)
    
    analyzer = SemanticAnalyzerVisitor()
    ast.accept(analyzer)

    # 6. تقرير الأخطاء الدلالية أو تشغيل الرسام في حال نجاح التحليل
    if analyzer.errors:
        print(f"❌ تم العثور على أخطاء دلالية ({len(analyzer.errors)} أخطاء):")
        for err in analyzer.errors:
            print(f"   ❌ {err}")
        print("\nفشلت عملية الترجمة. الرجاء إصلاح الأخطاء أعلاه.")
    else:
        print("✅ الكود سليم دلالياً ونحوياً 100%!")
        print("جاري توليد الرسم الهندسي البصري (PNG)...")
        visualizer = ASTVisualizerVisitor()
        ast.accept(visualizer)
        visualizer.render('ar_arduino_ast')

if __name__ == '__main__':
    main()