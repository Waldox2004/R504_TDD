import unittest
from cryptage import crypt

def test_crypt_simple():
    assert crypt("abc") == "bcd"

def test_crypt_avec_pas():
    assert crypt("abc", 2) == "cde2"

if __name__ == '__main__':
    unittest.main()