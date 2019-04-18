# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_cal.ui',
# licensing of 'test_cal.ui' applies.
#
# Created: Thu Apr 18 13:25:03 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 50, 312, 173))
        self.calendarWidget.setAutoFillBackground(False)
        self.calendarWidget.setStyleSheet("background-color: transparent;\n"
"border-bottom-color: transparent;\n"
"alternate-background-color: transparent;\n"
"selection-background-color: transparent;")
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setNavigationBarVisible(False)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))

