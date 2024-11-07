import hashlib
import base64
import random
import string
from src.hash_generator import HashGenerator

def random_string(length=10):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def test_md5():
    test_string = random_string()
    hash_gen = HashGenerator(test_string)
    assert hash_gen.get_md5() == hashlib.md5(test_string.encode()).hexdigest()

def test_sha1():
    test_string = random_string()
    hash_gen = HashGenerator(test_string)
    assert hash_gen.get_sha1() == hashlib.sha1(test_string.encode()).hexdigest()

def test_sha256():
    test_string = random_string()
    hash_gen = HashGenerator(test_string)
    assert hash_gen.get_sha256() == hashlib.sha256(test_string.encode()).hexdigest()

def test_encode_base64():
    test_string = random_string()
    hash_gen = HashGenerator(test_string)
    assert hash_gen.encode_base64() == base64.b64encode(test_string.encode()).decode()

def test_decode_base64():
    test_string = random_string()
    encoded_string = base64.b64encode(test_string.encode()).decode()
    hash_gen = HashGenerator(encoded_string)
    assert hash_gen.decode_base64() == test_string

def test_base64_padding():
    test_string = random_string(7)
    hash_gen = HashGenerator(test_string)
    encoded_string = hash_gen.encode_base64()
    assert len(encoded_string) % 4 == 0