from PySide2 import QtGui, QtWidgets
from PySide2.QtCore import Qt

class Reg_Dialog_Complete(QtWidgets.QDialog):
    def __init__(self, parent=None):
        self.movie_screen = QtWidgets.QLabel(self)
        ag_file = "../Assets/success.gif"
        self.movie = QtGui.QMovie(ag_file)
        self.label = QtWidgets.QLabel(self)
        self.okay = QtWidgets.QPushButton(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("dialog")
        Dialog.setFixedSize(340, 221)

        css_file = open('../Stylesheet/dialog_stylesheet.css').read()
        Dialog.setStyleSheet(css_file)

        self.movie_screen.setGeometry(140, 10, 100, 100)
        self.movie_screen.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                        QtWidgets.QSizePolicy.Expanding)

        self.movie.setCacheMode(QtGui.QMovie.CacheAll)
        self.movie.setSpeed(100)
        self.movie_screen.setMovie(self.movie)
        self.movie.start()

        self.label.setText("Register Completed !")
        self.label.setGeometry(80, 120, 200, 21)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(20)
        self.label.setFont(font)

        self.okay.setText("Yay")
        self.okay.setGeometry(120, 160, 101, 30)
        font.setPointSize(16)
        self.okay.setFont(font)
        self.okay.setObjectName("okay")

class Reg_Dialog_Error(QtWidgets.QDialog):
    def __init__(self, msg, parent=None):
        super(Reg_Dialog_Error, self).__init__(parent)
        self.length = len(msg)
        self.err_msg = msg
        self.label = QtWidgets.QLabel(self)
        self.okay = QtWidgets.QPushButton(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("dialog")
        Dialog.setFixedSize(340, 221 * self.length * 0.75)

        css_file = open('../Stylesheet/dialog_stylesheet.css').read()
        Dialog.setStyleSheet(css_file)

        self.text = ''
        for i in range(len(self.err_msg)):
            self.text = self.text + '\n\n' + self.err_msg[i]
        self.label.setText(self.text)
        self.label.setWordWrap(True)

        self.label.setGeometry(20, 0 , 290,  221 * self.length * 0.75 - 100)
        self.label.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(18)
        self.label.setFont(font)

        self.okay.setText("Try Again")
        self.okay.setGeometry(120, 160 * self.length * 0.75, 101, 30)
        font.setPointSize(16)
        self.okay.setFont(font)
        self.okay.setObjectName("okay")

