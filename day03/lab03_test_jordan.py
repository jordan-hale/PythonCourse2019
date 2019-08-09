import unittest
from lab03_jordan import *

class labTests(unittest.TestCase):

	## fill in a few tests for each
	## make sure to account for correct and incorrect input

    def test_shout(self):
		self.assertEqual('JORDAN', shout('jordan'))

    def test_reverse(self):
		self.assertEqual()

    def test_reversewords(self):

    def test_reversewordletters(self):

    def test_piglatin(self):


if __name__ == '__main__':
  unittest.main()


    def test_vowels(self):
        self.assertEqual(4, count_vowels("mississippi"))
        with self.assertRaises(TypeError): count_vowels(5)
        with self.assertRaises(TypeError): count_vowels([1,2,3])
