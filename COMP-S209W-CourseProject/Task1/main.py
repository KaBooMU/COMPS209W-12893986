from customer import Customer
from menu import FoodItem
from table import Table
from order import Order


def show_menu(menu):

    print("\nRestaurant Menu")

    for i in range(len(menu)):
        print(i + 1, end=". ")
        menu[i].display()


def main():

    menu = [
        FoodItem("Fried Rice", 48, "Main"),
        FoodItem("Burger", 55, "Main"),
        FoodItem("Salad", 36, "Starter"),
        FoodItem("Milk Tea", 18, "Drink"),
        FoodItem("Ice Cream", 22, "Dessert")
    ]

    customer = Customer("Ng Chun Yiu", "91234567")

    table = Table(1, 4)
    table.assign()

    order = Order(customer)

    show_menu(menu)

    order.add_item(menu[0])
    order.add_item(menu[3])

    order.display_order()


if __name__ == "__main__":
    main()