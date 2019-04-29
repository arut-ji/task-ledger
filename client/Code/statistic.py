import sys

from PySide2.QtGui import *
from PySide2.QtWidgets import *
from client.Code.ui_to_py.statistic_ui import Ui_Form

#TODO:: hover
class StatisticUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = StatisticUI()
    sys.exit(app.exec_())

