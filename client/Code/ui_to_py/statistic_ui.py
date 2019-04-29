# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistic.ui',
# licensing of 'statistic.ui' applies.
#
# Created: Mon Apr 22 10:32:26 2019
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
"\n"
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
"QTabWidget{\n"
"    font-size: 20px;\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane{\n"
"    padding: 5px 10px 5px 10px;   \n"
"    border: 1px solid rgb(40, 19, 18);\n"
"    border-radius: 10px;\n"
"    position: absolute;\n"
"     top: -1em;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab{\n"
"    padding: 5px 20px 5px 20px;  \n"
"    border: 1px solid rgb(251, 166, 0); \n"
"    min-width: 100px\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: white;\n"
"    color: rgb(231, 119, 32);\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background: white;\n"
"}\n"
"\n"
"\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: rgb(242, 247, 247);\n"
"}\n"
"\n"
"QTabBar::tab:first{\n"
"    border-top-left-radius: 11px;\n"
"    border-bottom-left-radius: 11px;\n"
"}\n"
"\n"
"QTabBar::tab:last{\n"
"    border-top-right-radius: 11px;\n"
"    border-bottom-right-radius: 11px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
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
        self.label_2.setPixmap(QtGui.QPixmap("../Assets/settings.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(550, 50, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(42)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(300, 110, 671, 451))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.create_button.setText(QtWidgets.QApplication.translate("Form", "+ Create", None, -1))
        self.schedule.setText(QtWidgets.QApplication.translate("Form", "Schedule", None, -1))
        self.calendar.setText(QtWidgets.QApplication.translate("Form", "Calendar", None, -1))
        self.history.setText(QtWidgets.QApplication.translate("Form", "History", None, -1))
        self.statistic.setText(QtWidgets.QApplication.translate("Form", "Statistic", None, -1))
        self.notification.setText(QtWidgets.QApplication.translate("Form", "Notifications", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "Statistic", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("Form", "Weekly", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtWidgets.QApplication.translate("Form", "Monthly", None, -1))

