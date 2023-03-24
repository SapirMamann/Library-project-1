from books import Book
from customers import Customer
from loans import Loan

from datetime import date, datetime, timedelta
from dateutil import parser
from tabulate import tabulate


def add_customer(cust_list):                            
    while True:                         #validation for customer id. has to be 9 digits
        customer_id = input("Please enter a 9 digits customer ID, enter 0 to exit: ")
        if len(customer_id) == 9 and customer_id.isnumeric():                           
            break
        if customer_id == '0':                          #in order to get out of this function, press 0
            return cust_list           
        print(f"'{customer_id}' is not a valid id")      

    for customer in cust_list:                         #check if a customer doesnt already exist
        if customer_id == customer.get_id():                                
            print('Customer already exists')
            return cust_list

    while True:                         #validation for customer name. has to contain alphabet characters only
        customer_name = input("Please enter customer's name: ") 
        customer_name = customer_name.title()
        if customer_name.replace(' ','').isalpha():

            break
        print('Name can only contain alphabet characters')

    while True:                         #validation for customer city. has to contain alphabet characters only
        customer_city = input('Please enter city: ')
        customer_city = customer_city.title()
        if customer_city.replace(' ','').isalpha():
            break
        print('City can only contain alphabet characters')

    while True:                         #validation for customer age. has to be a digit. positive, and under 120.
        customer_age = input('Please enter age: ')
        if customer_age.isnumeric() and int(customer_age) < 120 :
            break
        print(f"Age '{customer_age}' is not valid")

    print(f"Welcome, {customer_name}!")                         #confirmation message
    new_cust = Customer(customer_id, customer_name, customer_city, customer_age)                           #creating a proper instance for the Customer class
    cust_list.append(new_cust)                         #adding the current customer (instance) to the list (cust_list) 
    return cust_list                            #returning the updated list


def add_book(books_list):                 
    while True:                         #validation for book attributes
        book_id = input("Please enter a 5 digits book ID, enter 0 to exit: ")
        if len(book_id) == 5 and book_id.isnumeric():    
            break                      
        if book_id == '0':                          #in order to get out of this function, press 0
            return books_list
        print(f"'{book_id}' is not a valid ID") 
    for book in books_list:                         #making sure book (based on id) isnt already exists
        if book_id == book.get_book_id():
            print('book already exists')
            return books_list

    while True:                         #validation for name, name can only contain alphabet characters
        book_name = input("Please enter book's name: ")   
        book_name = book_name.title()                     
        if book_name.replace(' ','').isalpha():
            break
        print('Name can only contain alphabet characters')

    for book in books_list:                         #making sure book name doesnt already exists on the library
        if book_name == book.get_book_name():
            print('Book name already exists')
            return books_list

    while True:                         #validation for name. author name can only contain alphabet characters
        book_author = input("Please enter book's author name: ")
        book_author = book_author.title()
        if book_author.replace(' ','').isalpha():
            break
        print('Author name can only contain alphabet characters')

    while True:                         #year should make sense (positive number, not a futured year, not alphabetic characters, not under 1450)
        year_published = input("Please enter book's published year: ")
        if year_published.isnumeric():
            if (int(year_published) <= date.today().year) and (int(year_published) > 1450):
                break
        print(f'{year_published} is not a valid year')            

    while True:                         #validation + setting of the book's type
        book_type = input("Please enter book's type (1/2/3): ")
        if book_type == '1' or book_type == '2' or book_type == '3':
            break
        print(f"Book type '{book_type}' is not a valid type")

    while True:                         #validation for book's copies number
        book_copies = input("Enter copies amount: ")
        if (book_copies.isnumeric()) and (int(book_copies) >= 1):
            break
        print(f"{book_copies} is not an option !")

    print(f"'{book_name}' written by {book_author} was successfully added to the library!")                         #confirmation message
    new_book = Book(book_id, book_name, book_author, year_published ,book_type, book_copies)                         #creating a proper instance for the Book class 
    books_list.append(new_book)                         #adding the instance to the end of the books list
    return books_list                           #returning the updated books list


