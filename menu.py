
import re
def login():
    selector=True
    print("Select affiliation")
    print("1) Student")
    print("2) Employee")
    while(selector):
        try:
            aff=int(input("Enter choice : "))
            if(aff==1):
                #student_login()                                          function insert
                selector=False
            elif(aff==2):
                #employee_login()                                          function insert
                selector=False
            else:
                print("Enter valid value")
        except :
            print("Enter Integer Value") 
def signup():
    regx=True
    name=str(input("Enter Name : "))
    while(regx):
        reg=str(input("Enter Registration Number : "))
        if(re.match('[1-2][0-9][A-Za-z]{3}[0-9]{4}',reg)):
            if(int(reg[-4:])>0):
                #add_student(reg,name.upper())                                          function insert
                regx=False
        if(regx):
            print("Invalid Registration Number")
def stu_page():
    selector=True
    while(selector):
        print("Welcome to VIT Central Library")
        print("1) Issue\n2) Search\n3) Return\n4) Fine Payment\n5) Exit")
        try:
            ch=int(input("Enter choice : "))
            if(ch==1):
                pass
                #issue()                                          function insert
            elif(ch==2):
                pass
                #search()                                         function insert
            elif(ch==3):
                pass#book_return()                                         function insert
            elif(ch==4):
                pass#fine_payment()                                         function insert
            elif(ch==5):
                selector=False
            else:
                print("\nEnter valid choice (Between 1 and 4)\n")
        except :
            print("\nEnter Integer Value\n") 
def emp_page():
    selector=True
    while(selector):
        print("Enter Choice")
        print("1) Add Book")
        print("2) Update Shelf")
        print("3) Exit")
        try:
            aff=int(input("Enter choice : "))
            if(aff==1):
                #add_book()                                      insert function and remove pass
                pass
            elif(aff==2):
                #update_shelf()                                      insert function and remove pass
                pass
            elif(aff==3):
                selector=False
            else:
                print("\nEnter valid choice (1-3)\n")
        except :
            print("\nEnter Integer Value\n") 
