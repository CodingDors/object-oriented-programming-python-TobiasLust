"""
#######################################################
WARNING:

The code below contains the solution to the problem. 

ONLY refer to it after you've genuinely tried to 
solve the problem on your own. Struggling with a problem 
and trying to devise a solution on your own, even if not 
successful, is an essential part of the learning process.

Please ensure you've given it a fair attempt before diving 
into the solution.

#######################################################
"""




















import re

class Book:
    def __init__(self, title: str, author: str, book_id: str):
        self.title = title
        self.author = author
        self.book_id = book_id

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book: Book) -> bool:
        # Check if book_id is valid
        if not self.validate_book_id(book.book_id):
            return False

        # Check if book_id is already in the library
        if book.book_id in self.books:
            return False
        
        # Add the book to the library
        self.books[book.book_id] = book
        return True

    def remove_book(self, book_id: str) -> bool:
        # Check if book_id is valid
        if not self.validate_book_id(book_id):
            return False

        # Remove the book if it exists in the library
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False

    def find_book(self, book_id: str) -> Book:
        # Check if book_id is valid
        if not self.validate_book_id(book_id):
            return None

        # Return the book if it exists in the library
        return self.books.get(book_id, None)

    def validate_book_id(self, book_id: str) -> bool:
        pattern = re.compile(r'^B\d{4}$')
        return bool(pattern.match(book_id))
