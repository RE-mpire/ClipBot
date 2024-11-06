class LineParser:
    @staticmethod
    def remove_duplicates(text: str) -> str:
        return '\n'.join(dict.fromkeys(text.splitlines()))
    
    @staticmethod
    def strip_empty_lines(text: str) -> str:
        return '\n'.join(line for line in text.splitlines() if line.strip())
    
    @staticmethod
    def sort_lines(text: str) -> str:
        return '\n'.join(sorted(text.splitlines()))
    
    @staticmethod
    def to_list(text: str) -> str:
        # converts comma-separated text to a new line separated list
        return '\n'.join(text.replace(',', '').split())
    
    @staticmethod
    def to_csv(text: str) -> str:
        # converts a newlines separated list to a comma-separated text
        return ', '.join(text.splitlines())