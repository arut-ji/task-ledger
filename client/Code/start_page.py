from PySide2.QtCore import QSize
from PySide2.QtWidgets import QMainWindow, QWidget
import client.Code.ui_to_py.landingpage_ui as landing

class TaskLedger(QMainWindow):
    def __init__(self, parent=None):
        super(TaskLedger, self).__init__(parent)

        self.setWindowTitle('Task Ledger')

        self.landing_page = landing.Ui_TaskLedger(self)

        self.centralWidget = QWidget()
        self.centralWidget.setBaseSize(QSize(1000, 600))



