class Customer(object):
    def __init__(self, id = 'undefined', name = 'undefined', city = 'undefined', age = 'undefined'):
        self.__id = id
        self.__name = name
        self.__city = city
        self.__age = age

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_cust_atr(self):
        return self.__id, self.__name, self.__city, self.__age

    def __str__(self):
        return f'{self.__id},{self.__name},{self.__city},{self.__age}'
