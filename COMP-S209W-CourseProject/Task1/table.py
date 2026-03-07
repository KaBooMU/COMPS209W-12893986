class Table:

    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.occupied = False

    def assign(self):
        self.occupied = True

    def release(self):
        self.occupied = False

    def show_status(self):
        status = "Occupied" if self.occupied else "Available"
        print("Table", self.number, "-", status)