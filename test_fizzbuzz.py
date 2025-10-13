import unittest
from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
   def setUp(self):
       self.instance=fizzbuzz()
   def test_affiche_sans_param(self):
       self.assertEqual(self.instance.affiche(), "12fizz4buzzfizz")


if __name__ == '__main__':
   unittest.main()
