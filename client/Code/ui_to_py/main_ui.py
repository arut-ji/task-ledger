from PySide2.QtWidgets import QWidget

from client.Code.controller.subjects.subjects import Observable
from client.Code.ui_to_py.calendar_ui import CalendarWidget
import client.Code.ui_to_py.Statistics_ui as statistics
import client.Code.ui_to_py.schedule_ui as schedule
import client.Code.ui_to_py.history_ui as history
import client.Code.ui_to_py.side_navbar_ui as nav
from PySide2 import QtCore, QtGui, QtWidgets

from client.Code.utility.parsers import DatetimeParser

class MainUI(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.system = None
        self.navbar = nav.NavBarUI(parent)
        self.stackedWidget = QtWidgets.QStackedWidget(parent)
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.page = QtWidgets.QWidget()

    def bind_system(self, system: Observable):
        self.system = system

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        font = QtGui.QFont()
        css_file = open('../Stylesheet/main_stylesheet.css').read()
        Form.setStyleSheet(css_file)
        font.setFamily("Roboto Light")
        Form.setFont(font)

        # navbar
        self.navbar.setupUI(Form)
        self.navbar.schedule.clicked.connect(self.display_schedule)
        self.navbar.calendar.clicked.connect(self.display_calendar)
        self.navbar.history.clicked.connect(self.display_history)
        self.navbar.statistic.clicked.connect(self.display_statistics)

        # stack area
        self.stackedWidget.setGeometry(QtCore.QRect(280, 0, 721, 601))
        self.stackedWidget.setObjectName("stackedWidget")

        # schedule
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.schedule_ui = schedule.ScheduleUI(self.stackedWidgetPage1)
        self.schedule_ui.setupUi(self.stackedWidgetPage1)
        self.schedule_ui.bind(self.system)

        # Attach Observer to manager
        self.system.attach(self.schedule_ui)
        self.stackedWidget.addWidget(self.stackedWidgetPage1)

        # calendar
        self.page.setObjectName("page")
        self.calendarWidget = CalendarWidget(self.page)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 80, 651, 391))
        self.calendarWidget.clicked.connect(self.display_schedule)
        self.stackedWidget.addWidget(self.page)
        self.calendarWidget.bind(self.system)

        # history
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.history_ui = history.HistoryUI(self.page_2)
        self.history_ui.setupUi(self.page_2)
        self.history_ui.bind(self.system)

        
        # Attach history observer to manager
        self.system.attach(self.history_ui)
        self.stackedWidget.addWidget(self.page_2)

        # statistics
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.statistics = statistics.StatisticsUI(self.page_4)
        self.statistics.setupUI(self.page_4)
        self.statistics.bind(self.system)

        # Attach statistics observer to manager
        self.system.attach(self.statistics)
        self.stackedWidget.addWidget(self.page_4)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))

    def display_schedule(self):
        self.schedule_ui.set_date(self.calendarWidget.get_selected_date())
        selected_date = DatetimeParser.dateToDatetime(
            self.calendarWidget.get_selected_date()
        )

        self.statistics.stat_graph.set_max_bound(selected_date)
        self.stackedWidget.setCurrentIndex(0)

    def display_calendar(self):
        self.stackedWidget.setCurrentIndex(1)

    def display_history(self):
        self.stackedWidget.setCurrentIndex(2)

    def display_statistics(self):
        self.stackedWidget.setCurrentIndex(3)
