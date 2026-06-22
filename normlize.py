import re
import unicodedata

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