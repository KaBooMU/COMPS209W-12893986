class Table:
    def __init__(self, number, capacity):
        self.__number = number
        self.__capacity = capacity
        self.__occupied = False

    def assign(self):
        self.__occupied = True

    def release(self):
        self.__occupied = False

    def is_available(self):
        return not self.__occupied

    def get_capacity(self):
        return self.__capacity

    def get_number(self):
        return self.__number

    def display(self):
        status = "Occupied" if self.__occupied else "Available"
        print(f"Table {self.__number} ({self.__capacity} seats) - {status}")