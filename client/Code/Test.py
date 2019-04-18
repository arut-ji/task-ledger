import sys

from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Code.ui_to_py.cal_ui import Ui_Form

#TODO::Error
class LoginUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.ui = Ui_Form()
        self.ui.setupUi(self)




        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = LoginUI()
    sys.exit(app.exec_())

