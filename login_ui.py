# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 620)
        Dialog.setStyleSheet("background-color: rgb(49, 58, 70);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 140, 111, 41))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 28pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 240, 171, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(220, 240, 211, 31))
        self.username.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.username.setText("")
        self.username.setObjectName("username")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 330, 141, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(220, 330, 211, 31))
        self.password.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.password.setText("")
        self.password.setObjectName("password")
        self.loginbutton = QtWidgets.QPushButton(Dialog)
        self.loginbutton.setGeometry(QtCore.QRect(350, 440, 75, 23))
        self.loginbutton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.loginbutton.setObjectName("loginbutton")
        self.logo1 = QtWidgets.QWidget(Dialog)
        self.logo1.setGeometry(QtCore.QRect(160, 40, 120, 80))
        self.logo1.setStyleSheet("image: url(:/LOGOO/e5wbhcvarvc1szsusbbi.webp);\n"
"image: url(:/LOGOO/LOGO/e5wbhcvarvc1szsusbbi.webp);")
        self.logo1.setObjectName("logo1")
        self.error1 = QtWidgets.QLabel(Dialog)
        self.error1.setGeometry(QtCore.QRect(230, 380, 201, 16))
        self.error1.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.error1.setText("")
        self.error1.setObjectName("error1")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "LOGIN"))
        self.label_2.setText(_translate("Dialog", "USERNAME:"))
        self.label_3.setText(_translate("Dialog", "PASSWORD:"))
        self.loginbutton.setText(_translate("Dialog", "LOGIN"))

import resource_rc