def loan_book(cust_list, books_list, loans_list):
    customer_found = 0                          #flag 
    book_found = 0                           #flag

    while True:                         #validation for customer's id
        customer_loan = input("Please enter a 9 digits customer ID, enter 0 to exit: ")                         #validation for attributes that will go into the Loan class
        if len(customer_loan) == 9 and customer_loan.isnumeric():                           
            break
        if customer_loan == '0':                          #in order to get out of this function, press 0
            return loans_list           
        print(f"'{customer_loan}' is not a valid ID")      

    while True:                         #validation for book id (has to contain 5 digits)
        book_loan = input('Please enter a 5 digits book ID: ')
        if len(book_loan) == 5 and book_loan.isnumeric():    
            break                       
        print(f"'{book_loan}' is not a valid book ID")

    loan_date = date.today()                            #setting the return date of the specific book (based on today's date and the book's type)
    
    for customer in cust_list:                          #making sure a customer is a member, and the book exists
        if customer_loan == customer.get_id():                          #if customer exists -> continue
            customer_found = 1                          #raise the flag (customer found)
            for book in books_list: 
                if book_loan == book.get_book_id():                          #if book exists ->  continue
                    book_type = book.get_book_type()
                    book_found = 1                          #raise the flag (book found)
                    if int(book.get_book_copies_n()) >= 1:                          #if customer_found == 1 and book_found == 1:   -> allowed to continue
                        update_copies_num = int(book.get_book_copies_n()) -1                            #reduce copies number by one. 
                        book.update_copies(update_copies_num)                           #set the updated copies number
                        if book_type == '1':                            #setting the return date of the book based on its type
                            return_date = loan_date + timedelta(days = 10)
                        elif book_type == '2':
                            return_date = loan_date + timedelta(days = 5)
                        else:                           #elif book_type == '3': 
                            return_date = loan_date + timedelta(days = 2)
                        print('Book succesfully loaned')                            #confirmation message
                        new_loan = Loan(customer_loan, book_loan, loan_date, return_date)                           #making a proper instance of the Loan class
                        loans_list.append(new_loan)                         #and adding the instance to the end of the list
                        return loans_list  
                    else:                           #there arent enough copies to borrow
                        print('All copies of this book are already loaned')
                    break

    if customer_found == 0 or book_found == 0:                         #customer/ book doesn't exist -> will return the latest version of the loans list
        print('customer/ book was not found')
        return loans_list 
    

def return_book(loans_list, books_list):  
    while True:                             #validation for book id
        book_id = input("Please enter book ID (5 digits), enter 0 to exit: ")
        if len(book_id) == 5 and book_id.isnumeric():    
            break                       
        if book_id == '0':                          #in order to get out of this function, press 0
            return loans_list
        print("Please enter a valid book ID")

    while True:                         #validation for customer id
        customer_id = input("Please enter customer ID, enter 0 to exit: ")
        if len(customer_id) == 9 and customer_id.isnumeric():                           
            break
        if customer_id == '0':                          #in order to get out of this function, press 0
            return loans_list           
        print('This is not a valid ID') 

    for loan in loans_list:                         #making sure the book is a loaned book  
        if (book_id == loan.get_loan_book_id()) and (customer_id == loan.get_loan_cust_id()):
            loans_list.remove(loan)                         #theres a (book id- customer id) match. Loan is removed from loans list
            for book in books_list:
                if book_id == book.get_book_id():                           #updating the books list. theres one more avialable copy of this book.
                    update_copies_num = int(book.get_book_copies_n()) +1
                    book.update_copies(update_copies_num)
                    print(f"Book was successfully returned")                            #confirmation message
                    return loans_list

    print("Couldn't return book. This combination doesn't exist")                          #customer/ book combination wasnt found
    return loans_list
    

def display_books(books_list):
    table_list = []                         # Creating a new list. tabulate can only accept a list of lists.
    for book in books_list:                         #looping through objects in books list
        id, name, author, year_p, type, copies = book.get_book_atr()                     #setting 6 variables
        obj = [id, name, author, year_p, type, copies]                          #entering the variables into an list
        table_list.append(obj)                          #entering the list into the table_list. (creating list of lists)
    print(tabulate(table_list, headers=['ID', 'Name', 'Author', 'Year of publishment', 'Type', 'Copies'], tablefmt = 'rounded_grid', showindex = 'always'))


def display_customers(cust_list):
    table_list = []                         #same as above
    for customer in cust_list:
        id, name, city, age = customer.get_cust_atr()
        obj = [id, name, city, age]
        table_list.append(obj)
    print(tabulate(table_list, headers= ['ID', 'Name', 'City', 'Age'], tablefmt = 'rounded_grid', showindex = 'always'))


def display_loans(loans_list):
    loan_flag = 0                           #flag

    table_list = []                         #same as above
    for loan in loans_list:
        loan_flag = 1                           #raise flag
        cust_id, book_id, loan_date, return_date = loan.get_loan_atr()
        obj = [cust_id, book_id, loan_date, return_date]
        table_list.append(obj)

    if loan_flag == 0:                          #there are no loans
        print("There are no loans to display")
        return loans_list

    print(tabulate(table_list, headers = ['Customer ID', 'Book ID', 'Loan date', 'Return date'], tablefmt = 'rounded_grid', showindex = 'always'))


