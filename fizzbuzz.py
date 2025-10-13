class fizzbuzz:
   def __init__(self):
       pass


   def affiche():
       res = ""
       for i in range(1, 101):
           if i % 15 == 0:
               res += "FrisBee"
           elif i % 3 == 0:
               res += "Fizz"
           elif i % 5 == 0:
               res += "Buzz"
           else:
               res += str(i)
       return res
