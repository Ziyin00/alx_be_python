"""
Library management system with Book and Library classes.
"""


class Book:
    """A book class with title, author, and checkout status."""

    def __init__(self, title, author):
        """
        Initialize a book with title and author.

        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Check out the book if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        """Return string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A library class to manage a collection of books."""

    def __init__(self):
        """Initialize an empty library."""
        self._books = []

    def add_book(self, book):
        """
        Add a book to the library.

        Args:
            book (Book): The book to add
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by title.

        Args:
            title (str): The title of the book to check out

        Returns:
            bool: True if book was successfully checked out, False otherwise
        """
        for book in self._books:
            if book.title == title and book.is_available():
                return book.check_out()
        return False

    def return_book(self, title):
        """
        Return a book by title.

        Args:
            title (str): The title of the book to return

        Returns:
            bool: True if book was successfully returned, False otherwise
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                return book.return_book()
        return False

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(book)
