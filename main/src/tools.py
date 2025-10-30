import re
class Tools:
    @staticmethod
    def prepare_string_for_ai(rawString : str) -> str:
        convertedString = re.sub(r'[\*\+\°BEMH]', '', rawString)
        convertedString = re.sub(r'\s+', ' ', convertedString)
        return convertedString.strip()