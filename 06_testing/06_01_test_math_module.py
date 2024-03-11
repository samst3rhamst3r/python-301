# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.

import unittest, math

class TestMath(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(math.factorial(5), 120)
    
    def test_sumprod(self):
        self.assertEqual(math.fabs(-5), 5)

if __name__ == "__main__":
    unittest.main()