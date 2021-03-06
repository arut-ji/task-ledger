import sys

from PySide2.QtCore import QRect
from PySide2.QtWidgets import QWidget, QStackedWidget, QApplication, QLabel
import client.Code.ui_to_py.landing_page_ui as landing
import client.Code.ui_to_py.login_ui as login
import client.Code.ui_to_py.register_ui as reg
import client.Code.ui_to_py.main_ui as main
import client.Code.ui_to_py.dialog_ui as dialog
import client.Code.ui_to_py.dialog_reg as dialog_reg
import client.Code.ui_to_py.dialog_logout as dialog_logout

from client.Code.controller.subjects.subjects import TaskLedgerSystem
from client.Code.utility.parsers import DatetimeParser

DEBUG = False
error_stylesheet = "border-color: red; color: red;"
normal_stylesheet = "border-color: black; color: black;"

class Task_ledger(QWidget):
    def __init__(self, system, parent=None):
        super(Task_ledger, self).__init__(parent)
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage2 = QWidget()
        self.stackedWidgetPage3 = QWidget()
        self.stackedWidgetPage4 = QWidget()
        self.dialog = dialog_logout.Logout_Dialog()

        self.system = system

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(1000, 600)
        Form.setWindowTitle("Task Ledger")

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setGeometry(QRect(0, 0, 1000, 600))
        self.stackedWidget.setObjectName("stackedWidget")

        # Landing Page
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.landing = landing.LandingPageUI(self.stackedWidgetPage1)
        self.landing.setGeometry(0, 0, 1000, 60)
        self.landing.setupUi(self.stackedWidgetPage1)
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.landing.pushButton.clicked.connect(self.goto_login)

        # Login Page
        self.stackedWidgetPage2.setObjectName("stackedWidgetPage2")
        self.login = login.LoginUI(self.stackedWidgetPage2)
        self.login.setupUi(self.stackedWidgetPage2)
        self.login.setGeometry(0, 0, 1000, 60)
        self.login.reg_label.clicked.connect(self.goto_reg)
        self.login.back.clicked.connect(self.goto_landing)
        self.stackedWidget.addWidget(self.stackedWidgetPage2)

        # register Page
        self.stackedWidgetPage3.setObjectName("stackedWidgetPage3")
        self.reg = reg.RegisterUI(self.stackedWidgetPage3)
        self.reg.setupUi(self.stackedWidgetPage3)
        self.reg.setGeometry(0, 0, 1000, 600)
        self.reg.back.clicked.connect(self.goto_login)
        self.stackedWidget.addWidget(self.stackedWidgetPage3)

        # main
        self.stackedWidgetPage4.setObjectName("stackedWidgetPage4")
        self.main = main.MainUI(self.stackedWidgetPage4)
        # Pass system object to the child Widget
        self.main.bind_system(self.system)
        self.main.setupUi(self.stackedWidgetPage4)
        self.main.setGeometry(0, 0, 1000, 600)
        self.main.navbar.log_out.clicked.connect(self.logout)
        self.stackedWidget.addWidget(self.stackedWidgetPage4)

        self.stackedWidget.setCurrentIndex(0)

    def logout(self):
        self.dialog.setupUi(self.dialog)
        self.dialog.okay.clicked.connect(self.goto_landing)
        self.dialog.okay.clicked.connect(self.dialog.close)
        self.dialog.no.clicked.connect(self.dialog.close)
        self.dialog.show()

    def goto_landing(self):
        self.stackedWidget.setCurrentIndex(0)

    def goto_login(self):
        self.stackedWidget.setCurrentIndex(1)

    def goto_reg(self):
        self.stackedWidget.setCurrentIndex(2)

    def goto_main(self):
        self.stackedWidget.setCurrentIndex(3)

