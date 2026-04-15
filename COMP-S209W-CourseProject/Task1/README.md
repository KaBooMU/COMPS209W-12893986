# Task 1 – Smart Restaurant Ordering and Table Management System

## Description
This task is a restaurant ordering and table management system developed for COMP S209W.

The project keeps the original Python modules for the main business logic and extends the system with a simple Flask-based web interface. The system allows users to create customer orders, assign tables automatically, add and remove menu items, calculate bills, save order records, and manage table availability.

## Files
- `app.py` – Flask application for the web interface
- `customer.py` – customer class
- `menu.py` – menu item classes
- `order.py` – order class
- `table.py` – table class
- `restaurant.py` – restaurant management logic
- `file_handler.py` – file saving and reading
- `main.py` – original Python console entry
- `templates/index.html` – HTML page
- `static/styles.css` – CSS styling
- `static/app.js` – JavaScript for browser interaction

## Main Features
- Create a customer order
- Automatically assign a suitable table
- Display menu items
- Add and remove items from an order
- Calculate subtotal, service charge, and total
- Save order history to file
- Display current table status
- Provide a browser-based user interface

## Programming Concepts Used
- Modular programming
- Object-oriented programming
- Encapsulation
- Inheritance
- Polymorphism
- File handling
- Flask web integration

## How to Run
1. Open terminal in the `Task1` folder.
2. Install Flask:
   `pip install flask`
3. Run the program:
   `python app.py`
4. Open the browser and visit:
   `http://127.0.0.1:5000/`

## Notes
- This version uses the original Python modules as the core logic.
- The web interface is added for easier interaction and demonstration.
- Order history is saved to a text file.