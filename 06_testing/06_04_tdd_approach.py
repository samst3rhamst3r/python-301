# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.

import unittest

class TestStrManipulation(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(upper("sam"), "SAM")
    
    def test_lower(self):
        self.assertEqual(lower("SAM"), "sam")
    
    def test_capitalize(self):
        self.assertEqual(capitalize("sAm"), "Sam")
    
    def test_make_full_name(self):
        self.assertEqual(make_full_name("sAm", " tUrnEr "), "Sam Turner")
    
    def test_valid_input(self):
        self.assertRaises(ValueError, valid_input, "1")