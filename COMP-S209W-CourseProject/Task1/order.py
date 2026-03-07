class Order:

    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.status = "Preparing"

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def display_order(self):
        print("\nOrder Summary")
        self.customer.display_info()

        print("\nItems:")
        for item in self.items:
            item.display()

        print("Total Bill:", self.calculate_total())