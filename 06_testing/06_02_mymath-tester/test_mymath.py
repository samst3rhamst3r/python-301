# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `CustomZeroDivisionError` gets raised correctly.

import mymath, unittest

class TestMyMath(unittest.TestCase):

    def test_subtract_divide(self):
        result = mymath.subtract_divide(10, 7, 2)
        self.assertEqual(result, 2)
    
    def test_subtract_divide_zero_div_error(self):
        self.assertRaises(mymath.CustomZeroDivsionError, mymath.subtract_divide, 10, 5, 5)

if __name__ == "__main__":
    unittest.main()