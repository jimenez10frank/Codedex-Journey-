import unittest
import math

def get_sqrt(n):
    return math.sqrt(n)
    

def divide(a, b):
    return a / b

class TestUnexpected(unittest.TestCase):
    # here gives the square root back
    def test_get_sqrt_valid(self):
        self.assertEqual(get_sqrt(144),  12)
    
    # test for error when negative number
    def test_negative_numver(self):
        with self.assertRaises(ValueError):
            get_sqrt(-1)

    def test_divide(self):
        self.assertEqual(divide(144, 12), 12)

    def test_divide_negative(self):
        with self.assertRaises(ZeroDivisionError
                               ):
            divide(4, 0)

if __name__ == '__main__':
  unittest.main()