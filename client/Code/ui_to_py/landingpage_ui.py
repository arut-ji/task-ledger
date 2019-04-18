# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Landing-page.ui',
# licensing of 'Landing-page.ui' applies.
#
# Created: Thu Apr 18 14:03:40 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_TaskLedger(object):
    def setupUi(self, TaskLedger):
        TaskLedger.setObjectName("TaskLedger")
        TaskLedger.resize(1000, 600)
        TaskLedger.setMinimumSize(QtCore.QSize(1000, 600))
        TaskLedger.setMaximumSize(QtCore.QSize(1000, 600))
        TaskLedger.setBaseSize(QtCore.QSize(1000, 600))
        TaskLedger.setStyleSheet("QWidget{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: transparent;\n"
"    border: 1px solid #361A17;\n"
"    color: #361A17;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(40, 19, 18);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 8px;\n"
"}")
        self.landing_graphic = QtWidgets.QLabel(TaskLedger)
        self.landing_graphic.setGeometry(QtCore.QRect(90, 170, 359, 264))
        self.landing_graphic.setMinimumSize(QtCore.QSize(359, 264))
        self.landing_graphic.setMaximumSize(QtCore.QSize(359, 264))
        self.landing_graphic.setStyleSheet("")
        self.landing_graphic.setText("")
        self.landing_graphic.setPixmap(QtGui.QPixmap(":/graphic/graphic_landing.png"))
        self.landing_graphic.setScaledContents(True)
        self.landing_graphic.setWordWrap(False)
        self.landing_graphic.setObjectName("landing_graphic")
        self.bg = QtWidgets.QLabel(TaskLedger)
        self.bg.setGeometry(QtCore.QRect(480, 90, 435, 421))
        self.bg.setMinimumSize(QtCore.QSize(435, 300))
        self.bg.setMaximumSize(QtCore.QSize(435, 500))
        self.bg.setAutoFillBackground(False)
        self.bg.setStyleSheet("background-color: rgb(242, 247, 247);")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.logo = QtWidgets.QLabel(TaskLedger)
        self.logo.setGeometry(QtCore.QRect(520, 150, 220, 50))
        self.logo.setMinimumSize(QtCore.QSize(220, 50))
        self.logo.setMaximumSize(QtCore.QSize(220, 50))
        self.logo.setStyleSheet("background-color: transparent;")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/logo/TaskLedger_logoText-03.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.textEdit = QtWidgets.QTextEdit(TaskLedger)
        self.textEdit.setGeometry(QtCore.QRect(520, 230, 351, 151))
        self.textEdit.setStyleSheet("background-color: transparent;\n"
"color: rgb(40, 19, 18);")
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textEdit.setReadOnly(True)
        self.textEdit.setCursorWidth(0)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(TaskLedger)
        self.pushButton.setGeometry(QtCore.QRect(520, 400, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(TaskLedger)
        QtCore.QMetaObject.connectSlotsByName(TaskLedger)

    def retranslateUi(self, TaskLedger):
        TaskLedger.setWindowTitle(QtWidgets.QApplication.translate("TaskLedger", "Task Ledger", None, -1))
        self.textEdit.setHtml(QtWidgets.QApplication.translate("TaskLedger", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Roboto\'; font-size:16pt;\">In hac habitasse platea dictumst. Vivamus adipiscing fermentum quam volutpat aliquam. Integer et elit eget elit facilisis tristique. Nam vel iaculis mauris. Sed ullamcorper </span></p></body></html>", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("TaskLedger", "Get Started !", None, -1))


