import sys

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication


class Reg_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("dialog")
        Dialog.setFixedSize(340, 221)

        css_file = open('../../Stylesheet/dialog_stylesheet.css').read()
        Dialog.setStyleSheet(css_file)

        self.movie_screen = QtWidgets.QLabel(Dialog)
        # self.movie_screen.setFixedSize(QtCore.QSize(80, 80))
        self.movie_screen.setGeometry(140, 10, 100, 100)
        self.movie_screen.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                        QtWidgets.QSizePolicy.Expanding)


        # main_layout = QtWidgets.QVBoxLayout()
        # main_layout.addWidget(self.movie_screen)
        # Dialog.setLayout(main_layout)


        ag_file = "../../Assets/success.gif"
        self.movie = QtGui.QMovie(ag_file)
        self.movie.setCacheMode(QtGui.QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.movie_screen.setMovie(self.movie)
        self.movie.start()

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setText("Register Completed !")
        self.label.setGeometry(80, 120, 200, 21)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(20)
        self.label.setFont(font)

        self.okay = QtWidgets.QPushButton(Dialog)
        self.okay.setText("Yay")
        self.okay.setGeometry(120, 160, 101, 30)
        font.setPointSize(16)
        self.okay.setFont(font)
        self.okay.setObjectName("okay")


class create_dialogUI(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self, None)

        self.ui = Reg_Dialog()
        self.ui.setupUi(self)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = create_dialogUI()
    sys.exit(app.exec_())


