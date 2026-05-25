import unittest;
from palindromic_array import*;

class Test_palindromic_array(unittest.TestCase):

    def test_the_check_if_array_is_a_palindrome_function_with_a_palindrome(self):

        input = [45, 0, 8, 0, 45];

        expected = True;

        actual = check_if_array_is_a_palindrome(input);

        self.assertEqual(expected, actual)
   

    def test_the_check_if_array_is_a_palindrome_function_with_a_non_palindrome(self):

        input = [3, 0, 8, 0, 45];

        expected = False;

        actual = check_if_array_is_a_palindrome(input);

        self.assertEqual(expected, actual)



 
