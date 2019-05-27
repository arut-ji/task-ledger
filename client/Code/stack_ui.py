import sys

from PySide2.QtCore import QRect
from PySide2.QtWidgets import QWidget, QStackedWidget, QApplication

import client.Code.ui_to_py.landing_page_ui as landing
import client.Code.ui_to_py.login_ui as login
import client.Code.ui_to_py.register_ui as reg
import client.Code.ui_to_py.main_ui as main
import client.Code.ui_to_py.dialog_ui as dialog

import client.Code.controller.auth as task_auth
import client.Code.controller.manager as task_manager

class Task_ledger(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1000, 600)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setGeometry(QRect(0, 0, 1000, 600))
        self.stackedWidget.setObjectName("stackedWidget")

        #Landing Page
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.landing = landing.Ui_TaskLedger(self.stackedWidgetPage1)
        self.landing.setGeometry(0, 0, 1000, 60)
        self.landing.setupUi(self.stackedWidgetPage1)
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.landing.pushButton.clicked.connect(self.goto_login)

        #Login Page
        self.stackedWidgetPage2 = QWidget()
        self.stackedWidgetPage2.setObjectName("stackedWidgetPage2")
        self.login = login.Ui_Form(self.stackedWidgetPage2)
        self.login.setupUi(self.stackedWidgetPage2)
        self.login.setGeometry(0, 0, 1000, 60)
        self.login.reg_label.clicked.connect(self.goto_reg)
        self.login.back.clicked.connect(self.goto_landing)
        self.stackedWidget.addWidget(self.stackedWidgetPage2)

        #register Page
        self.stackedWidgetPage3 = QWidget()
        self.stackedWidgetPage3.setObjectName("stackedWidgetPage3")
        self.reg = reg.Ui_Form(self.stackedWidgetPage3)
        self.reg.setupUi(self.stackedWidgetPage3)
        self.reg.setGeometry(0, 0, 1000, 600)
        self.reg.back.clicked.connect(self.goto_login)
        self.stackedWidget.addWidget(self.stackedWidgetPage3)

        #main
        self.stackedWidgetPage4 = QWidget()
        self.stackedWidgetPage4.setObjectName("stackedWidgetPage4")
        self.main = main.Ui_Form(self.stackedWidgetPage4)
        self.main.setupUi(self.stackedWidgetPage4)
        self.main.setGeometry(0, 0, 1000, 600)
        self.main.create_button.clicked.connect(self.create_dialog)
        self.main.log_out.clicked.connect(self.goto_landing)
        self.stackedWidget.addWidget(self.stackedWidgetPage4)

        self.stackedWidget.setCurrentIndex(0)

    def goto_landing(self):
        self.stackedWidget.setCurrentIndex(0)

    def goto_login(self):
        self.stackedWidget.setCurrentIndex(1)

    def goto_reg(self):
        self.stackedWidget.setCurrentIndex(2)

    def goto_main(self):
        self.stackedWidget.setCurrentIndex(3)

    def create_dialog(self):
        self.dialog = dialog.Ui_Dialog()
        self.dialog.setupUi(self)
        self.show()


class LoginUI(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.manager = task_manager.TaskLedgerSystem()
        self.user_auth = task_auth.UserAuth()

        self.ui = Task_ledger()
        self.ui.setupUi(self)

        self.ui.login.button_login.clicked.connect(self.login_event)
        self.ui.reg.reg_button.clicked.connect(self.register_event)

        self.show()

    def login_event(self):
        username = self.ui.login.username_lineEdit.text()
        password = self.ui.login.pw_lineEdit.text()

        success = self.user_auth.login(username, password)
        if success:
            self.ui.goto_main()

    def register_event(self):
        username = self.ui.reg.username_lineEdit.text()
        password1 = self.ui.reg.pw_lineEdit.text()
        password2 = self.ui.reg.re_pw_lineEdit.text()

        success = self.user_auth.registration(username, password1, password2)
        if success:
            self.ui.goto_main()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = LoginUI()
    sys.exit(app.exec_())
