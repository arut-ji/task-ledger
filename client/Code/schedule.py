import sys

from PySide2.QtWidgets import *
from client.Code.ui_to_py.schedule_ui import Ui_Form

#TODO::setting icon
class scheduleUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = scheduleUI()
    sys.exit(app.exec_())

