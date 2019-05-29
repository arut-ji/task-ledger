from PySide2 import QtWidgets, QtCore, QtGui


class History_ui(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(History_ui, self).__init__(parent)

    def setupUi(self, parent=None):
        self.label_history = QtWidgets.QLabel(self.parent)
        self.label_history.setGeometry(QtCore.QRect(290, 40, 131, 51))
        self.label_history.setText("History")
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(42)
        self.label_history.setFont(font)
        self.label_history.setObjectName("label_4")

