# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui',
# licensing of 'login.ui' applies.
#
# Created: Fri Apr 19 13:58:39 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        Form.setMouseTracking(False)
        Form.setStyleSheet("QPushButton{\n"
"    border-radius: 8px;\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(40, 19, 18);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: transparent;\n"
"    border: 1px solid #361A17;\n"
"    color: #361A17;\n"
"}\n"
"QLabel{\n"
"    background-color: transparent;\n"
"    color: black;\n"
"}\n"
"QLabel:hover#reg_label{\n"
"    color: rgb(201, 50, 41)\n"
"}\n"
"QLineEdit{\n"
"    background-color: transparent;\n"
"    border-bottom: 1px solid black;\n"
"    border-top: 0px;\n"
"    padding: 2px;\n"
"}")
        self.login_label = QtWidgets.QLabel(Form)
        self.login_label.setGeometry(QtCore.QRect(440, 150, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(34)
        self.login_label.setFont(font)
        self.login_label.setAutoFillBackground(False)
        self.login_label.setStyleSheet("")
        self.login_label.setObjectName("login_label")
        self.username_lineEdit = QtWidgets.QLineEdit(Form)
        self.username_lineEdit.setGeometry(QtCore.QRect(360, 230, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(21)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setAutoFillBackground(False)
        self.username_lineEdit.setStyleSheet("\n"
"")
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.pw_lineEdit = QtWidgets.QLineEdit(Form)
        self.pw_lineEdit.setGeometry(QtCore.QRect(360, 290, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(21)
        self.pw_lineEdit.setFont(font)
        self.pw_lineEdit.setAutoFillBackground(False)
        self.pw_lineEdit.setStyleSheet("")
        self.pw_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_lineEdit.setClearButtonEnabled(False)
        self.pw_lineEdit.setObjectName("pw_lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(360, 370, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.reg_label = QtWidgets.QLabel(Form)
        self.reg_label.setGeometry(QtCore.QRect(390, 420, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(19)
        self.reg_label.setFont(font)
        self.reg_label.setMouseTracking(False)
        self.reg_label.setStyleSheet("")
        self.reg_label.setObjectName("reg_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.login_label.setText(QtWidgets.QApplication.translate("Form", "LOGIN", None, -1))
        self.username_lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Username", None, -1))
        self.pw_lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Password", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "Login", None, -1))
        self.reg_label.setText(QtWidgets.QApplication.translate("Form", "Don\'t have an account ?", None, -1))


