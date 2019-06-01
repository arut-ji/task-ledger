from PySide2 import QtCore, QtGui, QtWidgets

class RegisterUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(RegisterUI, self).__init__(parent)
        self.back = QtWidgets.QPushButton(parent)
        self.login_label = QtWidgets.QLabel(parent)
        self.username_lineEdit = QtWidgets.QLineEdit(parent)
        self.pw_lineEdit = QtWidgets.QLineEdit(parent)
        self.re_pw_lineEdit = QtWidgets.QLineEdit(parent)
        self.reg_button = QtWidgets.QPushButton(parent)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        Form.setAutoFillBackground(False)

        css_file = open('../Stylesheet/reg_stylesheet.css').read()
        Form.setStyleSheet(css_file)

        self.back.setIcon(QtGui.QIcon("../Assets/arrow_left.png"))
        self.back.setGeometry(10, 10, 41, 41)
        self.back.setIconSize(QtCore.QSize(21, 21))
        self.back.setObjectName("back")

        self.login_label.setGeometry(QtCore.QRect(410, 160, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(34)
        self.login_label.setFont(font)
        self.login_label.setAutoFillBackground(False)
        self.login_label.setStyleSheet("background-color: transparent;")
        self.login_label.setObjectName("login_label")

        self.username_lineEdit.setGeometry(QtCore.QRect(360, 220, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.username_lineEdit.setFont(font)
        self.username_lineEdit.setAutoFillBackground(False)
        self.username_lineEdit.setObjectName("username_lineEdit")

        self.pw_lineEdit.setGeometry(QtCore.QRect(360, 280, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.pw_lineEdit.setFont(font)
        self.pw_lineEdit.setAutoFillBackground(False)
        self.pw_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_lineEdit.setClearButtonEnabled(False)
        self.pw_lineEdit.setObjectName("pw_lineEdit")

        self.re_pw_lineEdit.setGeometry(QtCore.QRect(360, 340, 261, 31))
        self.re_pw_lineEdit.setFont(font)
        self.re_pw_lineEdit.setAutoFillBackground(False)
        self.re_pw_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.reg_button.setGeometry(QtCore.QRect(360, 400, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.reg_button.setFont(font)
        self.reg_button.setStyleSheet("")
        self.reg_button.setObjectName("reg_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.login_label.setText(QtWidgets.QApplication.translate("Form", "REGISTER", None, -1))
        self.username_lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Username", None, -1))
        self.pw_lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Password", None, -1))
        self.reg_button.setText(QtWidgets.QApplication.translate("Form", "Register", None, -1))
        self.re_pw_lineEdit.setPlaceholderText(QtWidgets.QApplication.translate("Form", "Password Confirmation", None, -1))

