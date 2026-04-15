class Order:
    def __init__(self, customer, table):
        self.customer = customer
        self.table = table
        self.items = []
        self.status = "Preparing"

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, index):
        if 0 <= index < len(self.items):
            return self.items.pop(index)
        return None

    def calculate_total(self):
        total = sum(item.get_price() for item in self.items)
        service = total * 0.1
        return total, service, total + service

    def display(self):
        print("\n===== ORDER =====")
        self.customer.display_info()
        print(f"Table: {self.table.get_number()}")

        print("\nItems:")
        for i, item in enumerate(self.items):
            print(f"{i+1}. ", end="")
            item.display()

        total, service, final = self.calculate_total()
        print(f"\nSubtotal: {total}")
        print(f"Service (10%): {service}")
        print(f"Final: {final}")
        print(f"Status: {self.status}")