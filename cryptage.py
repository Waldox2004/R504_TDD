def crypt(message, pas=1):
    res = ""
    for c in message:
        res += chr(ord(c) + pas)
    return res + str(pas)
