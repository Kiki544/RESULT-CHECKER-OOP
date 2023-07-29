import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sqlite3

# Step 1: Install Required Libraries

# Step 2: Design the GUI
# Implement your GUI design here using PyQt5

# Step 3: Set Up the Database
# connection = sqlite3.connect("main.db")
# cursor = connection.cursor()

def get_details(matric_no, cursor):
    cursor.execute("SELECT Name, Level FROM Students WHERE MatricNo=(?)", (matric_no,))
    print(cursor)
    res = cursor.fetchall()
    return {'name': res[0][0], 'level': res[0][1], 'matric': matric_no}

def getSession(details, cursor):
    cursor.execute("SELECT SemesterId FROM Registration WHERE MatricNo=(?)", (details['matric'],))
    semId = cursor.fetchone()[0]
    
    cursor.execute("SELECT Session FROM Semester WHERE SemesterId=(?)", (semId,))
    # print(cursor.fetchone()[0])
    details['session'] = cursor.fetchone()[0]
    # print(details['session'])
    return details

def curriculum_calc(details):
    # print(int(str(details['session']).split('/')[0]) - 2018)
    return ((((int(str(details['session']).split('/')[0])) - 2018) + 1) * 100)

# Step 8: Senate Summary
def display_senate_summary(window, mat_no, cursor):
    # connection = sqlite3.connect("main.db")
    # cursor = connection.cursor()
    
    matric_no = mat_no
    print(matric_no)
    table_widget = window.ui.student_table

    # print(get_details(matric_no))
    details = getSession(get_details(matric_no, cursor), cursor)

    if curriculum_calc(details) == details['level']:
        details['curriculum'] = 'o'
    else:
        details['curriculum'] = 'n'
    
    labels = ['label_5', 'label_6', 'label_7', 'label_8']

    window.ui.label_16.setText(details['name'])
    window.ui.label_16.adjustSize()
    
    window.ui.label_20.setText(details['matric'])
    window.ui.label_20.adjustSize()

    window.ui.label_21.setText(str(details['level']))
    window.ui.label_21.adjustSize()

    window.ui.label_23.setText(str(details['session']))
    window.ui.label_23.adjustSize()

    # Fetch data from the "registration" table
    cursor.execute("SELECT CourseCodes FROM Registration WHERE MatricNo=(?)", (matric_no,))
    registration_data = cursor.fetchall()
    # print(registration_data)

    # Create a table to display the senate summary
    table_widget.setColumnCount(3)  # Adjust the number of columns as per your requirement
    table_widget.setHorizontalHeaderLabels(["CourseCode", "Course Details", "Units"])

    # Create a dictionary to store course details for each course
    student_courses = {}

    # Process registration data
    courseCode = registration_data[0][0].split(',')
    # print(courseCode)
    # print(f"This: {details['curriculum']}")
    temp = details['curriculum']
    # courseCode = [1,2,3 ]

    # Fetch course details for the course code
    for i in courseCode:
        cursor.execute(f"SELECT CourseCode, CourseName, CourseUnits FROM {temp}_Courses WHERE CourseCode=(?)", (i,))
        # print('here')
        # print(cursor.fetchall())
        course_data = [j for j in cursor.fetchall()[0]]

        code = course_data[0]
        details = course_data[1:]


        if code not in student_courses:
            student_courses[code] = []
        student_courses[code].extend(details)
    


    # Populate the table with student course details
    row = table_widget.rowCount()

    for code, details in student_courses.items():
        table_widget.setRowCount(row + 1)

        code_item = QtWidgets.QTableWidgetItem(code)
        table_widget.setItem(row, 0, code_item)

        table_widget.setVerticalHeaderItem(row, QtWidgets.QTableWidgetItem())
        for i in range(1, 3):
            course_details_item = QtWidgets.QTableWidgetItem()
            course_details_item.setText(str(details[i - 1]))
            table_widget.setItem(row, i, course_details_item)

        row += 1
    table_widget.resizeColumnsToContents()
    # Show the table in the GUI
    # layout.addWidget(table_widget)


# class MyWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#         uic.loadUi("student.ui", self)


# Step 2: Design the GUI (continued)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()

    # Create the main layout
    # layout = QtWidgets.QVBoxLayout()

    # Call the function to display the senate summary
    display_senate_summary(window, 'EU210303-2872')

    # Create the central widget and set the layout
    # window.central_widget.setLayout(layout)

    window.show()
    sys.exit(app.exec_())

    # Step 9: Database Operations
    connection.close()
