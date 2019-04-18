# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui',
# licensing of 'register.ui' applies.
#
# Created: Thu Apr 18 14:10:00 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("QWidget{\n"
"    background-image: url(:/login-bg/login.png)\n"
"}\n"
"QPushButton{\n"
"    border-radius: 8px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 19, 18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: transparent;\n"
"    border: 1px solid #361A17;\n"
"    color: #361A17;\n"
"}")
        self.login_label = QtWidgets.QLabel(Form)
        self.login_label.setGeometry(QtCore.QRect(410, 160, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(34)
        self.login_label.setFont(font)
        self.login_label.setAutoFillBackground(False)
        self.login_label.setStyleSheet("background-color: transparent;")
        self.login_label.setObjectName("login_label")
        self.username_lineEdit = QtWidgets.QLineEdit(Form)
        self.username_lineEdit.setGeometry(QtCore.QRect(360, 220, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setAutoFillBackground(False)
        self.username_lineEdit.setStyleSheet("background-color: rgba(0,0,0,0%);\n"
"border-bottom: 1px solid black;\n"
"border-top: 0px;\n"
"padding: 2px;")
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.pw_lineEdit = QtWidgets.QLineEdit(Form)
        self.pw_lineEdit.setGeometry(QtCore.QRect(360, 340, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.pw_lineEdit.setFont(font)
        self.pw_lineEdit.setAutoFillBackground(False)
        self.pw_lineEdit.setStyleSheet("background-color: transparent;\n"
"border-bottom: 1px solid black;\n"
"border-top: 0px;\n"
"padding: 2px;")
        self.pw_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_lineEdit.setClearButtonEnabled(False)
        self.pw_lineEdit.setObjectName("pw_lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(360, 400, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pw_lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.pw_lineEdit_2.setGeometry(QtCore.QRect(360, 280, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.pw_lineEdit_2.setFont(font)
        self.pw_lineEdit_2.setAutoFillBackground(False)
        self.pw_lineEdit_2.setStyleSheet("background-color: transparent;\n"
"border-bottom: 1px solid black;\n"
"border-top: 0px;\n"
"padding: 2px;")
        self.pw_lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.pw_lineEdit_2.setClearButtonEnabled(False)
        self.pw_lineEdit_2.setObjectName("pw_lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.login_label.setText(QtWidgets.QApplication.translate("Form", "REGISTER", None, -1))
        self.username_lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Username", None, -1))
        self.pw_lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Password", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "Register", None, -1))
        self.pw_lineEdit_2.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Line ID", None, -1))

