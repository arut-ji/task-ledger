from PySide2.QtWidgets import QWidget

from client.Code.ui_to_py.calendar_ui import CalendarWidget
from client.Code.ui_to_py.line_graph import TableWidget
import client.Code.ui_to_py.schedule_ui as schedule
import client.Code.controller.observers as task_observers
import client.Code.ui_to_py.history_ui as history

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        font = QtGui.QFont()
        css_file = open('../Stylesheet/main_stylesheet.css').read()
        Form.setStyleSheet(css_file)
        font.setFamily("Helvetica")
        Form.setFont(font)

        # navbar
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 274, 600))
        self.label.setStyleSheet("QWidget{ background-color: rgb(242, 247, 247);}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.schedule = QtWidgets.QPushButton(Form)
        self.schedule.setGeometry(QtCore.QRect(30, 190, 89, 32))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.schedule.setFont(font)
        self.schedule.setObjectName("schedule")
        self.schedule.clicked.connect(self.display_sch)
        self.calendar = QtWidgets.QPushButton(Form)
        self.calendar.setGeometry(QtCore.QRect(30, 240, 85, 32))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.calendar.setFont(font)
        self.calendar.setObjectName("calendar")
        self.calendar.clicked.connect(self.display_cal)
        self.history = QtWidgets.QPushButton(Form)
        self.history.setGeometry(QtCore.QRect(30, 290, 69, 32))
        self.history.clicked.connect(self.display_his)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.history.setFont(font)
        self.history.setObjectName("history")
        self.statistic = QtWidgets.QPushButton(Form)
        self.statistic.setGeometry(QtCore.QRect(30, 340, 77, 32))
        self.statistic.clicked.connect(self.display_stat)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.statistic.setFont(font)
        self.statistic.setObjectName("statistic")
        self.notification = QtWidgets.QPushButton(Form)
        self.notification.setGeometry(QtCore.QRect(30, 390, 109, 32))
        self.notification.clicked.connect(self.display_noti)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.notification.setFont(font)
        self.notification.setObjectName("notification")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(50, 30, 167, 38))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../Assets/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.create_button = QtWidgets.QPushButton(Form)
        self.create_button.setGeometry(QtCore.QRect(30, 100, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.create_button.setFont(font)
        self.create_button.setObjectName("create_button")
        self.log_out = QtWidgets.QPushButton(Form)
        self.log_out.setGeometry(QtCore.QRect(15, 545, 51, 51))
        self.log_out.setText("")
        self.log_out.setIcon(QtGui.QIcon("../Assets/logout.png"))
        self.log_out.setIconSize(QtCore.QSize(31, 31))
        self.log_out.setObjectName("logout")

        # stack area
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(280, 0, 721, 601))
        self.stackedWidget.setObjectName("stackedWidget")

        # schedule
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.schedule_ui = schedule.Schedule_ui(self.stackedWidgetPage1)
        self.schedule_ui.setupUi(self.stackedWidgetPage1)

        self.stackedWidget.addWidget(self.stackedWidgetPage1)

        # calendar
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.calendarWidget = CalendarWidget(self.page)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 80, 651, 391))
        self.stackedWidget.addWidget(self.page)

        # history
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.history_ui = history.History_ui(self.page_2)
        self.history_ui.setupUi(self.page_2)

        self.stackedWidget.addWidget(self.page_2)

        # statistics
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stat_label = QtWidgets.QLabel(self.page_4)
        self.stat_label.setGeometry(QtCore.QRect(280, 40, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(42)
        self.stat_label.setFont(font)
        self.stat_label.setObjectName("stat_label")

        self.stat_frame = QtWidgets.QFrame(self.page_4)
        self.stat_frame.setObjectName("stat_frame")
        self.stat_frame.setGeometry(20, 100, 671, 451)

        self.stat_graph = TableWidget(self.stat_frame)
        self.stat_graph.setGeometry(0, 0, 671, 451)
        self.stat_graph.show()
        self.stackedWidget.addWidget(self.page_4)

        # notification
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stat_label_2 = QtWidgets.QLabel(self.page_3)
        self.stat_label_2.setGeometry(QtCore.QRect(260, 40, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(42)
        self.stat_label_2.setFont(font)
        self.stat_label_2.setObjectName("stat_label_2")
        self.stackedWidget.addWidget(self.page_3)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.create_button.setText(QtWidgets.QApplication.translate("Form", "+ Create", None, -1))
        self.stat_label.setText(QtWidgets.QApplication.translate("Form", "Statistic", None, -1))
        self.stat_label_2.setText(QtWidgets.QApplication.translate("Form", "Notification", None, -1))
        self.schedule.setText(QtWidgets.QApplication.translate("Form", "Schedule", None, -1))
        self.calendar.setText(QtWidgets.QApplication.translate("Form", "Calendar", None, -1))
        self.history.setText(QtWidgets.QApplication.translate("Form", "History", None, -1))
        self.statistic.setText(QtWidgets.QApplication.translate("Form", "Statistic", None, -1))
        self.notification.setText(QtWidgets.QApplication.translate("Form", "Notification", None, -1))

    def display_sch(self):
        self.stackedWidget.setCurrentIndex(0)

    def display_cal(self):
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget.removeWidget(self)

    def display_his(self):
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget.removeWidget(self)

    def display_stat(self):
        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget.removeWidget(self)

    def display_noti(self):
        self.stackedWidget.setCurrentIndex(4)
        self.stackedWidget.removeWidget(self)
