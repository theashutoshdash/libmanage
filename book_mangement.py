class Book:
    def _init_(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def _init_(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"{title} removed successfully.")
                return
        print(f"Book with title {title} not found.")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print("Book found:")
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"ISBN: {book.isbn}")
                return
        print(f"Book with title {title} not found.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("List of books in the library:")
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")

    def sort_books(self):
        self.books.sort(key=lambda x: x.title)

    def manage_fine(self, title, amount):
        for book in self.books:
            if book.title == title:
                print(f"Fine of ${amount} applied to {title}.")
                return
        print(f"Book with title {title} not found.")

# Example usage:
if _name_ == "_main_":
    library = Library()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

    library.add_book(book1)
    library.add_book(book2)

    library.display_books()

    library.sort_books()
    library.display_books()

    library.search_book("To Kill a Mockingbird")

    library.manage_fine("The Great Gatsby", 5)

    library.remove_book("The Great Gatsby")
    library.display_books()
