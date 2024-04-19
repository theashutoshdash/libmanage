class LibraryManagementSystem:
    def __init__(self):
        self.students = {}  # Dictionary to store student details
        self.books = {}     # Dictionary to store book details

    def add_student(self, reg_number, name):
        """Add a new student to the database."""
        if reg_number not in self.students:
            self.students[reg_number] = {
                'name': name,
                'history': [],       # List to track book issues history
                'fine_amount': 0.0,  # Fine amount (initially zero)
                'status': 'Active'   # Current status of book issues
            }
            print(f"Student {name} with registration number {reg_number} added successfully.")
        else:
            print(f"Student with registration number {reg_number} already exists.")

    def add_book(self, book_id, title, author, pub_year, buying_year):
        """Add a new book to the database."""
        if book_id not in self.books:
            self.books[book_id] = {
                'title': title,
                'author': author,
                'publication_year': pub_year,
                'buying_year': buying_year,
                'times_issued': 0  # Number of times issued (initially zero)
            }
            print(f"Book '{title}' by {author} added successfully with ID {book_id}.")
        else:
            print(f"Book with ID {book_id} already exists.")

    def issue_book(self, reg_number, book_id):
        """Allow a student to issue a book."""
        if reg_number in self.students and book_id in self.books:
            if self.students[reg_number]['status'] == 'Active':
                if self.books[book_id]['times_issued'] < 2:  # Max two times issue limit per book
                    self.students[reg_number]['history'].append({
                        'book_id': book_id,
                        'issue_date': 'today',  # Placeholder for actual issue date
                    })
                    self.books[book_id]['times_issued'] += 1
                    print(f"Book '{self.books[book_id]['title']}' issued to {self.students[reg_number]['name']} successfully.")
                else:
                    print(f"Book '{self.books[book_id]['title']}' has already been issued twice and cannot be issued further.")
            else:
                print(f"Student {self.students[reg_number]['name']} cannot issue books due to their status ({self.students[reg_number]['status']}).")
        else:
            print("Invalid student registration number or book ID.")

    def return_book(self, reg_number, book_id):
        """Allow a student to return a book."""
        if reg_number in self.students and book_id in self.books:
            for issue in self.students[reg_number]['history']:
                if issue['book_id'] == book_id:
                    self.students[reg_number]['history'].remove(issue)
                    self.books[book_id]['times_issued'] -= 1
                    print(f"Book '{self.books[book_id]['title']}' returned by {self.students[reg_number]['name']} successfully.")
                    break
            else:
                print(f"Student {self.students[reg_number]['name']} did not issue this book.")
        else:
            print("Invalid student registration number or book ID.")

    def display_student_details(self, reg_number):
        """Display details of a specific student."""
        if reg_number in self.students:
            student = self.students[reg_number]
            print(f"Name: {student['name']}")
            print(f"Registration Number: {reg_number}")
            print("Book Issue History:")
            for issue in student['history']:
                book_title = self.books[issue['book_id']]['title']
                issue_date = issue['issue_date']
                print(f"- Book: '{book_title}', Issue Date: {issue_date}")
            print(f"Fine Amount: {student['fine_amount']}")
            print(f"Status: {student['status']}")
        else:
            print("Student not found.")

    def display_book_details(self, book_id):
        """Display details of a specific book."""
        if book_id in self.books:
            book = self.books[book_id]
            print(f"Title: '{book['title']}'")
            print(f"Author: {book['author']}")
            print(f"Publication Year: {book['publication_year']}")
            print(f"Buying Year: {book['buying_year']}")
            print(f"Number of Times Issued: {book['times_issued']}")
        else:
            print("Book not found.")


# Example usage:
library_system = LibraryManagementSystem()

# Adding students
library_system.add_student(1001, "Alice")
library_system.add_student(1002, "Bob")

# Adding books
library_system.add_book(2001, "Introduction to Python", "John Smith", 2020, 2021)
library_system.add_book(2002, "Data Structures and Algorithms", "Jane Doe", 2019, 2020)

# Issuing books
library_system.issue_book(1001, 2001)
library_system.issue_book(1002, 2002)

# Displaying student and book details
library_system.display_student_details(1001)
library_system.display_student_details(1002)
library_system.display_book_details(2001)
library_system.display_book_details(2002)

# Returning a book
library_system.return_book(1001, 2001)
library_system.display_book_details(2001)
