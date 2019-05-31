import PySide2
from PySide2.QtWidgets import QWidget

from client.Code.controller.subjects.manager import Observable
from client.Code.ui_to_py.calendar_ui import CalendarWidget
import client.Code.ui_to_py.Statistics_ui as statistics
import client.Code.ui_to_py.schedule_ui as schedule
import client.Code.ui_to_py.history_ui as history
import client.Code.ui_to_py.side_navbar_ui as nav

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Form(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.system = None

    def set_system(self, system: Observable):
        self.system = system

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        font = QtGui.QFont()
        css_file = open('../Stylesheet/main_stylesheet.css').read()
        Form.setStyleSheet(css_file)
        font.setFamily("Helvetica")
        Form.setFont(font)

        # navbar
        self.navbar = nav.NavBarUI(Form)
        self.navbar.setupUI(Form)
        self.navbar.schedule.clicked.connect(self.display_sch)
        self.navbar.calendar.clicked.connect(self.display_cal)
        self.navbar.history.clicked.connect(self.display_his)
        self.navbar.statistic.clicked.connect(self.display_stat)
        self.navbar.notification.clicked.connect(self.display_noti)

        # stack area
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(280, 0, 721, 601))
        self.stackedWidget.setObjectName("stackedWidget")

        # schedule
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.schedule_ui = schedule.Schedule_ui(self.stackedWidgetPage1)
        self.schedule_ui.setupUi(self.stackedWidgetPage1)
        self.schedule_ui.bind_system(self.system)

        # Attach Observer to manager
        self.system.attach(self.schedule_ui)
        self.stackedWidget.addWidget(self.stackedWidgetPage1)

        # calendar
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.calendarWidget = CalendarWidget(self.page)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 80, 651, 391))
        self.calendarWidget.clicked.connect(self.display_sch)
        self.stackedWidget.addWidget(self.page)
        self.calendarWidget.bind_system(self.system)

        # history
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.history_ui = history.History_ui(self.page_2)
        self.history_ui.setupUi(self.page_2)
        
        # Attach history observer to manager
        self.system.attach(self.history_ui)
        self.stackedWidget.addWidget(self.page_2)

        # statistics
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.statistics = statistics.StatisticsUI(self.page_4)
        self.statistics.setupUI(self.page_4)
        self.stackedWidget.addWidget(self.page_4)

        # notification
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_noti = QtWidgets.QLabel(self.page_3)
        self.label_noti.setGeometry(QtCore.QRect(260, 40, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(42)
        self.label_noti.setFont(font)
        self.label_noti.setObjectName("stat_label_2")
        self.stackedWidget.addWidget(self.page_3)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label_noti.setText(QtWidgets.QApplication.translate("Form", "Notification", None, -1))

    def display_sch(self):
        self.schedule_ui.set_date(self.calendarWidget.get_selected_date())
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
