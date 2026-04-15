class Customer:
    def __init__(self, customer_id, name, phone):
        self.__customer_id = customer_id
        self.__name = name
        self.__phone = phone

    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def display_info(self):
        print(f"Customer ID: {self.__customer_id}")
        print(f"Name: {self.__name}")
        print(f"Phone: {self.__phone}")