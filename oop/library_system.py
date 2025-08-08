class Book:
    """
    Base class for representing a book with title and author.
    """
    
    def __init__(self, title, author):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author


class EBook(Book):
    """
    Derived class representing an electronic book.
    Inherits from Book and adds file_size attribute.
    """
    
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The file size in KB
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    """
    Derived class representing a printed book.
    Inherits from Book and adds page_count attribute.
    """
    
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages in the book
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    """
    Library class that demonstrates composition by managing a collection of books.
    """
    
    def __init__(self):
        """
        Initialize a Library instance with an empty list of books.
        """
        self.books = []
    
    def add_book(self, book):
        """
        Add a book to the library.
        
        Args:
            book: A Book, EBook, or PrintBook instance
        """
        self.books.append(book)
    
    def list_books(self):
        """
        Print details of each book in the library.
        """
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
