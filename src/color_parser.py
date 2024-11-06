import re
from typing import Optional
import colorsys
from dataclasses import dataclass

@dataclass
class Color:
    """Internal color representation with parsing and conversion methods"""
    r: float
    g: float
    b: float
    
    @classmethod
    def from_string(cls, color_str: str) -> Optional['Color']:
        """Detect and parse color string in any supported format"""
        color_str = color_str.strip().lower()
        
        # Try HEX
        if color_str.startswith('#'):
            hex_color = color_str.lstrip('#')
            if len(hex_color) == 6:
                try:
                    r, g, b = tuple(int(hex_color[i:i+2], 16)/255 for i in (0, 2, 4))
                    return cls(r, g, b)
                except ValueError:
                    pass
                    
        # Try RGB
        rgb_match = re.match(r'rgb\((\d+),\s*(\d+),\s*(\d+)\)', color_str)
        if rgb_match:
            try:
                r, g, b = (int(x)/255 for x in rgb_match.groups())
                return cls(r, g, b)
            except ValueError:
                pass
                
        hsl_pattern = r'''hsl\(
            (\d*\.?\d+)\s*,\s*
            (\d*\.?\d+)%?\s*,\s*
            (\d*\.?\d+)%? 
            \)'''
        hsl_match = re.match(hsl_pattern, color_str, re.VERBOSE)
        if hsl_match:
            try:
                h, s, l = (float(x) for x in hsl_match.groups())
                h = max(0, min(360, h))
                s = max(0, min(100, s))
                l = max(0, min(100, l))
                rgb = colorsys.hls_to_rgb(h/360, l/100, s/100)
                return cls(*rgb)
            except ValueError:
                pass
            
        return None
    
    def to_hex(self) -> str:
        """Convert to hex format"""
        return f"#{int(self.r*255):02x}{int(self.g*255):02x}{int(self.b*255):02x}"
    
    def to_rgb(self) -> str:
        """Convert to RGB format"""
        return f"rgb({int(self.r*255)}, {int(self.g*255)}, {int(self.b*255)})"
    
    def to_hsl(self) -> str:
        """Convert to HSL format"""
        h, l, s = colorsys.rgb_to_hls(self.r, self.g, self.b)
        return f"hsl({h*360:.1f}, {s*100:.1f}%, {l*100:.1f}%)"