def display_late_loans(loans_list):  
    late_loan_flag = 0                          #flag     

    table_list = []
    for loan in loans_list:                         #looping through returning dates, checking whether the date has passed
        date_check = parser.parse(loan.get_return_date())
        today = datetime.today()
        if today > date_check:                          #if the return date of the book passed -> 
            late_loan_flag = 1                          #raise flag
            Customer_id, Book_id, Loan_date, Return_date = loan.get_loan_atr()                          
            obj = [Customer_id, Book_id, Loan_date, Return_date]
            table_list.append(obj)                          #append the book to the table_list (which will be later displayed)

    if late_loan_flag == 0:                         #no late loans were detected
        print('There are no late loans to display')
        return loans_list

    print(tabulate(table_list, headers = ['customer_id', 'book_id', 'loan_date', 'return_date'], tablefmt = 'rounded_grid', showindex = 'always'))


def book_by_name(books_list):
    book_flag = 0                           #flag

    while True:                         #validation for book's name input
        search = input("Please enter book's name, enter 0 to exit: ")
        search = search.title()
        if search.replace(' ','').isalpha():
            break
        if search == '0':                              #'0' to exit
            return books_list
        print("Book's name can only contain alphabet characters")

    table_list = []
    for book in books_list:                         #returns the wanted book's details   
        wanted_book_name = book.get_book_name()
        if search in wanted_book_name:
            book_flag = 1
            id, name, author, year_p, type, copies = book.get_book_atr()
            obj = [id, name, author, year_p, type, copies]
            table_list.append(obj)
            
    if book_flag == 0:
        print('Book wasnt found')

    if book_flag == 1:
        print(tabulate(table_list, headers= ['ID', 'Name', 'Author', 'Year of publishment', 'Type', 'Copies'], tablefmt = 'rounded_grid', showindex = 'always'))   


def customer_by_name(cust_list):
    cust_flag = 0                           #flag

    while True:                         #validation for customer's name input
        search = input("Please enter customer's name, enter 0 to exit: ")
        search = search.title() 
        if search.replace(' ','').isalpha():
            break
        if search == '0':                              #'0' to exit
            return cust_list
        print("Customer's name can only contain alphabet characters")
        
    table_list = []
    for customer in cust_list:                          #returning the wanted customer's details
        wanted_customer_name = customer.get_name()                           #the wanted customer's name
        if search in wanted_customer_name:                          
            cust_flag = 1
            id, name, city, age = customer.get_cust_atr()
            obj = [id, name, city, age]
            table_list.append(obj)
    
    if cust_flag == 0:
        print('Customer wasnt found')                          

    if cust_flag == 1:
        print(tabulate(table_list, headers= ['ID', 'Name', 'City', 'Age'], tablefmt = 'rounded_grid', showindex = 'always'))


def remove_book(books_list, loans_list):                            #before removing a book, make sure its not loaned by any customer
    book_flag = 0
    while True:                         #validation for user's input
        to_remove = input("Enter book ID, enter 0 to exit: ")
        if len(to_remove) == 5 and to_remove.isnumeric():
            break
        if to_remove == '0':                            #'0' to exit
            return books_list
        print('please enter a valid book ID')

    for loan in loans_list:                         #check if the book is not loaned by any customer
        if to_remove == loan.get_loan_book_id():
            print('Unable to remove book.\nThe book is loaned by customer/s')
            return books_list

    for book in books_list:                         #removing the book
        if to_remove == book.get_book_id():
            book_flag = 1
            book_name = book.get_book_name()
            books_list.remove(book)
            print(f"'{book_name}' successfully removed from books")
            break

    if book_flag == 0:
        print('there are no books in the library')

    return books_list


def remove_customer(cust_list, loans_list):                         #before removing a customer, make sure he returned all loaned books
    cust_flag = 0                           #flag

    while True:                         #validation for user's input
        to_remove = input("Enter customer ID, enter 0 to exit: ")  
        if len(to_remove) == 9 and to_remove.isnumeric():
            break
        if to_remove == '0':                            #'0' to exit
            return cust_list
        print('Please enter a valid ID')

    for loan in loans_list:                         #check if customer returned all books
        if to_remove == loan.get_loan_cust_id():
            print(f'Customer has loaned books.\nReturn books before removing customer')
            return cust_list

    for customer in cust_list:                      #removing the customer from the list
        if to_remove == customer.get_id():
            cust_flag = 1
            cust_name = customer.get_name()
            cust_list.remove(customer)
            print(f"{cust_name} successfully removed from members")
            break
    
    if cust_flag == 0:
        print('There are no customers that are members')

    return cust_list
