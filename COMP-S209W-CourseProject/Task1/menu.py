class MenuItem:
    def __init__(self, item_id, name, price):
        self._item_id = item_id
        self._name = name
        self._price = price

    def get_item_id(self):
        return self._item_id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def display(self):
        print(f"[{self._item_id}] {self._name} - HKD {self._price}")

class FoodItem(MenuItem):
    def __init__(self, item_id, name, price, category):
        super().__init__(item_id, name, price)
        self._category = category

    def display(self):
        print(f"[{self._item_id}] {self._name} ({self._category}) - HKD {self._price}")
        
class DrinkItem(MenuItem):
    def __init__(self, item_id, name, price, size):
        super().__init__(item_id, name, price)
        self._size = size

    def display(self):
        print(f"[{self._item_id}] {self._name} ({self._size}) - HKD {self._price}")