import sys

from PySide2.QtGui import *
from PySide2.QtWidgets import QWidget, QApplication

from client.Code.stack_ui import Task_ledger

class LandingPageUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.ui = Task_ledger()
        self.ui.setupUi(self)

        #set graphics
        # self.ui.landing_graphic.setPixmap(QPixmap("../Assets/graphic_landing.png"))
        # self.ui.logo.setPixmap(QPixmap('../Assets/logo.png'))

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = LandingPageUI()
    sys.exit(app.exec_())