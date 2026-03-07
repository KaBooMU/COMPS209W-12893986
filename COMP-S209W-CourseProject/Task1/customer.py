class Customer:

    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def get_name(self):
        return self.__name

    def display_info(self):
        print("Customer:", self.__name)
        print("Phone:", self.__phone)