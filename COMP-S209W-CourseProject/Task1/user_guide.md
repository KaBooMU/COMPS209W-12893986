# Task 1 User Guide

## System Name
Smart Restaurant Ordering and Table Management System

## Purpose
This system helps restaurant staff manage customer orders and table allocation more systematically.

## Steps to Use

### 1. Start the system
- Open terminal in the `Task1` folder.
- Run:
  `python app.py`
- Open the browser at:
  `http://127.0.0.1:5000/`

### 2. Create a new order
- Enter the customer name
- Enter the phone number
- Enter the group size
- Click **Create New Order**

The system will automatically assign a suitable available table.

### 3. Add menu items
- Browse the menu shown on the page
- Click the button to add items to the active order

### 4. Remove menu items
- In the active order section, click the remove button beside the item you want to delete

### 5. Check bill calculation
The system will automatically show:
- subtotal
- service charge
- total amount

### 6. Save the order
- Click **Save Order**
- The order record will be written to the order history file

### 7. Checkout
- Click **Checkout**
- The order will be completed
- The assigned table will be released and become available again

## Notes
- Only one active order is handled at a time in this version
- Table assignment is automatic
- A service charge is included in bill calculation