from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QPalette, QPixmap


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        Form.setMouseTracking(False)

        css_file = open('../Stylesheet/reg_stylesheet.css').read()
        Form.setStyleSheet(css_file)

        self.back = QtWidgets.QPushButton(Form)
        self.back.setIcon(QtGui.QIcon("../Assets/arrow_left.png"))
        self.back.setGeometry(10, 10, 41, 41)
        self.back.setIconSize(QtCore.QSize(21, 21))
        self.back.setObjectName("back")

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
        self.username_lineEdit.setStyleSheet("")
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
        self.button_login = QtWidgets.QPushButton(Form)
        self.button_login.setGeometry(QtCore.QRect(360, 370, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.button_login.setFont(font)
        self.button_login.setObjectName("button_login")
        self.reg_label = QtWidgets.QPushButton(Form)
        self.reg_label.setGeometry(QtCore.QRect(390, 420, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(19)
        self.reg_label.setFont(font)
        self.reg_label.setObjectName("reg_label")

        self.error_msg = QtWidgets.QLabel(Form)
        self.error_msg.setGeometry(QtCore.QRect(365, 330, 251, 31))
        self.error_msg.setObjectName("err_msg")
        font.setPointSize(18)
        self.error_msg.setFont(font)
        self.error_msg.setText("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.login_label.setText(QtWidgets.QApplication.translate("Form", "LOGIN", None, -1))
        self.username_lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Username", None, -1))
        self.pw_lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Password", None, -1))
        self.button_login.setText(QtWidgets.QApplication.translate("Form", "Login", None, -1))
        self.reg_label.setText(QtWidgets.QApplication.translate("Form", "Don\'t have an account ?", None, -1))



