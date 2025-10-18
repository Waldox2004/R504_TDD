def affiche(n1=1, n2=100):
    res = ""
    for i in range(n1, n2 + 1):
        if i % 15 == 0:
            res += "FrisBee"
        elif i % 3 == 0:
            res += "Fizz"
        elif i % 5 == 0:
            res += "Buzz"
        else:
            res += str(i)
    return res



