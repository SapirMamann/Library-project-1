class Book(object):
    def __init__(self, id = 'undefined', name = 'undefined', author = 'undefined', year_published = 'undefined', type = 'undefined', copies = 'undefined'):
        self.__id = id
        self.__name = name
        self.__author = author
        self.__year_published = year_published
        self.__type = type
        self.__copies = copies 

    def get_book_id(self):
        return self.__id

    def get_book_name(self):
        return self.__name

    def get_book_type(self):
        return self.__type
    
    def get_book_copies_n(self):
        return self.__copies

    def update_copies(self, value):
        self.__copies = value

    def get_book_atr(self):
        return self.__id, self.__name, self.__author, self.__year_published, self.__type, self.__copies

    def __str__(self):
        return f'{self.__id},{self.__name},{self.__author},{self.__year_published},{self.__type},{self.__copies}'
