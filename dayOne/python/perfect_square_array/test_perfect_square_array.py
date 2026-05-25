import unittest
from perfect_square_array import return_perfect_squares

class Test_perfect_square_array(unittest.TestCase):

    def test_that_returning_perfect_squares_function_works(self):

        input = [4, 7, 9, 10, 16, 18];

        expected = [4, 9, 16];

        actual = return_perfect_squares(input);

        self.assertEqual(expected, actual);

 
