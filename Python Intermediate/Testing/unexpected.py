import unittest
import math

def get_sqrt(n):
    return math.sqrt(n)
    

def divide(a, b):
    return a / b

class TestUnexpected(unittest.TestCase):

    def test_get_sqrt_valid(self):
        self.assertEqual(get_sqrt(144),  12)


if __name__ == '__main__':
  unittest.main()