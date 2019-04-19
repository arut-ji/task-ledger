import sys

from PySide2.QtWidgets import QWidget, QApplication
from client.Code.ui_to_py.create_dialog_ui import Ui_Form

#TODO::hover
class create_dialogUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = create_dialogUI()
    sys.exit(app.exec_())