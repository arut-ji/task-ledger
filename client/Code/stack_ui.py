import sys

from PySide2.QtCore import QRect
from PySide2.QtWidgets import QWidget, QStackedWidget, QApplication
import client.Code.ui_to_py.landing_page_ui as landing
import client.Code.ui_to_py.login_ui as login
import client.Code.ui_to_py.register_ui as reg
import client.Code.ui_to_py.main_ui as main
import client.Code.ui_to_py.dialog_ui as dialog

from client.Code.controller.subjects.manager import TaskLedgerSystem

DEBUG = True


class Task_ledger(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1000, 600)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setGeometry(QRect(0, 0, 1000, 600))
        self.stackedWidget.setObjectName("stackedWidget")

        # Landing Page
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.landing = landing.Ui_TaskLedger(self.stackedWidgetPage1)
        self.landing.setGeometry(0, 0, 1000, 60)
        self.landing.setupUi(self.stackedWidgetPage1)
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.landing.pushButton.clicked.connect(self.goto_login)

        # Login Page
        self.stackedWidgetPage2 = QWidget()
        self.stackedWidgetPage2.setObjectName("stackedWidgetPage2")
        self.login = login.Ui_Form(self.stackedWidgetPage2)
        self.login.setupUi(self.stackedWidgetPage2)
        self.login.setGeometry(0, 0, 1000, 60)
        self.login.reg_label.clicked.connect(self.goto_reg)
        self.login.back.clicked.connect(self.goto_landing)
        self.stackedWidget.addWidget(self.stackedWidgetPage2)

        # register Page
        self.stackedWidgetPage3 = QWidget()
        self.stackedWidgetPage3.setObjectName("stackedWidgetPage3")
        self.reg = reg.Ui_Form(self.stackedWidgetPage3)
        self.reg.setupUi(self.stackedWidgetPage3)
        self.reg.setGeometry(0, 0, 1000, 600)
        self.reg.back.clicked.connect(self.goto_login)
        self.stackedWidget.addWidget(self.stackedWidgetPage3)

        # main
        self.stackedWidgetPage4 = QWidget()
        self.stackedWidgetPage4.setObjectName("stackedWidgetPage4")
        self.main = main.Ui_Form(self.stackedWidgetPage4)
        self.main.setObservable(self.system)
        self.main.setupUi(self.stackedWidgetPage4)
        self.main.setGeometry(0, 0, 1000, 600)
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


mock_user = {
    "key": "6bdf6d2c610e585fd8584f2bc51127df87fcec71",
    "user": {
        "id": 1,
        "username": "admin",
        "email": "admin@admin.com"
    }
}


class TaskLedgerUI(QWidget):
    def __init__(self, application, parent=None):
        QWidget.__init__(self, parent)

        self.app = application
        self.system = TaskLedgerSystem()

        # Set up the UI and mapping the buttons
        self.ui = Task_ledger()
        self.ui.setupUi(self)

        self.system.attach(self.ui.main.schedule_ui)

        self.ui.login.button_login.clicked.connect(self.login_event)
        self.ui.reg.reg_button.clicked.connect(self.register_event)
        self.ui.main.create_button.clicked.connect(self.create_dialog)

        self.show()

    def login_event(self):
        username = self.ui.login.username_lineEdit.text()
        password = self.ui.login.pw_lineEdit.text()

        # Set system loading state
        self.system.set_loading(True)

        # Goto main page
        if self.system.login(username, password) and not DEBUG:
            self.system.set_loading(False)
            self.ui.goto_main()
        else:
            self.system.user = mock_user["user"]
            # self.system.token = mock_user["token"]
            self.ui.goto_main()
        self.system.set_loading(False)

    def register_event(self):
        username = self.ui.reg.username_lineEdit.text()
        password1 = self.ui.reg.pw_lineEdit.text()
        password2 = self.ui.reg.re_pw_lineEdit.text()

        # Set system loading state
        self.system.set_loading(True)

        if self.system.register(username, password1, password2):
            self.system.set_loading(False)
            self.ui.goto_main()
        self.system.set_loading(False)

    def create_dialog(self):
        self.dialog = dialog.Create_dialog()
        self.dialog.setupUi(self.ui)

        self.dialog.save_btn.clicked.connect(self.create_event)

        self.ui.show()

    def create_event(self):
        s_time = self.dialog.timeEdit.time()
        s_date = self.dialog.from_dateEdit.date()

        e_time = self.dialog.to_timeEdit.time()
        e_date = self.dialog.to_dateEdit.date()

        topic = self.dialog.title.text()

        description = self.dialog.textEdit_desc.toPlainText()
        start_date = s_date.toString("yyyy-MM-dd")
        end_date = e_date.toString("yyyy-MM-dd")
        start_time = s_time.toString()
        end_time = e_time.toString()
        status = False
        location = self.dialog.location.text()

        start_at = "{}T{}Z".format(start_date, start_time)
        end_at = "{}T{}Z".format(end_date, end_time)

        task_data = {
            "topic": topic,
            "description": description,
            "start_at": start_at,
            "end_at": end_at,
            "status": status,
            "location": location,
            "user": self.system.user["id"]
        }

        time_object = {
            "s_date": s_date,
            "e_date": e_date,
            "s_time": s_time,
            "e_time": e_time
        }

        self.system.create_task(task_data, time_object)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = TaskLedgerUI(app)
    sys.exit(app.exec_())