class TaskLedgerUI(QWidget):
    def __init__(self, application, parent=None):
        QWidget.__init__(self, parent)

        self.app = application
        self.system = TaskLedgerSystem()

        # Set up the UI and mapping the buttons
        self.ui = Task_ledger(self.system)
        self.ui.setupUi(self)

        self.system.attach(self.ui.main.schedule_ui)

        self.ui.login.button_login.clicked.connect(self.login_event)
        self.ui.reg.reg_button.clicked.connect(self.register_event)
        self.ui.main.navbar.create_button.clicked.connect(self.create_dialog)

        self.dialog = dialog.Create_dialog()

        self.show()

    def login_event(self):
        username = self.ui.login.username_lineEdit.text()
        password = self.ui.login.pw_lineEdit.text()

        # Set system loading state
        self.system.set_loading(True)

        # Goto main page
        if self.system.login(username, password):
            self.system.set_loading(False)
            self.ui.goto_main()
        else:
            self.ui.login.error_msg.setText("Invalid username or password")
            self.ui.login.username_lineEdit.setText("")
            self.ui.login.pw_lineEdit.setText("")
        self.system.set_loading(False)

    def register_event(self):
        username = self.ui.reg.username_lineEdit.text()
        password1 = self.ui.reg.pw_lineEdit.text()
        password2 = self.ui.reg.re_pw_lineEdit.text()

        # Set system loading state
        self.system.set_loading(True)

        result = self.system.register(username, password1, password2)
        if len(result.values()) == 0:
            self.system.set_loading(False)
            self.dialog = dialog_reg.Reg_Dialog_Complete()
            self.dialog.setupUi(self.dialog)
            self.dialog.okay.clicked.connect(self.ui.goto_login)
            self.dialog.okay.clicked.connect(self.dialog.close)
            self.dialog.show()
        else:
            # dialog
            error_messages = []
            for message in result.values():
                error_messages += message

            self.dialog = dialog_reg.Reg_Dialog_Error(error_messages)
            self.dialog.setupUi(self.dialog)
            self.dialog.okay.clicked.connect(self.dialog.close)
            self.dialog.show()

            self.ui.reg.username_lineEdit.setText("")
            self.ui.reg.line_id_lineEdit.setText("")
            self.ui.reg.pw_lineEdit.setText("")
            self.ui.reg.re_pw_lineEdit.setText("")

        self.system.set_loading(False)

    def create_dialog(self):
        create_fragment = dialog.Create_dialog()
        create_fragment.setupUi(create_fragment)
        create_fragment.title.setText('')
        create_fragment.save_btn.clicked.connect(lambda: self.create_event(create_fragment))
        create_fragment.show()

    def create_event(self, fragment):
        start_time = fragment.timeEdit.time()
        start_date = fragment.from_dateEdit.date()

        end_time = fragment.to_timeEdit.time()
        end_date = fragment.to_dateEdit.date()

        topic = fragment.title.text()

        description = fragment.textEdit_desc.toPlainText()
        status = False
        location = fragment.location.text()

        start_at = DatetimeParser.fromQDateAndQTime(start_date, start_time)
        end_at = DatetimeParser.fromQDateAndQTime(end_date, end_time)

        details = {
            "topic": topic,
            "description": description,
            "start_at": str(start_at),
            "end_at": str(end_at),
            "status": status,
            "location": location,
        }

        if self.system.create_task(details):
            fragment.close()
        else:
            if topic == '':
                fragment.title.setStyleSheet(error_stylesheet)
            else:
                fragment.title.setStyleSheet(normal_stylesheet)

            if start_at.date() > end_at.date():
                fragment.to_dateEdit.setStyleSheet(error_stylesheet)
                fragment.from_dateEdit.setStyleSheet(error_stylesheet)

            else:
                fragment.to_dateEdit.setStyleSheet(normal_stylesheet)
                fragment.from_dateEdit.setStyleSheet(normal_stylesheet)

            if start_time >= end_time:
                fragment.timeEdit.setStyleSheet(error_stylesheet)
                fragment.to_timeEdit.setStyleSheet(error_stylesheet)
            else:
                fragment.timeEdit.setStyleSheet(normal_stylesheet)
                fragment.to_timeEdit.setStyleSheet(normal_stylesheet)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = TaskLedgerUI(app)
    sys.exit(app.exec_())
