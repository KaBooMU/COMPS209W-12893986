class MenuItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(self.name, "- HKD", self.price)


class FoodItem(MenuItem):

    def __init__(self, name, price, category):
        super().__init__(name, price)
        self.category = category

    def display(self):
        print(self.name, "(", self.category, ") - HKD", self.price)