import csv
import re

class LibraryManagementSystem:
    def __init__(self):
        self.students = {}
        self.books = {}
        self.student_filename = "students.csv"
        self.book_filename = "books.csv"

        # Load existing student data from CSV
        self.load_students_from_csv()

        # Load existing book data from CSV
        self.load_books_from_csv()

    def load_students_from_csv(self):
        try:
            with open(self.student_filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.students[row['Registration Number']] = {
                        'name': row['Name'],
                        'status': row['Status'],
                        'fine_amount': float(row['Fine Amount']),
                        'history': []  # Initialize history list
                    }
        except FileNotFoundError:
            # File does not exist yet, will be created when writing data
            pass

    def load_books_from_csv(self):
        try:
            with open(self.book_filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.books[row['Book ID']] = {
                        'title': row['Title'],
                        'author': row['Author'],
                        'times_issued': int(row['Times Issued'])
                    }
        except FileNotFoundError:
            # File does not exist yet, will be created when writing data
            pass
    def stu_page(self):
        selector = True
        while selector:
            print('Welcome to VIT Central Library')
            print("1) Issue\n2) Search\n3) Return\n4) Fine Payment\n5) Dashboard\n6) Exit\n")
            try:
                ch = int(input("Enter choice : "))
                if ch == 1:
                    reg_number = input("Enter Registration Number: ")
                    book_id = input("Enter Book ID: ")
                    self.issue_book(reg_number, book_id)
                elif ch == 2:
                    self.search_book()
                    pass
                elif ch == 3:
                    reg_number = input("Enter Registration Number: ")
                    book_id = input("Enter Book ID: ")
                    self.return_book(reg_number, book_id)
                elif ch == 4:
                    self.fine_payment()
                    pass
                elif ch == 5:
                    reg_number = input("Enter Registration Number: ")
                    self.display_student_details(reg_number)
                elif ch == 6:
                    selector = False
                else:
                    print("\nEnter valid choice (Between 1 and 6)\n")
            except ValueError:
                print("\nEnter Integer Value\n")

    def emp_page(self):
        selector = True
        while selector:
            print("Welcome to VIT Central Library - Employee Panel")
            print("1) Add Book")
            print("2) Update Shelf")
            print("3) Exit\n")
            try:
                aff = int(input("Enter choice : "))
                if aff == 1:
                    book_id = input("Enter Book ID: ")
                    title = input("Enter Title: ")
                    author = input("Enter Author: ")
                    self.add_book(book_id, title, author)
                elif aff == 2:
                    # Implement shelf update
                    pass
                elif aff == 3:
                    selector = False
                else:
                    print("\nEnter valid choice (1-3)\n")
            except ValueError:
                print("\nEnter Integer Value\n")

    def write_students_to_csv(self):
        with open(self.student_filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Registration Number', 'Name', 'Status', 'Fine Amount'])
            for reg_number, details in self.students.items():
                writer.writerow([reg_number, details['name'], details['status'], details['fine_amount']])

    def write_books_to_csv(self):
        with open(self.book_filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Book ID', 'Title', 'Author', 'Times Issued'])
            for book_id, details in self.books.items():
                writer.writerow([book_id, details['title'], details['author'], details['times_issued']])

    def add_student(self, reg, name):
        if reg not in self.students:
            self.students[reg] = {
                'name': name,
                'status': 'Active',
                'fine_amount': 0.0,
                'history': []  # Initialize history list
            }
            print(f"Student {name} with registration number {reg} added successfully.")
            self.write_students_to_csv()
        else:
            print(f"Student with registration number {reg} already exists.")

    def add_book(self, book_id, title, author):
        if book_id not in self.books:
            self.books[book_id] = {
                'title': title,
                'author': author,
                'times_issued': 0
            }
            print(f"Book '{title}' by {author} added successfully with ID {book_id}.")
            self.write_books_to_csv()
        else:
            print(f"Book with ID {book_id} already exists.")

    def issue_book(self, reg_number, book_id):
        if reg_number in self.students and book_id in self.books:
            if self.students[reg_number]['status'] == 'Active':
                if self.books[book_id]['times_issued'] < 2:
                    self.students[reg_number]['history'].append({
                        'book_id': book_id,
                        'issue_date': 'today',
                    })
                    self.books[book_id]['times_issued'] += 1
                    print(f"Book '{self.books[book_id]['title']}' issued to {self.students[reg_number]['name']} successfully.")
                    self.write_students_to_csv()  # Update student data
                    self.write_books_to_csv()     # Update book data
                else:
                    print(f"Book '{self.books[book_id]['title']}' has already been issued twice and cannot be issued further.")
            else:
                print(f"Student {self.students[reg_number]['name']} cannot issue books due to their status ({self.students[reg_number]['status']}).")
        else:
            print("Invalid student registration number or book ID.")

    def return_book(self, reg_number, book_id):
        if reg_number in self.students and book_id in self.books:
            for issue in self.students[reg_number]['history']:
                if issue['book_id'] == book_id:
                    self.students[reg_number]['history'].remove(issue)
                    self.books[book_id]['times_issued'] -= 1
                    print(f"Book '{self.books[book_id]['title']}' returned by {self.students[reg_number]['name']} successfully.")
                    self.write_students_to_csv()  # Update student data
                    self.write_books_to_csv()     # Update book data
                    break
            else:
                print(f"Student {self.students[reg_number]['name']} did not issue this book.")
        else:
            print("Invalid student registration number or book ID.")

    def display_student_details(self, reg_number):
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
            
    def signup_or_login(self, name, reg_number):
        if reg_number in self.students:
            if self.students[reg_number]['name'] == name:
                print(f"Login successful. Welcome, {name}!")
                self.stu_page()
            else:
                print("Invalid credentials. Login failed.")
        else:
            self.add_student(reg_number, name)
            print(f"Signup successful. Welcome, {name}!")

    def login(self):
        selector = True
        print("Select affiliation")
        print("1) Student")
        print("2) Employee")
        while selector:
            try:
                aff = int(input("Enter choice : "))
                if aff == 1:
                    nu = input("Username: ")
                    re = input("Password: ")
                    self.signup_or_login(nu, re)
                    selector = False
                elif aff == 2:
                    self.emp_page()
                else:
                    print("Enter valid value")
            except ValueError:
                print("Enter Integer Value")

    def signup(self):
        regx = True
        name = str(input("Enter Name : "))
        while regx:
            reg = str(input("Enter Registration Number : "))
            if re.match('[1-2][0-9][A-Za-z]{3}[0-9]{4}', reg):
                if int(reg[-4:]) > 0:
                    self.add_student(reg, name)
                    regx = False
                else:
                    print("Invalid Registration Number")
    def search_book(self, query):
        found_books = []
        query = query.lower()  # Convert query to lowercase for case-insensitive search

        for book_id, details in self.books.items():
            title = details['title'].lower()
            author = details['author'].lower()

            if query in title or query in author:
                found_books.append((book_id, details['title'], details['author']))

        if found_books:
            print("Search Results:")
            for book_id, title, author in found_books:
                print(f"Book ID: {book_id}, Title: '{title}', Author: {author}")
        else:
            print("No books found matching the search query.")
    def fine_payment(self, reg_number, amount):
        if reg_number in self.students:
            if amount > 0:
                self.students[reg_number]['fine_amount'] -= amount
                if self.students[reg_number]['fine_amount'] < 0:
                    self.students[reg_number]['fine_amount'] = 0
                print(f"Fine payment of ${amount} successful.")
                self.write_students_to_csv()  # Update student data
            else:
                print("Invalid payment amount. Payment should be greater than zero.")
        else:
            print("Student not found.")

    

# Example usage
lib = LibraryManagementSystem()
k = "Periyar EVR Library"
print(k.center(60, '='))
lib.login()
