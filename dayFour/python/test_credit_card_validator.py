import unittest

from credit_card_validator import (
    convert_number_to_array,
    get_card_type,
    calculate_sum_of_doubled_even_position_digits,
    calculate_sum_of_odd_position_digits,
    is_valid_card
)


class CreditCardValidatorTest(unittest.TestCase):

    def test_convert_number_to_array(self):
        card_number = 438857

        expected_digits = [4, 3, 8, 8, 5, 7]

        actual_digits = convert_number_to_array(card_number)

        self.assertEqual(expected_digits, actual_digits)

    def test_get_card_type_returns_visa(self):
        card_digits = [4, 3, 8, 8, 5, 7]

        expected_card_type = "Visa Card"

        actual_card_type = get_card_type(card_digits)

        self.assertEqual(expected_card_type, actual_card_type)

    def test_get_card_type_returns_mastercard(self):
        card_digits = [5, 3, 8, 8, 5, 7]

        expected_card_type = "MasterCard"

        actual_card_type = get_card_type(card_digits)

        self.assertEqual(expected_card_type, actual_card_type)

    def test_get_card_type_returns_discover(self):
        card_digits = [6, 3, 8, 8, 5, 7]

        expected_card_type = "Discover Card"

        actual_card_type = get_card_type(card_digits)

        self.assertEqual(expected_card_type, actual_card_type)

    def test_get_card_type_returns_american_express(self):
        card_digits = [3, 7, 8, 8, 5, 7]

        expected_card_type = "American Express Card"

        actual_card_type = get_card_type(card_digits)

        self.assertEqual(expected_card_type, actual_card_type)


    def test_is_valid_card_returns_false(self):
        card_digits = convert_number_to_array(4388576018402625)

        expected_validity_status = False

        actual_validity_status = is_valid_card(card_digits)

        self.assertEqual(expected_validity_status, actual_validity_status)

    def test_is_valid_card_returns_false(self):
        card_digits = convert_number_to_array(4388576018402627)

        expected_validity_status = False

        actual_validity_status = is_valid_card(card_digits)

        self.assertEqual(expected_validity_status, actual_validity_status)



