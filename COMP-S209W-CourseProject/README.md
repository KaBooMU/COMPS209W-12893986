# Smart Restaurant Ordering and Table Management System

## Course
COMP S209W Data Structures and Problem Solving (Spring Term 2026)

## Student Information
**Name:** Ng Chun Yiu  
**SID:** 12893986

## Project Overview
This project is developed as the final course project for COMP S209W. It consists of two tasks that demonstrate problem solving, modular programming, object-oriented programming, data structures, and algorithms.

### Task 1
**Smart Restaurant Ordering and Table Management System**

Task 1 is a restaurant ordering and table management system built with the original Python modules and enhanced with a simple Flask-based web interface.

The project keeps the original Python program structure and business logic in separate files, including customer management, menu items, table assignment, order processing, restaurant coordination, and file handling. A browser-based user interface is added through Flask, HTML, CSS, and JavaScript so that the system is easier to demonstrate and use.

### Task 2
**Heap and Heap Sort Self-Study**

Task 2 is a self-study task covering:

- **Data Structure:** Heap
- **Algorithm:** Heap Sort

This part demonstrates the implementation of a max heap, major heap operations, and the use of heap sort to sort a list of values.

## Project Structure


COMP-S209W-CourseProject/
│
├── README.md
│
├── Task1/
│   ├── app.py
│   ├── customer.py
│   ├── file_handler.py
│   ├── main.py
│   ├── menu.py
│   ├── order.py
│   ├── restaurant.py
│   ├── table.py
│   ├── README.md
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── styles.css
│       └── app.js
│
├── Task2/
│   ├── heap_study.py
│   ├── README.md
│
├── Task1_Report.pdf
├── Task2_Report.pdf
└── video_link.txt


## Task 1 Features
- Customer creation
- Menu display
- Automatic table assignment
- Order creation and management
- Add and remove menu items
- Bill calculation with service charge
- Order history saving
- Restaurant table status display
- Simple browser-based user interface

## Task 2 Features
- Max heap implementation
- Insert operation
- Extract maximum operation
- Heapify process
- Build max heap
- Heap sort demonstration
- Time complexity discussion in the report

## How to Run

### Task 1
Task 1 uses Flask for the web interface.

1. Open terminal in the `Task1` folder
2. Install Flask
pip install flask

3. Run the program
python app.py

4. Open the browser and visit:
http://127.0.0.1:5000/


### Task 2
1. Open terminal in the `Task2` folder
2. Run:
python heap_study.py


## Files Included in the Repository
The repository should contain:
- all Python source code files
- web interface files for Task 1
- user guides for Task 1 and Task 2
- Task 1 report
- Task 2 report
- video demonstration link

## Video Demonstration
task1: https://youtu.be/RZsxKb7AmEY
task2 :https://youtu.be/IDe4b9Th2jQ

## GitHub Repository
https://github.com/KaBooMU/COMPS209W-12893986/tree/main/COMP-S209W-CourseProject/

## References
- COMP S209W lecture notes
- Python Documentation
- Flask Documentation
