from cryptage import crypt

def test_crypt_simple():
    assert crypt("abc") == "bcd"
