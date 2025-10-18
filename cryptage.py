def crypt(message, pas=1):
    res = ""
    for c in message:
        res += chr(ord(c) + pas)
    return res + str(pas)

def decrypt(message):
    pas = int(message[-1])
    corps = message[:-1]
    res = ""
    for c in corps:
        res += chr(ord(c) - pas)
    return res
