import re
from typing import Optional
from dataclasses import dataclass
from datetime import datetime
import parsedatetime

@dataclass
class DateManager:
    """Handle date parsing and formatting"""
    date: datetime
    
    @classmethod
    def from_string(cls, date_str: str) -> Optional['DateManager']:
        """Try to parse a date string using parsedatetime library"""
        cal = parsedatetime.Calendar(version=3)

        # date_str contains only numbers, slash, comma, space, hyphen, and letters
        if not re.match(r'^[\d\s\-,/a-zA-Z]+$', date_str):
            return None
        
        try:
            if re.match(r'\d{2}/\d{2}/\d{4}', date_str):
                month, day, year = map(int, date_str.split('/'))
                if month > 12:
                    date_str = f"{day}/{month}/{year}"
                
            time_struct, parse_status = cal.parse(date_str)
            if parse_status > 0:
                return cls(datetime(*time_struct[:3]))
        except ValueError:
            pass
        return None
    
    def to_iso(self) -> str:
        """Convert to ISO 8601 format (YYYY-MM-DD)"""
        return self.date.strftime("%Y-%m-%d")
    
    def to_us(self) -> str:
        """Convert to US format (MM/DD/YYYY)"""
        return self.date.strftime("%m/%d/%Y")
    
    def to_european(self) -> str:
        """Convert to European format (DD/MM/YYYY)"""
        return self.date.strftime("%d/%m/%Y")
    
    def to_long(self) -> str:
        """Convert to long format (Month DD, YYYY)"""
        return self.date.strftime("%B %d, %Y")
    
    def to_short(self) -> str:
        """Convert to abbreviated format (Mon DD, YYYY)"""
        return self.date.strftime("%b %d, %Y")