import unittest
from replacing_non_perfect_squares import replace_non_perfect_squares


class TestReplacingNonPerfectSquares(unittest.TestCase):

    def test_replacing_non_perfect_squares_function(self):
        input_data = [4, 7, 9, 10, 49, 6]
        expected = [4, -1, 9, -1, 49, -1]

        actual = replace_non_perfect_squares(input_data)

        self.assertEqual(expected, actual)

