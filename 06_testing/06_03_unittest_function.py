# Demonstrate your knowledge of unittest by first creating a function 
# with input parameters and a return value.
# Once you have a function, write at least two tests for the function 
# that use different assertions. The tests should pass.
# Then, include another test that doesn't pass.
#
# NOTE: You can write both the code as well as the tests for it in this file.
# However, feel free to adhere to best practices and separate your tests and
# the functions you are testing into different files.
# Keep in mind that you will run into an error when you'll attempt to import
# this file, because Python modules can't begin with a number.
# You can rename the file to make it work :)

import unittest

def area_rectangle(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be greater than zero.")
    return length * width

class Test_AreaRectangle(unittest.TestCase):

    def test_area_rectangle(self):
        self.assertEqual(area_rectangle(3, 4), 12)
    
    def test_area_rectangle_valid(self):
        self.assertRaises(ValueError, area_rectangle, -1, 5)
    
    def test_area_rectangle_fail(self):
        self.assertIsInstance(area_rectangle(3, 4), str)

if __name__ == "__main__":
    unittest.main()