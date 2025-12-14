class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.dict_books = {}

    def add_book(self, book: Book):
        self.dict_books[book.title] = book.author

    def remove_book(self, book: Book):
        self.dict_books.pop(book.title, None)

    def get_all_books(self):
        return list([key, val] for key, val in self.dict_books.items())


lib = Library()
book1 = Book('1984', 'Gora Orwell')
lib.add_book(book1)
print(lib.get_all_books())
lib.remove_book(book1)
print(lib.get_all_books())
