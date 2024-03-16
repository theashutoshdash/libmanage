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

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book with ISBN {isbn} removed successfully.")
                return
        print("Book not found.")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                print(f"Book found - Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
                return
        print("Book not found.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Books in the library:")
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display Books")
        #print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            new_book = Book(title, author, isbn)
            library.add_book(new_book)

        elif choice == '2':
            isbn = input("Enter ISBN of the book to remove: ")
            library.remove_book(isbn)

        elif choice == '3':
            title = input("Enter title of the book to search: ")
            library.search_book(title)

        elif choice == '4':
            library.display_books()

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if _name_ == "_main_":
    main()
