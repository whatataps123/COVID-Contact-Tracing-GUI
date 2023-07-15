class Entry_panel():
    def user_info(self, name="",age="",address="",contact="",email=""):
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

    def get_info(self, name):
        return self.__name
    
    def get_info(self, age):
        return self.__age