import sys

from PySide2.QtGui import *
from PySide2.QtWidgets import *
from client.Code.ui_to_py.register_ui import Ui_Form

class RegisterUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        palette = QPalette()
        palette.setBrush(QPalette.Background, QPixmap('../Assets/login.png'))
        self.setPalette(palette)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = RegisterUI()
    sys.exit(app.exec_())

