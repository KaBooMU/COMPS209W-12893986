import os
from flask import Flask, render_template, request, jsonify
from restaurant import Restaurant
from customer import Customer
from order import Order
from file_handler import FileHandler

app = Flask(__name__)

restaurant = Restaurant()
restaurant.setup()
file_handler = FileHandler("orders.txt")

active_order = None
order_counter = 1
customer_counter = 1


def item_to_dict(item):
    item_type = item.__class__.__name__
    extra = ""
    if hasattr(item, "_category"):
        extra = item._category
    elif hasattr(item, "_size"):
        extra = item._size
    return {
        "id": item.get_item_id(),
        "name": item.get_name(),
        "price": item.get_price(),
        "type": item_type,
        "extra": extra
    }


def table_to_dict(table):
    return {
        "number": table.get_number(),
        "capacity": table.get_capacity(),
        "occupied": not table.is_available()
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/menu")
def get_menu():
    return jsonify([item_to_dict(item) for item in restaurant.menu])


@app.route("/api/tables")
def get_tables():
    return jsonify([table_to_dict(table) for table in restaurant.tables])


@app.route("/api/create_order", methods=["POST"])
def create_order():
    global active_order, order_counter, customer_counter

    data = request.get_json() or {}
    name = str(data.get("name", "")).strip()
    phone = str(data.get("phone", "")).strip()

    try:
        people = int(data.get("people", 0))
    except (TypeError, ValueError):
        return jsonify({"error": "Group size must be an integer."}), 400

    if not name or not phone or people <= 0:
        return jsonify({"error": "Invalid customer data."}), 400

    if active_order is not None:
        return jsonify({"error": "An active order already exists."}), 400

    table = restaurant.assign_table(people)
    if table is None:
        return jsonify({"error": "No suitable table is available."}), 400

    customer = Customer(f"C{customer_counter:03d}", name, phone)
    active_order = Order(customer, table)

    order_counter += 1
    customer_counter += 1

    return jsonify({
        "message": "Order created successfully.",
        "customer_id": customer.get_customer_id(),
        "customer_name": customer.get_name(),
        "table_number": table.get_number()
    })


@app.route("/api/add_item", methods=["POST"])
def add_item():
    global active_order

    if active_order is None:
        return jsonify({"error": "No active order."}), 400

    data = request.get_json() or {}
    item_id = str(data.get("item_id", "")).strip()
    selected_item = restaurant.find_item(item_id)

    if selected_item is None:
        return jsonify({"error": "Item not found."}), 404

    active_order.add_item(selected_item)
    return jsonify({"message": "Item added successfully."})


@app.route("/api/remove_item", methods=["POST"])
def remove_item():
    global active_order

    if active_order is None:
        return jsonify({"error": "No active order."}), 400

    data = request.get_json() or {}
    try:
        index = int(data.get("index", -1))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid item index."}), 400

    removed = active_order.remove_item(index)
    if removed is None:
        return jsonify({"error": "Invalid item index."}), 400

    return jsonify({"message": "Item removed successfully."})


@app.route("/api/order")
def get_order():
    global active_order

    if active_order is None:
        return jsonify(None)

    subtotal, service_charge, total = active_order.calculate_total()

    return jsonify({
        "customer_name": active_order.customer.get_name(),
        "customer_phone": active_order.customer.get_phone(),
        "table_number": active_order.table.get_number(),
        "status": active_order.status,
        "items": [
            {
                "name": item.get_name(),
                "price": item.get_price()
            }
            for item in active_order.items
        ],
        "subtotal": subtotal,
        "service_charge": service_charge,
        "total": total
    })


@app.route("/api/save_order", methods=["POST"])
def save_order():
    global active_order

    if active_order is None:
        return jsonify({"error": "No active order."}), 400

    if len(active_order.items) == 0:
        return jsonify({"error": "Order is empty."}), 400

    file_handler.save(active_order)
    return jsonify({"message": "Order saved successfully."})


@app.route("/api/checkout", methods=["POST"])
def checkout_order():
    global active_order

    if active_order is None:
        return jsonify({"error": "No active order."}), 400

    if len(active_order.items) == 0:
        return jsonify({"error": "Order is empty."}), 400

    file_handler.save(active_order)
    active_order.table.release()
    active_order = None

    return jsonify({"message": "Checkout completed successfully."})


@app.route("/api/history")
def history():
    filename = file_handler.filename
    if not os.path.exists(filename):
        return jsonify([])

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if not content:
        return jsonify([])

    blocks = [block.strip() for block in content.split("===== ORDER =====") if block.strip()]
    results = []

    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines:
            continue
        customer_name = lines[0]
        total_line = lines[-1]
        item_names = lines[1:-1]
        results.append({
            "customer_name": customer_name,
            "items": item_names,
            "total_line": total_line
        })

    return jsonify(results)


if __name__ == "__main__":
    import os
    app.run(debug=True)
