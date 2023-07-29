import os.path
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui, uic


# dbFile = os.path.abspath(os.path.join(os.path.dirname(__file__), 'students.db'))

def create_connection(dbFile):
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
    except Exception as e:
        print(e)

    return conn

def convert(file, offset, num):
        rows = []
        if num == 0:
            for row in getData(file, offset):
                rows.append(row)
        elif num == 1:
            for row in filter_by_matric_no(file, offset):
                rows.append(row)
        elif num==2:
            for row in sort_by_cgpa(file, offset):
                rows.append(row)
        return rows

def getData(dbFile, offset):
        conn = create_connection(dbFile)

        get_all = "SELECT * FROM students LIMIT 10 OFFSET (?)"

        try:

            c = conn.cursor()
            c.execute(get_all, (offset,))
            return c.fetchall()
        except Exception as e:
            print(e)

def calculate_remarks(grade):
    remarks = ["First Class", "Second Class Upper", "Second Class Lower", "Third Class"]
    if grade >= 4.50:
        return remarks[0]
    elif grade <= 4.49 and grade >= 3.50:
        return remarks[1]
    elif grade <= 3.49 and grade >= 2.50:
        return remarks[2]
    else:
        return remarks[3]

    

def calculation(list, num):
    if num == 0:
        return list[0] + list[3]
    elif num == 1:
        return list[1] + list[4]
    elif num == 2:
        return round((list[0] + list[3]) / (list[1] + list[4]), 2)

def filter_by_matric_no(dbFile, offset):
    conn = create_connection(dbFile)
    cursor = conn.cursor()

    query = "SELECT * FROM students ORDER BY matric_no LIMIT 10 OFFSET(?)"
    cursor.execute(query, (offset,))
        
    return cursor

def sort_by_cgpa(self, dbFile, offset):
    conn = create_connection(dbFile)
    cursor = conn.cursor()

    query = "SELECT * FROM students ORDER BY gpaPresent DESC LIMIT 10 OFFSET(?) "
    cursor.execute(query, (offset,))

    return cursor

def show_data(window, val, num, file):
        window.offset += val
        rows = convert(file, window.offset, num)
        arr = [window.ui.tableWidget_2, window.ui.tableWidget_3, window.ui.tableWidget_4, window.ui.tableWidget_5, window.ui.tableWidget_6]
        for i in arr:
            i.setRowCount(0)
        display(window, rows)
        display_previous(window, rows)
        display_present(window, rows)
        display_cummulative(window, rows)

def display(window, rows):   # First Table
        headerList = window.headerList
        window = window.ui
        window.tableWidget_2.setColumnCount(len(headerList[:3]))
        window.tableWidget_2.horizontalHeader
        window.tableWidget_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        window.tableWidget_2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        window.tableWidget_2.setHorizontalHeaderLabels(headerList[:3])

        window.tableWidget_6.setColumnCount(1)
        window.tableWidget_6.horizontalHeader
        window.tableWidget_6.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        window.tableWidget_6.setHorizontalHeaderLabels(headerList[7:])

        rowPosition = window.tableWidget_2.rowCount()

        # row = ['', '', '']
        # window.tableWidget.setRowCount(rowPosition + 1)
        # window.tableWidget.setVerticalHeaderItem(rowPosition, QtWidgets.QTableWidgetItem())
        # window.tableWidget4.setRowCount(rowPosition + 1)
        # window.tableWidget4.setVerticalHeaderItem(rowPosition, QtWidgets.QTableWidgetItem())

        # itemCount = 0
        # for item in row:
        #     if itemCount == 0 and rowPosition == 0:
        #         window.qtablewidgetitem = QtWidgets.QTableWidgetItem()
        #         window.tableWidget4.setItem(rowPosition, itemCount, window.qtablewidgetitem)
        #         window.qtablewidgetitem = window.tableWidget4.item(rowPosition, itemCount)
        #         window.qtablewidgetitem.setText('')

        #     window.qtablewidgetitem = QtWidgets.QTableWidgetItem()
        #     window.tableWidget.setItem(rowPosition, itemCount, window.qtablewidgetitem)
        #     window.qtablewidgetitem = window.tableWidget.item(rowPosition, itemCount)
        #     window.qtablewidgetitem.setText(str(item))

        #     itemCount += 1
        # rowPosition += 1
        for row in rows:
            # if (rowPosition > row[0]):
            #     continue            

            window.tableWidget_2.setRowCount(rowPosition + 1)
            qtablewidgetitem = QtWidgets.QTableWidgetItem()
            window.tableWidget_2.setVerticalHeaderItem(rowPosition, qtablewidgetitem)

            window.tableWidget_6.setRowCount(rowPosition + 1)
            qtablewidgetitem = QtWidgets.QTableWidgetItem()
            window.tableWidget_6.setVerticalHeaderItem(rowPosition, qtablewidgetitem)
            
            itemCount = 0
            for item in row:
                window.qtablewidgetitem = QtWidgets.QTableWidgetItem()
                
                if itemCount in [3, 4, 5, 6, 7, 8, 9]:
                    itemCount += 1
                    continue
                
                elif itemCount == 10:
                    tw = window.tableWidget_6
                    tw.setItem(rowPosition, 0, window.qtablewidgetitem)
                    window.qtablewidgetitem = tw.item(rowPosition, 0)
                    window.qtablewidgetitem.setText(str(calculate_remarks(calculation(row[4:10], 2))))
                    break
                
                window.tableWidget_2.setItem(rowPosition, itemCount, window.qtablewidgetitem)
                window.qtablewidgetitem = window.tableWidget_2.item(rowPosition, itemCount)
                window.qtablewidgetitem.setText(str(item))

                itemCount += 1
            rowPosition += 1
        window.tableWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        window.tableWidget_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    
