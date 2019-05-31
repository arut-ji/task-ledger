import sys

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication


class Logout_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("dialog")
        Dialog.setFixedSize(340, 221)

        css_file = open('../Stylesheet/dialog_stylesheet.css').read()
        Dialog.setStyleSheet(css_file)

        self.graphic = QtWidgets.QLabel(Dialog)
        self.graphic.setPixmap(QtGui.QPixmap('../Assets/logout_confirm.png'))
        self.graphic.setGeometry(120, 10, 101, 100)
        self.graphic.setScaledContents(True)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setText("Logout ?")
        self.label.setGeometry(135, 120, 200, 21)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(20)
        self.label.setFont(font)

        self.okay = QtWidgets.QPushButton(Dialog)
        self.okay.setText("Yes")
        self.okay.setGeometry(50, 160, 101, 30)
        font.setPointSize(16)
        self.okay.setFont(font)
        self.okay.setObjectName("okay")

        self.no = QtWidgets.QPushButton(Dialog)
        self.no.setText("No")
        self.no.setGeometry(190, 160, 101, 30)
        font.setPointSize(16)
        self.no.setFont(font)
        self.no.setObjectName("delete_btn")


class create_dialogUI(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self, None)

        self.ui = Logout_Dialog()
        self.ui.setupUi(self)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = create_dialogUI()
    sys.exit(app.exec_())


