import unittest
from cryptage import crypt

def test_crypt_simple():
    assert crypt("abc") == "bcd"

if __name__ == '__main__':
    unittest.main()