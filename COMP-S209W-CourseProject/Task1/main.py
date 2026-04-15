from customer import Customer
from restaurant import Restaurant
from order import Order
from file_handler import FileHandler


def main():
    r = Restaurant()
    r.setup()
    fh = FileHandler("orders.txt")

    order = None

    while True:
        print("\n1.Menu 2.Tables 3.New Order 4.View Order 5.Remove Item")
        print("6.Save History 7.View History 0.Exit")

        choice = input("Choice: ")

        if choice == "1":
            r.show_menu()

        elif choice == "2":
            r.show_tables()

        elif choice == "3":
            name = input("Name: ")
            phone = input("Phone: ")
            people = int(input("People: "))

            customer = Customer("C1", name, phone)
            table = r.assign_table(people)

            if not table:
                print("No table available")
                continue

            order = Order(customer, table)

            while True:
                r.show_menu()
                item_id = input("Add item (0 to stop): ")

                if item_id == "0":
                    break

                item = r.find_item(item_id)
                if item:
                    order.add_item(item)

        elif choice == "4":
            if order:
                order.display()

        elif choice == "5":
            if order:
                index = int(input("Remove item number: ")) - 1
                order.remove_item(index)

        elif choice == "6":
            if order:
                fh.save(order)

        elif choice == "7":
            fh.read()

        elif choice == "0":
            break


if __name__ == "__main__":
    main()