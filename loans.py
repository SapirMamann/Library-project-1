class Loan(object):
    def __init__(self, customer_id = 'undefined', book_id = 'undefined', loan_date = 'undefined', return_date = 'undefined'):
        self.__customer_id = customer_id
        self.__book_id = book_id
        self.__loan_date = loan_date
        self.__return_date = return_date
    
    def get_loan_cust_id(self):
        return self.__customer_id

    def get_loan_book_id(self):
        return self.__book_id

    def get_return_date(self):
        return self.__return_date

    def get_loan_atr(self):
        return self.__customer_id, self.__book_id, self.__loan_date, self.__return_date
        
    def __str__(self):
        return f'{self.__customer_id},{self.__book_id},{self.__loan_date},{self.__return_date}'