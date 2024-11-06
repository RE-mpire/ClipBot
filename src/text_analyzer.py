from typing import Dict

class TextAnalyzer:
    @staticmethod
    def count_words(text: str) -> int:
        return len(text.split())
    
    @staticmethod
    def count_chars(text: str) -> Dict[str, int]:
        return {
            'total': len(text),
            'no_spaces': len(text.replace(' ', '')),
            'no_whitespace': len(''.join(text.split()))
        }
    
    @staticmethod
    def line_count(text: str) -> int:
        return 0 if text == "" else len(text.splitlines())
    
    @staticmethod
    def count_paragraphs(text: str) -> int:
        return 0 if text == "" else len(text.split('\n\n'))
    
    @staticmethod
    def count_sentences(text: str) -> int:
        return 0 if text == "" else len(text.split('. '))
    
    @staticmethod
    def read_time(text: str, wpm: int = 180) -> str:
        time = len(text.split()) // wpm
        if time < 1:
            return "Less than a minute"
        return f"{time} minute{'s' if time > 1 else ''}"