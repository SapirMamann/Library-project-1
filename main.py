'''this is the menu,                                                                                                                                                 בס"ד 
the librarian would be able to choose what to do


>>>>>>>>>>>>  ELIAV - Things to notice before running the code:  <<<<<<<<<<<<
customer id is a 9 digits number,
accepting ALL ages under 120,
book id is a 5 digits number,
year of book publishment cant be under 1450,
book name is uniqe (cant name 2 books the same),
book name cant contain digits,
customer is allowed to loan the same book for as many times as he wants,
i wanted to keep the try module as an appendix :)
i hope i didnt forgot anything
'''

import m_functions
from customers import Customer
from books import Book
from loans import Loan

#converting files into lists
with open ('customers.txt', 'r+') as cust_f, open ('books.txt', 'r+') as books_f, open ('loans.txt', 'r+') as loans_f:
    cust_str_list = cust_f.readlines()                          
    books_str_list = books_f.readlines()
    loans_str_list = loans_f.readlines()
    cust_list = []
    books_list = []
    loans_list = []

    #converting every item on the list -> to an object
    for line in cust_str_list:
        if line.startswith('Id'):
            pass
        else:
            cust_id, cust_name, cust_city, cust_age = line.split(',')
            cust_age = cust_age.strip()                         #(removes the \n in the latest variable)
            cust = Customer(cust_id, cust_name, cust_city, cust_age)
            cust_list.append(cust)

    for line in books_str_list:
        if line.startswith('Id'):
            pass
        else:
            book_id, book_name, book_author, book_year, book_type, book_copies = line.split(',')
            book_copies = book_copies.strip()
            book = Book(book_id, book_name, book_author, book_year, book_type, book_copies)
            books_list.append(book)
    
    for line in loans_str_list:
        if line.startswith('Customer'):
            pass
        else:
            Customer_id, Book_id, Loan_date, Return_date = line.split(',')
            Return_date = Return_date.strip()                          
            loan = Loan(Customer_id, Book_id, Loan_date, Return_date)
            loans_list.append(loan)
    
    #displaying the menu until 'x' is entered
    ans = True
    while ans:  
        print("""
        1. Add a new customer
        2. Add a new book
        3. Loan a book
        4. Return a book
        5. Display all books
        6. Display all customers
        7. Display all loans
        8. Display late loans
        9. Find book by name
        10. Find customer by name
        11. Remove a book
        12. Remove a customer
        x for exit
        """)
        ans = input('What would you like to do? ')
        if ans == '1':
            'Add a new customer'
            cust_list = m_functions.add_customer(cust_list)

        elif ans == '2':
            'Add a new book'
            books_list = m_functions.add_book(books_list)
            
        elif ans == '3':
            'Loan a book'
            loans_list = m_functions.loan_book(cust_list, books_list, loans_list)
            
        elif ans == '4':
            'Return a book'
            loans_list = m_functions.return_book(loans_list, books_list)
 
        elif ans == '5':
            'Display all books'
            m_functions.display_books(books_list)

        elif ans == '6':
            'Display all customers'
            m_functions.display_customers(cust_list)

        elif ans == '7':
            'Display all loans'
            m_functions.display_loans(loans_list)

        elif ans == '8':
            'Display late loans'
            m_functions.display_late_loans(loans_list)

        elif ans == '9':
            'Find book by name'
            m_functions.book_by_name(books_list)
            
        elif ans == '10':
            'Find customer by name'
            m_functions.customer_by_name(cust_list)
            
        elif ans == '11':
            'Remove a book'
            books_list = m_functions.remove_book(books_list, loans_list)

        elif ans == '12':
            'Remove a customer'
            cust_list = m_functions.remove_customer(cust_list, loans_list)

        elif ans == ('x' or 'X'):
            break

        else:
            print(f"\nSorry, {ans} is not a valid choice,\nplease enter a choice between 1 to 12") 
            
    # after 'x' entered -> rewrite the files        
    cust_f.seek(0)                          #set the file's position to top left corner
    cust_f.truncate(0)                          #deletes the file
    cust_f.write('Id, Name, City, Age\n')                           #first, write the headers on the file
    for customer in cust_list:                          #then, looping through cust_list, write the customers.
        print(customer, file = cust_f)                          #(whenever printing an object it uses the str method)
        
    books_f.seek(0)                         #as above
    books_f.truncate(0)
    books_f.write('Id, Name, Author, Year Published, Type, Copies\n')
    for book in books_list:
        print(book, file = books_f)          

    loans_f.seek(0)                         #as above
    loans_f.truncate(0)   
    loans_f.write('Customer id, Book id, Loan date, Return date\n')
    for loan in loans_list:
        print(loan, file = loans_f)