def display_previous(window, rows): #Previous Scores Table
        tw = window.ui.tableWidget_3
        tw.setColumnCount(3)
        tw.horizontalHeader
        tw.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        tw.setHorizontalHeaderLabels(window.headerList[4:7])

        rowPosition = tw.rowCount()

        tw.setRowCount(rowPosition + 1)
        tw.setVerticalHeaderItem(rowPosition, QtWidgets.QTableWidgetItem())

        itemCount = 0
        # for item in window.headerList[4:7]:
        #     window.qtablewidgetitem = QtWidgets.QTableWidgetItem()
        #     tw.setItem(rowPosition, itemCount, window.qtablewidgetitem)
        #     window.qtablewidgetitem = tw.item(rowPosition, itemCount)
        #     window.qtablewidgetitem.setText(str(item))

        #     itemCount += 1
        # rowPosition += 1

        for row in rows:
            row = row[4:7]

            tw.setRowCount(rowPosition + 1)
            qtablewidgetitem = QtWidgets.QTableWidgetItem()
            tw.setVerticalHeaderItem(rowPosition, qtablewidgetitem)

            itemCount = 0
            for item in row:
                window.qtablewidgetitem = QtWidgets.QTableWidgetItem()
                tw.setItem(rowPosition, itemCount, window.qtablewidgetitem)
                window.qtablewidgetitem = tw.item(rowPosition, itemCount)
                window.qtablewidgetitem.setText(str(item))

                itemCount += 1
            rowPosition += 1

        tw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # tw.setMinimumHeight(tw.horizontalHeader().height() + (tw.rowHeight(0) * tw.rowCount()))
        # tw.setMaximumHeight(tw.minimumHeight())

def display_present(window, rows): #Present Scores Table
    tw = window.ui.tableWidget_4
    tw.setColumnCount(3)
    tw.horizontalHeader
    tw.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    tw.setHorizontalHeaderLabels(window.headerList[4:7])

    rowPosition = tw.rowCount()

    tw.setRowCount(rowPosition + 1)
    tw.setVerticalHeaderItem(rowPosition, QtWidgets.QTableWidgetItem())

    # itemCount = 0
    # for item in self.headerList[4:7]:
    #     self.qtablewidgetitem = QtWidgets.QTableWidgetItem()
    #     tw.setItem(rowPosition, itemCount, self.qtablewidgetitem)
    #     self.qtablewidgetitem = tw.item(rowPosition, itemCount)
    #     self.qtablewidgetitem.setText(str(item))

    #     itemCount += 1
    # rowPosition += 1

    for row in rows:
        row = row[7:10]

        tw.setRowCount(rowPosition + 1)
        qtablewidgetitem = QtWidgets.QTableWidgetItem()
        tw.setVerticalHeaderItem(rowPosition, qtablewidgetitem)

        itemCount = 0
        for item in row:
            window.qtablewidgetitem = QtWidgets.QTableWidgetItem()
            tw.setItem(rowPosition, itemCount, window.qtablewidgetitem)
            window.qtablewidgetitem = tw.item(rowPosition, itemCount)
            window.qtablewidgetitem.setText(str(item))

            itemCount += 1
        rowPosition += 1

    tw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    # tw.setMinimumHeight(tw.horizontalHeader().height() + (tw.rowHeight(0) * tw.rowCount()))
    # tw.setMaximumHeight(tw.minimumHeight())

def display_cummulative(window, rows):
    tw = window.ui.tableWidget_5
    tw.setColumnCount(3)
    tw.horizontalHeader
    tw.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    tw.setHorizontalHeaderLabels(window.headerList[4:7])

    rowPosition = tw.rowCount()

    tw.setRowCount(rowPosition + 1)
    tw.setVerticalHeaderItem(rowPosition, QtWidgets.QTableWidgetItem())

    itemCount = 0
    # for item in self.headerList[4:7]:
    #     self.qtablewidgetitem = QtWidgets.QTableWidgetItem()
    #     tw.setItem(rowPosition, itemCount, self.qtablewidgetitem)
    #     self.qtablewidgetitem = tw.item(rowPosition, itemCount)
    #     self.qtablewidgetitem.setText(str(item))

    #     itemCount += 1
    #     rowPosition += 1

    for row in rows:
        row = row[4:10]

        tw.setRowCount(rowPosition + 1)
        qtablewidgetitem = QtWidgets.QTableWidgetItem()
        tw.setVerticalHeaderItem(rowPosition, qtablewidgetitem)

        itemCount = 0
        for item in row:
            if itemCount > 2:
                break
            item = calculation(row, itemCount)
            window.qtablewidgetitem = QtWidgets.QTableWidgetItem()
            tw.setItem(rowPosition, itemCount, window.qtablewidgetitem)
            window.qtablewidgetitem = tw.item(rowPosition, itemCount)
            window.qtablewidgetitem.setText(str(item))

            itemCount += 1
        rowPosition += 1

    tw.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    # tw.setMinimumHeight(tw.horizontalHeader().height() + (tw.rowHeight(0) * tw.rowCount()))
    # tw.setMaximumHeight(tw.minimumHeight())


# class MyWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#         uic.loadUi("untitled.ui", self)

#         self.headerList = ['S/N', "Name", "Matric No.", "Grade", 'TCP', 'TNU', 'GPA', 'Remarks']
#         self.offset = 0
#         self.btn_prev.clicked.connect(lambda: self.show_data(-10, 0))
#         self.btn_next.clicked.connect(lambda: self.show_data(10, 0))
#         self.btn_mat.clicked.connect(lambda: self.show_data(0, 1))
#         self.btn_gpa.clicked.connect(lambda: self.show_data(0, 2))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     window.show_data(0, 0)
#     sys.exit(app.exec_())


