import unittest
from exercise import *

class TestLibrary(unittest.TestCase):
    
    def setUp(self):
        self.library = Library()
        self.valid_book = Book("Harry Potter", "J.K. Rowling", "B1234")
        self.invalid_id_book = Book("Sample Book", "Author Name", "BK123")

    def test_add_book_valid_id(self):
        """Test adding a book with a valid ID."""
        result = self.library.add_book(self.valid_book)
        self.assertTrue(result)
        self.assertIn(self.valid_book.book_id, self.library.books)

    def test_add_book_duplicate_valid_id(self):
        """Test trying to add a book with a valid ID that's already in the library."""
        self.library.add_book(self.valid_book)  # Adding the book for the first time
        result = self.library.add_book(self.valid_book)  # Trying to add it again
        self.assertFalse(result)

    def test_add_book_invalid_id(self):
        """Test trying to add a book with an invalid ID."""
        result = self.library.add_book(self.invalid_id_book)
        self.assertFalse(result)
        self.assertNotIn(self.invalid_id_book.book_id, self.library.books)

    # Test cases for remove_book function
    def test_remove_book_valid_id(self):
        self.library.add_book(self.valid_book)
        self.assertTrue(self.library.remove_book(self.valid_book.book_id))
        self.assertNotIn(self.valid_book.book_id, self.library.books)

    def test_remove_book_invalid_id(self):
        self.library.add_book(self.valid_book)
        self.assertFalse(self.library.remove_book(self.invalid_id_book.book_id))
        self.assertIn(self.valid_book.book_id, self.library.books)

    def test_remove_non_existent_book(self):
        self.assertFalse(self.library.remove_book(self.valid_book.book_id))

    # Test cases for find_book function
    def test_find_book_valid_id(self):
        self.library.add_book(self.valid_book)
        found_book = self.library.find_book(self.valid_book.book_id)
        self.assertEqual(found_book, self.valid_book)

    def test_find_book_invalid_id(self):
        self.library.add_book(self.valid_book)
        self.assertIsNone(self.library.find_book(self.invalid_id_book.book_id))

    def test_find_non_existent_book(self):
        self.assertIsNone(self.library.find_book(self.valid_book.book_id))

if __name__ == '__main__':
    unittest.main()

