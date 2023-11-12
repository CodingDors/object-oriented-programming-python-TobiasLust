import re

class Book:
    def __init__(self, title: str, author: str, book_id: str):
        """
        Initializes a new book.

        :param title: The title of the book.
        :param author: The author of the book.
        :param book_id: The id of the book.
        """
        self.title = title
        self.author = author
        self.book_id = book_id

class Library:
    def __init__(self):
        """
        Initializes a new library.
        """
        self.books = {}

    def add_book(self, book: Book) -> bool:
        """
        Adds a book to the library.

        :param book: The book object to add.
        :return: True if the book was added, False otherwise.
        Ensure that the book ID is validated before attempting to remove the book
        and hasn't already been added
        """
        # TODO: Implement the method
        raise NotImplementedError("This method has not been implemented yet.")
    

    def remove_book(self, book_id: str) -> bool:
        """
        Removes a book from the library using its id.

        :param book_id: The id of the book to remove.
        :return: True if the book was removed, False otherwise.
        """
        # TODO: Implement the method
        raise NotImplementedError("This method has not been implemented yet.")


    def find_book(self, book_id: str) -> Book:
        """
        Finds a book in the library using its id.

        :param book_id: The id of the book to find.
        :return: Book object if found, None otherwise.
        """
        # TODO: Implement the method
        raise NotImplementedError("This method has not been implemented yet.")

    def validate_book_id(self, book_id: str) -> bool:
        """
        Validates the book's id using a regular expression.

        :param book_id: The id of the book to validate.
        :return: True if the id is valid, False otherwise.
        """
        pattern = re.compile(r'^B\d{4}$')
        return bool(pattern.match(book_id))


# ================================================================================
# This is a driver function for the Library class.
# 
# The purpose of this function is to provide students with a series of statements 
# that can be used to manually test the functionality of the Library and Book classes 
# as they're being implemented. 
#
# Students can run this function to see the output of their code, add breakpoints,
# and make use of print statements or other debugging techniques. This allows for 
# a hands-on approach to understanding and testing the behavior of the code.
# ================================================================================

def driver():
    """A manual test function for the Library class."""
    library = Library()
    print("Initialized a new library.")

    # Adding a valid book
    # book1 = Book("Harry Potter", "J.K. Rowling", "B1234")
    # result = library.add_book(book1)
    # print(f"Adding book with ID {book1.book_id}. Success: {result}")

    # # Trying to add the same book again
    # result = library.add_book(book1)
    # print(f"Trying to add book with ID {book1.book_id} again. Success: {result}")

    # # Trying to add an invalid book
    # invalid_book = Book("Invalid Book", "Author Name", "BK123")
    # result = library.add_book(invalid_book)
    # print(f"Trying to add book with ID {invalid_book.book_id}. Success: {result}")

    # # Removing the valid book
    # result = library.remove_book(book1.book_id)
    # print(f"Removing book with ID {book1.book_id}. Success: {result}")

    # # Trying to find the removed book
    # found_book = library.find_book(book1.book_id)
    # print(f"Searching for book with ID {book1.book_id}. Found: {found_book}")

if __name__ == "__main__":
    driver()