import unittest
from string_utils import reverse_string, capitalize_string, is_capitalized


class TestStringUtils(unittest.TestCase):

    def test_reverse_string(self):
       self.assertEqual(reverse_string('mochi'), 'ihcom')

    def test_capitalize_string(self):
       self.assertEqual(capitalize_string('hello'),'Hello')

    def test_is_capitalized(self):
       self.assertTrue(is_capitalized('Hello'))

if __name__ == '__main__':
  unittest.main()