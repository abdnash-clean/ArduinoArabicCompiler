from antlr4.error.ErrorListener import ErrorListener


class ArabicErrorListener(ErrorListener):
    """يجمع أخطاء ANTLR ويحوّلها إلى رسائل عربية واضحة."""

    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        message = self._translate_message(msg)
        self.errors.append(f"خطأ نحوي (سطر {line}، عمود {column}): {message}")

    def _translate_message(self, msg: str) -> str:
        text = (msg or "").strip()
        lowered = text.lower()

        if "token recognition error" in lowered:
            return "تم العثور على رمز غير معروف أو غير مدعوم."
        if "mismatched input" in lowered:
            return "تم العثور على إدخال غير متوقع في هذا الموضع."
        if "extraneous input" in lowered:
            return "يوجد إدخال إضافي لا يتناسب مع البنية الحالية."
        if "missing" in lowered:
            return "هناك عنصر مفقود في هذا السطر."
        if "no viable alternative" in lowered:
            return "لا يوجد بديل صالح لهذا الجزء من البرنامج."
        if "expecting" in lowered:
            return "تم توقع عنصر آخر هنا."
        return text or "تم اكتشاف خطأ نحوي."
