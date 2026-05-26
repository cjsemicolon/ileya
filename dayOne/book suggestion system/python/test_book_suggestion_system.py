import unittest
from book_suggestion_system import *

class TestBookSuggestion(unittest.TestCase):

    def test_add_book(self):

        result = add_book("Atomic Habits")

        self.assertEqual(result, "Book added successfully")

    def test_remove_book(self):

        add_book("Dune")

        result = remove_book("Dune")

        self.assertEqual(result, "Book removed successfully")

    def test_update_book(self):

        result = update_book("Harry Potter", "Harry Potter 2")

        self.assertEqual(result, "Book updated successfully")


