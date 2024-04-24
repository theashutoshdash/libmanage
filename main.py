import csv
import re

class LibraryManagementSystem:
    def __init__(self):
        self.students = {}
        self.books = {}
        self.filename = "library_data.csv"  

    def add_student(self, reg, name):
        if reg not in self.students:
            self.students[reg] = {
                'name': name,
                'history': [],
                'fine_amount': 0.0,
                'status': 'Active'
            }
            print(f"Student {name} with registration number {reg} added successfully.")
            self.write_data_to_csv()
        else:
            print(f"Student with registration number {reg} already exists.")

    def add_book(self, book_id, title, author, pub_year, buying_year):
        if book_id not in self.books:
            self.books[book_id] = {
                'title': title,
                'author': author,
                'publication_year': pub_year,
                'buying_year': buying_year,
                'times_issued': 0
            }
            print(f"Book '{title}' by {author} added successfully with ID {book_id}.")
            self.write_data_to_csv()
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
                    self.write_data_to_csv()
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
                    self.write_data_to_csv()
                    break
            else:
                print(f"Student {self.students[reg_number]['name']} did not issue this book.")
        else:
            print("Invalid student registration number or book ID.")

    def write_data_to_csv(self):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Registration Number', 'Name', 'Status', 'Fine Amount'])
            for reg_number, details in self.students.items():
                writer.writerow([reg_number, details['name'], details['status'], details['fine_amount']])
            
            writer.writerow(['Book ID', 'Title', 'Author', 'Times Issued'])
            for book_id, details in self.books.items():
                writer.writerow([book_id, details['title'], details['author'], details['times_issued']])

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

    def display_book_details(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            print(f"Title: '{book['title']}'")
            print(f"Author: {book['author']}")
            print(f"Publication Year: {book['publication_year']}")
            print(f"Buying Year: {book['buying_year']}")
            print(f"Number of Times Issued: {book['times_issued']}")
        else:
            print("Book not found.")
    
    def signup_or_login(self, name, reg_number):
        if reg_number in self.students:
            if self.students[reg_number]['name'] == name:
                print(f"Login successful. Welcome, {name}!")
                self.stu_page()
            else:
                print("Invalid credentials. Login failed.")
        else:
            print("Account does not exist \nSignup")
            self.signup()
    def login(self):
        selector=True
        print("Select affiliation")
        print("1) Student")
        print("2) Employee")
        while(selector):
            try:
                aff=int(input("Enter choice : "))
                if(aff==1):
                    nu=input("Username: ")
                    re=input("Password: ")
                    self.signup_or_login(nu,re)
                    selector=False
                elif(aff==2):
                    self.emp_page()
                    selector=False
                else:
                    print("Enter valid value")
            except :
                print("Enter Integer Value") 
    def signup(self):
        regx=True
        name=str(input("Enter Name : "))
        while(regx):
            reg=str(input("Enter Registration Number : "))
            if(re.match('[1-2][0-9][A-Za-z]{3}[0-9]{4}',reg)):
                if(int(reg[-4:])>0):
                    self.add_student(reg, name)
                    print("Successful Registration!")
                    self.stu_page()                                      
            if(regx):
                print("Invalid Registration Number")
    def stu_page(self):
        selector=True
        while(selector):
            print('Welcome to VIT Central Library')
            print("1) Issue\n2) Search\n3) Return\n4) Fine Payment\n5) Exit")
            try:
                ch=int(input("Enter choice : "))
                if(ch==1):
                    pass
                    self.issue_book()                                          
                elif(ch==2):
                    pass
                    self.search()                                        
                elif(ch==3):
                    self.book_return()
                    pass                                         
                elif(ch==4):
                    self.fine_payment()
                    pass                                        
                elif(ch==5):
                    selector=False
                    self.login()
                else:
                    print("\nEnter valid choice (Between 1 and 5)\n")
            except :
                print("\nEnter Integer Value\n") 
    def emp_page(self):
        selector=True
        while(selector):
            print("Enter Choice")
            print("1) Add Book")
            print("2) Exit")
            try:
                aff=int(input("Enter choice : "))
                if(aff==1):
                    title=str(input("Title : "))
                    author=str(input("Author : "))
                    bookid=str(input("Book ID : "))
                    pub_yr=int(input("Publishing Year : "))
                    buy_yr=int(input("Buying Year : "))
                    self.add_book(bookid,title,author,pub_yr,buy_yr)                                      
                    pass
                elif(aff==2):
                    selector=False
                    self.login()
                else:
                    print("\nEnter valid choice (1 or 2)\n")
            except :
                print("\nEnter Integer Value\n") 


lib=LibraryManagementSystem()
k="Periyar EVR Library"
print(k.center(60,'='))
lib.login()


