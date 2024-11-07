import hashlib
import base64
from dataclasses import dataclass

@dataclass
class HashGenerator:
    string: str

    def __init__(self, string: str):
        self.string = string

    def get_md5(self):
        return hashlib.md5(self.string.encode()).hexdigest()
    
    def get_sha1(self):
        return hashlib.sha1(self.string.encode()).hexdigest()
    
    def get_sha256(self):
        return hashlib.sha256(self.string.encode()).hexdigest()
    
    def encode_base64(self):
        return base64.b64encode(self.string.encode()).decode()
    
    def decode_base64(self):
        return base64.b64decode(self.string).decode()