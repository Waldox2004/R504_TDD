def crypt(message):
    res = ""
    for c in message:
        res += chr(ord(c) + 1)
    return res
