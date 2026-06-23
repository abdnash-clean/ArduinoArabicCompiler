# main.py (النسخة النهائية مع ميزة تنظيف وتسوية النصوص العربية)
import sys
from backend.optimizer import Optimizer
from normlize import normalize_arabic_text 
from antlr4 import *
from frontend.ArArduinoLexer import ArArduinoLexer
from frontend.ArArduinoParser import ArArduinoParser
from frontend.ast_builder import ASTBuilderVisitor
from semantic.semantic_analyzer import SemanticAnalyzerVisitor
from backend.ir_generator import LLVMIRGenerator
# from ast_visualizer import ASTVisualizerVisitor



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
        ir_generator = LLVMIRGenerator()
        # visualizer = ASTVisualizerVisitor()
        # ast.accept(visualizer)
        # visualizer.render('ar_arduino_ast')
        ast.accept(ir_generator)
        print("\n--- LLVM IR OUTPUT ---")
        print(ir_generator.get_ir())
        llvm_ir = ir_generator.get_ir()
        print("\n--- توليد لغة التجميع AVR ---")
        optimizer = Optimizer(opt_level=2, size_level=1,verbose=True)
        optimized_ir = optimizer.optimize(llvm_ir)
        optimizer.write_object(optimized_ir, "output.o")
        print(optimizer.emit_assembly(optimized_ir))
if __name__ == '__main__':
    main()