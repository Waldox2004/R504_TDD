def affiche(n=100):
    res = ""
    for i in range(1, n + 1):
        if i % 15 == 0:
            res += "FrisBee"
        elif i % 3 == 0:
            res += "Fizz"
        elif i % 5 == 0:
            res += "Buzz"
        else:
            res += str(i)
    return res


