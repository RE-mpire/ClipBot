import hashlib
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