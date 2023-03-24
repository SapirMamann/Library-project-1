'''im testing things in here'''

# # new = input('enter id please: ')

# # while new.isnumeric() is False:
# #     print('please enter numbers only')
# #     new = (input('enter id please: '))
# # print(f' id is {new}')

# x = input('enter name: ')
# while x.isdigit():
#     print('not good')
#     x = input('enter again:')

# y = x
# print(y)

# from datetime import date
# y = input('enter year plaese: ')
# while (int(y) > (date.today().year)) or (int(y) < 1950):
#     print('year can not be a future year')
#     y = input('enter valid year: ')

# print(f' year {y} is okayyyzzzzzzzzz')

# customer_id2 = '209680968'
# input('enter id: ')
# with open ('customers.txt', 'r+') as filee:
#     for line in filee.readlines():
#         if line.startswith('Id'):
#             continue
#         # print(line[0:line.find(',')])
#         elif (customer_id2) == (line.split(',')[0]):
#             print('customer is already exists')
#             break
#         else:
#             # with open ('customer.txt', 'a'):
#                 filee.write(f'\n{customer_id2}')
# # 
                        # cust_f.write(f'\n{self.__id}, {self.__name}, {self.__city}, {self.__age}')


#this was the old add customer:  <<<<>>>>>
            # def add_customer():
            #         '''calls the Customers class in order to create a new customer,

            #         when the librarian press 1(t ==1)- this function start working,
            #         with open customers.txt, loop through ids and make sure it doesnt already exist,
            #         maybe to have a list of ids from the customers txt
            #         before i add a new customer ill make sure his id is not on the customers txt
            #         '''
            #         from customers import Customer
            #         new_c = Customer()                                                           #should this be in the main?
            #         new_c.set_id((input('Enter id please: ')))
            #         while not id.isnumeric():
            #             print('please enter valid id')
            #             id = input('enter id:')
            #         new_c.set_name(input('Enter name please: '))
            #         new_c.set_city(input('Enter city please: '))
            #         new_c.set_age(input('Enter age please: '))
            #         new_c.__str__()
            #         # verify_cust = input('enter y to change something')
            #         # if verify_cust == 'y':
            #         new_c.add_to_file()

# with open ('customers.txt', 'r+') as cf:
#     str = cf.readlines()
#     print(str) 
# def add__sm(cust_list):
#     for cust in cust_list:
#         print (cust)

# while True:
#     name = input('enter shit: ')
#     if  name.isalpha():
#         break

# while True:
#     book_type = input("Please enter book's type (1/2/3): ")
#     if book_type == '1' or book_type == '2' or book_type == '3':
#         break
#     print(f"book type '{book_type}' is not a valid type")
# print(book_type)
# while True:
#         customer_age = input('Please enter age: ')
#         if customer_age.isnumeric() and int(customer_age)<110 :
#             #and customer_age<110
#             break
#         print(f"Age '{customer_age}' is not valid")

# def loan_book(cust_list, books_list, loans_list):
#     customer_found = 0                          #flag 
#     book_found = 0                          #flag
#     customer_loan = input('Please enter id, press 0 to exit: ')                         #validation for attributes that will go into the Loan class
#     for customer in cust_list:
#         if customer_loan == customer.get_id():                          #if customer exists -> continue
#             customer_found = 1
#             book_loan = input('Please enter book id: ')             
#             for book in books_list: 
#                 if book_loan == book.get_id():                          #if book exists ->  continue
#                     book_found = 1
# customer_found = input('here: ')
# book_found = input('here: ')

# if customer_found == '0' or book_found== '0' :                         #customer doesnt exist -> will return the latest version of the loans list
#     print('customer doesnt exist')
#     print('1')
# if book_found == '0':                         #book doesnt exist -> will return the latest version of the loans list
#     print ('njjkn')  
#     print('2')
# from datetime import date, timedelta
# loan_date = date.today()
# print(loan_date)


# while True:
#     book_type = input('Please enter book type: ')
#     if book_type == '1' or book_type == '2' or book_type == '3':
#         print('okkkkkkkkkkk')
#         break

#     print('thats bad')

# return_date = loan_date + timedelta(days= 10)

# print(return_date)


# from main import cust_list, books_list, loans_list
# from customers import Customer
# from loans import Loan
# from books import Book

# def return_book(loans_list):
#     '''
#     '''
#     while True: 
#         book_id = input('Please enter book id (5 digits), press 0 to exit: ')
#         if len(book_id) == 5 and book_id.isnumeric():    
#             break                       
#         if book_id == '0':
#             return loans_list

#     for loan in loans_list:
#         if book_id == loan.get_id():
#             print(loan)

# from datetime import datetime
# today = datetime.now()
# if datetime(2022,10,1) < today:
#     print('works')
# else:
#     print('itttt')
    
# try_2 = [1,2,3,4,5,6,7]
# print(try_2.index(1))

# ans = True
# while ans:
#     ans = input('enter: ')
#     if ans == '1':
#         print('1')
#     elif ans == '2':
#         print('2')
#     elif ans == '3':
#         print('3')
#     elif ans == 'x':
#         break
#     else:
#         print('else')

#validation of input - string with spaces
# while True:                         #validation for customer id. has to be 9 digits  <<<<<<<<<<<<<<<<<<<<<<
#         customer_name = input("Please enter customer's name, press 0 to exit: ")
#         if customer_name.replace(' ','').isalpha():    
#             print("thats okkkkkkkkkkk")                       
#             break          
#         print('This is not a valid id')      

# original.replace(' ','').isalpha()

# b_data = pandas.DataFrame({books_list[1]: 'id'}, columns=['Id, Name, Author, Year Published, Type, Copies'])
# import pandas
# from main import books_list

# b_data = pandas.DataFrame(books_list, columns=['Id, Name, Author, Year Published, Type, Copies'])
# b_data = pandas.DataFrame({'oldcol':[1,2,3]})
# b_data['col'] = books_list

# print(f'There are {len(b_data.index)} books in the library.\n')
# print(b_data)
    


    # b_data = pandas.read_csv('books.txt')
    # print(f'There are {len(b_data.index)} books in the library.\n')
    # print(b_data)
    # print(tabulate[['']], headers = ['id'])
    # b_data = pandas.DataFrame(books_list, columns=['Id, Name, Author, Year Published, Type, Copies'])
    # print(f'There are {len(b_data.index)} books in the library.\n')
    # print(b_data)
    