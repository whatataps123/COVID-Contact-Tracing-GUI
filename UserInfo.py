class User_info():
    def __init__(self, name="",age="",address="",contact="",email=""):
        # get name
        self.__name = name
        # get age
        self.__age = age
        # get address
        self.__address = address
        # get contact
        self.__contact = contact
        # get email
        self.__email = email

    def get_name(self, name):
        return self.__name
    
    def get_age(self, age):
        return self.__age
    
    def get_address(self, address):
        return self.__address
    
    def get_contact(self, contact):
        return self.__contact
    
    def get_email(self, email):
        return self.__email