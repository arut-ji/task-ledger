import sys

from PySide2.QtGui import *
from Code.ui_to_py.landingpage_ui import Ui_TaskLedger
from Code.stylesheet import *


class LandingPageUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.ui = Ui_TaskLedger()
        self.ui.setupUi(self)

        self.ui.landing_graphic.setPixmap(QPixmap("../Assets/graphic_landing.png"))
        self.ui.logo.setPixmap(QPixmap('../Assets/logo.png'))

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = LandingPageUI()
    sys.exit(app.exec_())