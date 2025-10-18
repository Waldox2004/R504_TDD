import unittest
from fizzbuzz import affiche

class TestFizzBuzz(unittest.TestCase):
    def test_affiche_sans_param(self):
        result = affiche()
        self.assertIn("FrisBee", result)
        self.assertTrue(result.startswith("12Fizz"))

def test_affiche_avec_param(self):
    result = affiche(15)
    self.assertEqual(result, "12Fizz4BuzzFizz78FizzBuzz11Fizz1314FrisBee")


if __name__ == '__main__':
    unittest.main()
