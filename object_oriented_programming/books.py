class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.book = []

    def add_book(self, book):
        self.book.append(book)

    def remove_book(self, book):
        for lib_books in self.book:
            if (book.title == lib_books.title and book.author == lib_books.author):
                self.book.remove(book)

    def search_book(self, search_string):
        result = []
        for lib_book in self.book:
            if (search_string.lower() in lib_book.lower() or search_string.lower() in lib_book.lower()):
                result.append(lib_book)
        return result
