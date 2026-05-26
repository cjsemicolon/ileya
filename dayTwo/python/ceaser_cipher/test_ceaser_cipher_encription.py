import unittest
from ceaser_cipher_encription import*

class TestEncryption(unittest.TestCase):

    def test_function_encrypts_lowercase_letters(self):

        password = "dog"
        shift = 3

        expected = "grj"

        actual = encryption(password, shift)

        self.assertEqual(expected, actual)

    def test_encrypts_uppercase_letters(self):

        password = "DOG"
        shift = 3

        expected = "GRJ"

        actual = encryption(password, shift)

        self.assertEqual(expected, actual)

    def test_wraps_around_alphabet(self):

        password = "XYZ"
        shift = 3

        expected = "ABC"

        actual = encryption(password, shift)

        self.assertEqual(expected, actual)

    def test_keeps_numbers_and_symbols(self):

        password = "Dog123!"
        shift = 3

        expected = "Grj123!"

        actual = encryption(password, shift)

        self.assertEqual(expected, actual)

    def test_decrypts_with_negative_shift(self):

        password = "Grj"
        shift = -3

        expected = "Dog"

        actual = encryption(password, shift)

        self.assertEqual(expected, actual)

