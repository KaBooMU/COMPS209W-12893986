from menu import FoodItem, DrinkItem
from table import Table


class Restaurant:
    def __init__(self):
        self.menu = []
        self.tables = []

    def setup(self):
        # menu
        self.menu.append(FoodItem("F1", "Fried Rice", 48, "Main"))
        self.menu.append(FoodItem("F2", "Burger", 55, "Main"))
        self.menu.append(FoodItem("F3", "Salad", 36, "Starter"))

        self.menu.append(DrinkItem("D1", "Milk Tea", 18, "Regular"))
        self.menu.append(DrinkItem("D2", "Coffee", 22, "Regular"))

        # tables
        self.tables.append(Table(1, 2))
        self.tables.append(Table(2, 4))
        self.tables.append(Table(3, 6))

    def show_menu(self):
        print("\n===== MENU =====")
        for item in self.menu:
            item.display()

    def find_item(self, item_id):
        for item in self.menu:
            if item.get_item_id() == item_id:
                return item
        return None

    def assign_table(self, people):
        for table in self.tables:
            if table.is_available() and table.get_capacity() >= people:
                table.assign()
                return table
        return None

    def show_tables(self):
        for table in self.tables:
            table.display()