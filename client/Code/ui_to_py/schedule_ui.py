# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'schedule.ui',
# licensing of 'schedule.ui' applies.
#
# Created: Fri Apr 19 21:00:58 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        Form.setFont(font)
        Form.setStyleSheet("QWidget{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color: transparent;\n"
"    color: rgb(40, 19, 18)\n"
"}\n"
"QLabel#today_label{\n"
"    color: rgb(231, 119, 32);\n"
"}\n"
"QLabel:hover#left_arrow, :hover#right_arrow{\n"
"    background-color: rgb(244,244,244);\n"
"    border-radius: 20px;\n"
"}\n"
"QLabel:hover#schedule,:hover#calendar,:hover#history,:hover#statistic,:hover#notification{\n"
"    color: rgb(231, 119, 32);\n"
"    border-bottom: 1px solid rgb(224, 144, 66);\n"
"}\n"
"\n"
"QLabel:pressed#schedule,:pressed#calendar,:pressed#history,:pressed#statistic,:pressed#notification{\n"
"    color: rgb(231, 119, 32);\n"
"    border-bottom: 1px solid rgb(224, 144, 66);\n"
"}\n"
"\n"
"QPushButton#create_button{\n"
"    border-radius: 20px;\n"
"    background-color: rgb(40, 19, 18);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover#create_button{\n"
"    background-color: transparent;\n"
"    border: 1px solid #361A17;\n"
"    color: #361A17;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    background-color:transparent;\n"
"    color: black;\n"
"    spacing: 4px;\n"
"    outline: none;\n"
"    padding-top: 4px;\n"
"    padding-bottom: 4px;\n"
"}\n"
"\n"
"QCheckBox:focus {\n"
"    border: none;\n"
"}\n"
"\n"
"QCheckBox QWidget:disabled {\n"
"    background-color: transparent;\n"
"    color: #9B9B9B;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    margin-left: 4px;\n"
"    margin-right: 10px;\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(../Assets/checkbox_unchecked.png)\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QCheckBox::indicator:unchecked:focus,\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"    border: none;\n"
"    image: url(../Assets/checkbox/checkbox_checked_active.png)\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:disabled {\n"
"    image: url(../Assets/checkbox_checked.png)\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(../Assets/checkbox_checked.png)\n"
"}\n"
"QCheckBox::indicator:checked:hover,\n"
"QCheckBox::indicator:checked:focus,\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border: none;\n"
"    image: url(../Assets/checkbox_unchecked_active.png);\n"
"}\n"
"QCheckBox::indicator:checked:disabled{\n"
"    image: url(../Assets/checkbox_checked.png)\n"
"}\n"
"Line{\n"
"    color: rgb(201, 50, 41);\n"
"}\n"
"\n"
"QFrame[frameShape=\"4\"],\n"
"QFrame[frameShape=\"5\"]\n"
"{\n"
"    border: none;\n"
"    background: rgb(40, 19, 18);\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 274, 600))
        self.label.setStyleSheet("QWidget{\n"
"    background-color: rgb(242, 247, 247);\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(50, 30, 167, 38))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../Assets/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.create_button = QtWidgets.QPushButton(Form)
        self.create_button.setGeometry(QtCore.QRect(30, 100, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.create_button.setFont(font)
        self.create_button.setObjectName("create_button")
        self.schedule = QtWidgets.QLabel(Form)
        self.schedule.setGeometry(QtCore.QRect(30, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.schedule.setFont(font)
        self.schedule.setObjectName("schedule")
        self.calendar = QtWidgets.QLabel(Form)
        self.calendar.setGeometry(QtCore.QRect(30, 240, 89, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.calendar.setFont(font)
        self.calendar.setObjectName("calendar")
        self.history = QtWidgets.QLabel(Form)
        self.history.setGeometry(QtCore.QRect(30, 290, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.history.setFont(font)
        self.history.setObjectName("history")
        self.statistic = QtWidgets.QLabel(Form)
        self.statistic.setGeometry(QtCore.QRect(30, 340, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.statistic.setFont(font)
        self.statistic.setObjectName("statistic")
        self.notification = QtWidgets.QLabel(Form)
        self.notification.setGeometry(QtCore.QRect(30, 390, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.notification.setFont(font)
        self.notification.setObjectName("notification")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 550, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/setting/Downloads/settings-01.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.left_arrow = QtWidgets.QLabel(Form)
        self.left_arrow.setGeometry(QtCore.QRect(290, 60, 41, 41))
        self.left_arrow.setText("")
        self.left_arrow.setPixmap(QtGui.QPixmap("../Assets/arrow_left.png"))
        self.left_arrow.setScaledContents(True)
        self.left_arrow.setMargin(10)
        self.left_arrow.setObjectName("left_arrow")
        self.today_label = QtWidgets.QLabel(Form)
        self.today_label.setGeometry(QtCore.QRect(390, 25, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(32)
        self.today_label.setFont(font)
        self.today_label.setObjectName("today_label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(380, 65, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(42)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.right_arrow = QtWidgets.QLabel(Form)
        self.right_arrow.setGeometry(QtCore.QRect(340, 60, 41, 41))
        self.right_arrow.setText("")
        self.right_arrow.setPixmap(QtGui.QPixmap("../Assets/arrow_right.png"))
        self.right_arrow.setScaledContents(True)
        self.right_arrow.setMargin(10)
        self.right_arrow.setObjectName("right_arrow")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(350, 150, 271, 41))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(350, 200, 271, 41))
        self.checkBox_2.setObjectName("checkBox_2")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(360, 280, 215, 1))
        self.line.setStyleSheet("color: rgb(201, 50, 41);\n"
"border-color: rgb(32, 133, 61);\n"
"gridline-color: rgb(201, 50, 41);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.complete_label = QtWidgets.QLabel(Form)
        self.complete_label.setGeometry(QtCore.QRect(590, 270, 101, 25))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(20)
        self.complete_label.setFont(font)
        self.complete_label.setObjectName("complete_label")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(697, 280, 215, 1))
        self.line_2.setStyleSheet("color: rgb(201, 50, 41);\n"
"border-color: rgb(32, 133, 61);\n"
"gridline-color: rgb(201, 50, 41);")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(350, 370, 271, 41))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(350, 320, 271, 41))
        self.checkBox_4.setObjectName("checkBox_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.create_button.setText(QtWidgets.QApplication.translate("Form", "+ Create", None, -1))
        self.schedule.setText(QtWidgets.QApplication.translate("Form", "Schedule", None, -1))
        self.calendar.setText(QtWidgets.QApplication.translate("Form", "Calendar", None, -1))
        self.history.setText(QtWidgets.QApplication.translate("Form", "History", None, -1))
        self.statistic.setText(QtWidgets.QApplication.translate("Form", "Statistic", None, -1))
        self.notification.setText(QtWidgets.QApplication.translate("Form", "Notifications", None, -1))
        self.today_label.setText(QtWidgets.QApplication.translate("Form", "Today", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", " Mon 15 April", None, -1))
        self.checkBox.setText(QtWidgets.QApplication.translate("Form", "CheckBox", None, -1))
        self.checkBox_2.setText(QtWidgets.QApplication.translate("Form", "CheckBox", None, -1))
        self.complete_label.setText(QtWidgets.QApplication.translate("Form", "Completed ", None, -1))
        self.checkBox_3.setText(QtWidgets.QApplication.translate("Form", "CheckBox", None, -1))
        self.checkBox_4.setText(QtWidgets.QApplication.translate("Form", "CheckBox", None, -1))


