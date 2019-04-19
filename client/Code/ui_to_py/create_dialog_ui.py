# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_dialog.ui',
# licensing of 'create_dialog.ui' applies.
#
# Created: Fri Apr 19 10:02:33 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(463, 500)
        Form.setStyleSheet("QWidget{\n"
"    background-color: rgb(242, 247, 247);\n"
"    color: rgb(40, 19, 18);\n"
"}\n"
"QLineEdit#title{\n"
"    background-color: rgba(0,0,0,0%);\n"
"    border-bottom: 1px solid black;\n"
"    border-top: 0px;\n"
"    padding: 1px;\n"
"}\n"
"QPushButton#save_btn{\n"
"    background-color: rgb(242, 183, 54);\n"
"    color: rgb(40, 19, 18);\n"
"    border-radius: 10px\n"
"}\n"
"QPushButton:hover#save_btn{\n"
"    background-color: rgba(242, 183, 54, 95);\n"
"    color: rgb(40, 19, 18);\n"
"    border-radius: 10px\n"
"}\n"
"QPushButton#delete_btn{\n"
"    background-color: transparent;\n"
"    color: rgb(40, 19, 18);\n"
"    border: 1px solid #361A17;\n"
"    border-radius: 10px\n"
"}\n"
"QPushButton:hover#delete_btn{\n"
"    background-color: transparent;\n"
"    border: 1px solid  rgb(40, 19, 18);\n"
"    color: rgb(201, 50, 41);\n"
"}\n"
"QDateEdit{\n"
"    background-color: rgb(242, 247, 247);\n"
"    padding: 5px;\n"
"    border-color: transparent;\n"
"}\n"
"\n"
"QDateEdit, QComboBox{\n"
"    background-color: white;\n"
"    border-style: none;\n"
"    spacing: 5px; \n"
"}\n"
"\n"
"QDateEdit:drop-down, QComboBox:drop-down {\n"
"    image: url(../Assets/arrow_down.png);\n"
"    width: 25px;\n"
"    height: 10px;\n"
"    subcontrol-position: right center;\n"
"    subcontrol-origin: margin;\n"
"    background-color: white;\n"
"    border-style: none;\n"
"    spacing: 5px; \n"
"}\n"
"\n"
"QTimeEdit{\n"
"    background-color: white;\n"
"    border-style: none;\n"
"    spacing: 5px; \n"
"}\n"
"\n"
"QtimeEdit:drop-down {\n"
"    width: 25px;\n"
"    height: 10px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"    background-color: white;\n"
"    border-style: none;\n"
"    spacing: 5px; \n"
"}\n"
"\n"
"QLineEdit#location, QTextEdit{\n"
"    background-color: white;\n"
"    padding: 5px;\n"
"    border-style: none;\n"
"}\n"
"\n"
"")
        self.title = QtWidgets.QLineEdit(Form)
        self.title.setGeometry(QtCore.QRect(30, 30, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(21)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.save_btn = QtWidgets.QPushButton(Form)
        self.save_btn.setGeometry(QtCore.QRect(330, 30, 101, 30))
        self.save_btn.setObjectName("save_btn")
        self.from_dateEdit = QtWidgets.QDateEdit(Form)
        self.from_dateEdit.setGeometry(QtCore.QRect(30, 80, 101, 31))
        self.from_dateEdit.setAcceptDrops(False)
        self.from_dateEdit.setAutoFillBackground(False)
        self.from_dateEdit.setFrame(False)
        self.from_dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.from_dateEdit.setCalendarPopup(True)
        self.from_dateEdit.setObjectName("from_dateEdit")
        self.to_dateEdit = QtWidgets.QDateEdit(Form)
        self.to_dateEdit.setGeometry(QtCore.QRect(170, 80, 101, 31))
        self.to_dateEdit.setAcceptDrops(False)
        self.to_dateEdit.setAutoFillBackground(False)
        self.to_dateEdit.setFrame(False)
        self.to_dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.to_dateEdit.setCalendarPopup(True)
        self.to_dateEdit.setObjectName("to_dateEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 90, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.clock_icon = QtWidgets.QLabel(Form)
        self.clock_icon.setGeometry(QtCore.QRect(30, 130, 30, 30))
        self.clock_icon.setText("")
        self.clock_icon.setPixmap(QtGui.QPixmap("../Assets/clock.png"))
        self.clock_icon.setScaledContents(True)
        self.clock_icon.setObjectName("clock_icon")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 135, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(130, 130, 61, 28))
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit.setObjectName("timeEdit")
        self.location_icon = QtWidgets.QLabel(Form)
        self.location_icon.setGeometry(QtCore.QRect(30, 180, 30, 30))
        self.location_icon.setText("")
        self.location_icon.setPixmap(QtGui.QPixmap("../Assets/placeholder.png"))
        self.location_icon.setScaledContents(True)
        self.location_icon.setObjectName("location_icon")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 185, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.location = QtWidgets.QLineEdit(Form)
        self.location.setGeometry(QtCore.QRect(70, 220, 359, 28))
        self.location.setObjectName("location")
        self.noti_icon = QtWidgets.QLabel(Form)
        self.noti_icon.setGeometry(QtCore.QRect(30, 270, 30, 30))
        self.noti_icon.setText("")
        self.noti_icon.setPixmap(QtGui.QPixmap("../Assets/ring.png"))
        self.noti_icon.setScaledContents(True)
        self.noti_icon.setObjectName("noti_icon")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 275, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(190, 275, 161, 26))
        self.comboBox.setObjectName("comboBox")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 320, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(30, 350, 401, 114))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.title.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Title", None, -1))
        self.save_btn.setText(QtWidgets.QApplication.translate("Form", "SAVE", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "to", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "Time", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Location", None, -1))
        self.location.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Add Location", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "Notifications", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Form", "Descriptions", None, -1))
        self.textEdit.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Add Description", None, -1))


