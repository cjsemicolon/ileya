import unittest  
from even_and_odds import *

class Test_even_and_odds_array(unittest.TestCase):

    
    def test_the_sorting_of_even_elements(self):

        input = [1,3,2,4,5,6,7,8]; 
        expected = [2,4,6,8];
        actual = collect_even_elements(input);
        self.assertEqual(expected, actual);


    def test_the_sorting_of_odd_elements(self):

        input = [1,3,2,4,5,6,7,8]; 
        expected = [1,3,5,7];
        actual = collect_odd_elements(input);
        self.assertEqual(expected, actual);

    
    def test_the_return_of_split_array(self):

        input = [1,3,2,4,5,6,7,8]; 
        expected = [[2,4,6,8],[1,3,5,7]];
        actual = split_array(input);
        self.assertEqual(expected, actual);

    


