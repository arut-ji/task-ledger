from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QWidget


class LandingPageUI(QWidget):
    def __init__(self, parent=None):
        super(LandingPageUI, self).__init__(parent)
        self.landing_graphic = QtWidgets.QLabel(parent)
        self.bg = QtWidgets.QLabel(parent)
        self.logo = QtWidgets.QLabel(parent)
        self.textEdit = QtWidgets.QTextEdit(parent)
        self.pushButton = QtWidgets.QPushButton(parent)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)

        css_file = open('../Stylesheet/landing-page.css').read()
        Form.setStyleSheet(css_file)

        self.landing_graphic.setGeometry(QtCore.QRect(90, 170, 359, 264))
        self.landing_graphic.setMinimumSize(QtCore.QSize(359, 264))
        self.landing_graphic.setMaximumSize(QtCore.QSize(359, 264))
        self.landing_graphic.setStyleSheet("")
        self.landing_graphic.setText("")
        self.landing_graphic.setPixmap(QtGui.QPixmap("../Assets/graphic_landing.png"))
        self.landing_graphic.setScaledContents(True)
        self.landing_graphic.setWordWrap(False)
        self.landing_graphic.setObjectName("landing_graphic")

        self.bg.setGeometry(QtCore.QRect(480, 90, 435, 421))
        self.bg.setMinimumSize(QtCore.QSize(435, 300))
        self.bg.setMaximumSize(QtCore.QSize(435, 500))
        self.bg.setAutoFillBackground(False)
        self.bg.setText("")
        self.bg.setObjectName("bg")

        self.logo.setGeometry(QtCore.QRect(520, 150, 220, 50))
        self.logo.setMinimumSize(QtCore.QSize(220, 50))
        self.logo.setMaximumSize(QtCore.QSize(220, 50))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../Assets/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        self.textEdit.setGeometry(QtCore.QRect(520, 230, 351, 200))
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textEdit.setReadOnly(True)
        self.textEdit.setCursorWidth(0)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        text = "    TaskLedger is an application that allows you to manage " \
               "your schedule and view your past activities. " \
               "Completed tasks are kept to visualize your productivity levels. " \
               "\n    To get started, head on to the next page and " \
               "create an account if you haven’t done so yet!"
        self.textEdit.setText(text)
        self.textEdit.setObjectName("textEdit")

        self.pushButton.setGeometry(QtCore.QRect(520, 400, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.hide()

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Task Ledger", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "Get Started !", None, -1))


