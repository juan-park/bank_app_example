import unittest

def is_odd(num):
    """Function that checks if number is even or odd"""
    return num%2

class TestIsOdd(unittest.TestCase):
    def test_odd_num(self):
        self.assertTrue(is_odd(3))
        self.assertFalse(is_odd(4))

if __name__=='__main__':
    unittest.main()