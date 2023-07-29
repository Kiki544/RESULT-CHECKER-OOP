import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sqlite3

# Step 1: Install Required Libraries

# Step 2: Design the GUI
# Implement your GUI design here using PyQt5

# Step 3: Set Up the Database
# connection = sqlite3.connect("main.db")
# cursor = connection.cursor()

def get_grade(course, matric_no, cursor):
    # print(f"Course: {course}")
    # print(f"Matric: {matric_no}")
    cursor.execute(f"SELECT {course} FROM nResults_100L2 WHERE MATRIC_NUMBER=(?)", (matric_no,))
    # print(f"Test: {cursor.fetchone()[0]}")
    return cursor.fetchone()[0]

def get_codes(courses, matric_no):
    courses = courses[0].split(',')
    print(f"Testing: {courses}")
    for i in range(len(courses)):
        courses[i] = f"{courses[i]}({get_grade(courses[i], matric_no)})"
    return courses

def get_courses(matric, cursor):
    cursor.execute("SELECT CourseCodes FROM Registration WHERE MatricNo=(?)", (matric,))
    return cursor.fetchone()

def get_matrics(cursor):
    cursor.execute("SELECT MatricNo FROM Registration")
    temp = cursor.fetchall()
    return temp

# Step 6: Display Departmental Summary
def display_departmental_summary(window, cursor):
    table_widget = window.ui.departmental_table
    # Fetch data from the "registration" table
    cursor.execute("SELECT * FROM Registration")
    student_data = cursor.fetchall()


    # Create a table to display the departmental summary
    table_widget.setColumnCount(2)  # Adjust the number of columns as per your requirement
    table_widget.setHorizontalHeaderLabels(["Matric No", "Course Code"])

    # Populate the table with student data
    row = 0
    matric_nos = get_matrics(cursor)
    print(f"This: {matric_nos}")
    for student in matric_nos:
        matric_no = student[0]
        courses = get_courses(matric_no, cursor)[0]
        # print(f"Students: {student_row}")
        # print(f"courses: {courses}")
        
        # Insert data into the table
        table_widget.insertRow(row)
        print("Works")
        table_widget.setVerticalHeaderItem(row, QtWidgets.QTableWidgetItem())

        table_widget.setItem(row, 0, QtWidgets.QTableWidgetItem(matric_no))
        table_widget.setItem(row, 1, QtWidgets.QTableWidgetItem(courses))
        # print(table_widget.item(row, 1))
        # table_widget.setItem(row, 2, QtWidgets.QTableWidgetItem(grade))

        row += 1
    table_widget.resizeColumnsToContents()

    # Show the table in the GUI
    # layout.addWidget(table_widget)

# class MyWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#         uic.loadUi("departmental.ui", self)

# Step 2: Design the GUI (continued)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()

    # Create the main layout
    # layout = QtWidgets.QVBoxLayout()

    # Call the function to display the departmental summary
    display_departmental_summary(window)

    # Create the central widget and set the layout
    central_widget = QtWidgets.QWidget()
    # central_widget.setLayout(layout)

    window.show()
    sys.exit(app.exec_())

    # Step 9: Database Operations
    connection.close()
