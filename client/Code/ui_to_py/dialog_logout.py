from PySide2 import QtGui, QtWidgets

class Logout_Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Logout_Dialog, self).__init__(parent)
        self.graphic = QtWidgets.QLabel(self)
        self.label = QtWidgets.QLabel(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("dialog")
        Dialog.setFixedSize(340, 221)

        css_file = open('../Stylesheet/dialog_stylesheet.css').read()
        Dialog.setStyleSheet(css_file)

        self.graphic.setPixmap(QtGui.QPixmap('../Assets/logout_confirm.png'))
        self.graphic.setGeometry(120, 10, 101, 100)
        self.graphic.setScaledContents(True)

        self.label.setText("Logout ?")
        self.label.setGeometry(135, 120, 200, 21)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(20)
        self.label.setFont(font)

        self.okay = QtWidgets.QPushButton(self)
        self.okay.setText("Yes")
        self.okay.setGeometry(50, 160, 101, 30)
        font.setPointSize(16)
        self.okay.setFont(font)
        self.okay.setObjectName("okay")

        self.no = QtWidgets.QPushButton(self)
        self.no.setText("No")
        self.no.setGeometry(190, 160, 101, 30)
        font.setPointSize(16)
        self.no.setFont(font)
        self.no.setObjectName("delete_btn")



