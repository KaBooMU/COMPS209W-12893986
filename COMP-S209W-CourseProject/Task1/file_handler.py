class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def save(self, order):
        with open(self.filename, "a") as f:
            f.write("===== ORDER =====\n")
            f.write(order.customer.get_name() + "\n")

            for item in order.items:
                f.write(item.get_name() + "\n")

            total, service, final = order.calculate_total()
            f.write(f"Total: {final}\n\n")

    def read(self):
        try:
            with open(self.filename, "r") as f:
                print(f.read())
        except:
            print("No history yet.")