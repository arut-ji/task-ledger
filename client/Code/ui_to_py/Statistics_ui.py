import datetime

from PySide2.QtCore import QRect, QSize
from PySide2.QtGui import QFont, QIcon, QPixmap
from PySide2.QtWidgets import (QWidget, QLabel, QPushButton, QComboBox, QTabWidget)
from client.Code.controller.observers.observers import ObserverWidget
from client.Code.ui_to_py.chart import BarChart, LineChart

class StatisticsUI(ObserverWidget):
    def __init__(self, parent=None):
        super(StatisticsUI, self).__init__(parent)
        self.task_list = None
        self.system = None

    def bind(self, system):
        self.system = system

    def setupUI(self, parent=None):
        self.stat_label = QLabel(parent)
        self.stat_label.setGeometry(QRect(280, 40, 200, 51))
        font = QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(42)
        self.stat_label.setFont(font)
        self.stat_label.setObjectName("stat_label")
        self.stat_label.setText("Statistics")

        self.tabWidget = QTabWidget(parent)
        self.tabWidget.setGeometry(QRect(20, 110, 671, 451))
        self.tabWidget.setObjectName("stat_frame")
        self.tab = QWidget()
        self.tab.setFont("Roboto Light")
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "Task Done")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab_2.setFont("Roboto Light")
        self.tabWidget.addTab(self.tab_2, "Karma Point")

        self.stat_graph = BarChart(self.tab)
        self.line_graph = LineChart(self.tab_2)

        self.stat_graph.setGeometry(0, 50, 671, 451)
        self.line_graph.setGeometry(0, 50, 671, 451)
        self.line_graph.show()
        self.stat_graph.show()

        self.left_arrow = QPushButton(self.tabWidget)
        self.left_arrow.setGeometry(QRect(50, 50, 41, 41))
        self.left_arrow.setText("")
        self.left_arrow.setIcon(QIcon("../Assets/arrow_left.png"))
        self.left_arrow.setFlat(True)
        self.left_arrow.setIconSize(QSize(21, 21))
        self.left_arrow.setObjectName("left_arrow")

        self.right_arrow = QPushButton(self.tabWidget)
        self.right_arrow.setGeometry(QRect(100, 50, 41, 41))
        self.right_arrow.setText("")
        self.right_arrow.setIcon(QIcon("../Assets/arrow_right.png"))
        self.right_arrow.setFlat(True)
        self.right_arrow.setIconSize(QSize(21, 21))
        self.right_arrow.setObjectName("right_arrow")

        self.combo_box = QComboBox(self.tabWidget)
        self.combo_box.setGeometry(QRect(150, 50, 121, 36))
        self.combo_box.setFont("Roboto Light")
        self.combo_box.addItem("Weekly")
        self.combo_box.addItem("Monthly")
        self.combo_box.setCurrentIndex(0)

        self.btn_change = QPushButton(self.tabWidget)
        self.btn_change.setFont("Roboto Light")
        self.btn_change.setGeometry(QRect(300, 50, 121, 36))
        self.btn_change.setText("Change GRAPH")
        self.btn_change.clicked.connect(self.change_graph)
        self.btn_change.setObjectName("save_btn")

        self.label = QLabel(self.tab_2)
        self.label.setPixmap(QPixmap('../Assets/question.png'))
        self.label.setScaledContents(True)
        self.label.setGeometry(430, 40, 20, 20)

        str_tooltip = "Karma Points:\n" \
                      "Earn 5 points for complete tasks within the due date\n" \
                      "Lose 1 point per day when having tasks that are overdue."
        self.label.setToolTip(str_tooltip)

        self.left_arrow.clicked.connect(self.change_chart_backward)
        self.right_arrow.clicked.connect(self.change_chart_forward)

    def change_graph(self):
        if self.tabWidget.tabText(self.tabWidget.currentIndex()) == "Task Done":
            if self.combo_box.currentText() == 'Monthly':
                self.stat_graph.set_interval(31)
            else:
                self.stat_graph.set_interval(7)
        else:
            if self.combo_box.currentText() == 'Monthly':
                self.line_graph.set_interval(31)
            else:
                self.line_graph.set_interval(7)

    def update_data(self):
        self.task_list = self.system.get_task_list()
        self.stat_graph.update_chart(self.task_list, datetime.datetime.now())
        self.line_graph.update_chart(self.task_list, datetime.datetime.now())
        self.update()

    def change_chart_backward(self):
        if self.tabWidget.tabText(self.tabWidget.currentIndex()) == "Task Done":
            if self.combo_box.currentText() == 'Monthly':
                self.stat_graph.change_max_bound(-31)
            else:
                self.stat_graph.change_max_bound(-7)
        else:
            if self.combo_box.currentText() == 'Monthly':
                self.line_graph.change_max_bound(-31)
            else:
                self.line_graph.change_max_bound(-7)

    def change_chart_forward(self):
        if self.tabWidget.tabText(self.tabWidget.currentIndex()) == "Task Done":
            if self.combo_box.currentText() == 'Monthly':
                self.stat_graph.change_max_bound(31)
            else:
                self.stat_graph.change_max_bound(7)
        else:
            if self.combo_box.currentText() == 'Monthly':
                self.line_graph.change_max_bound(31)
            else:
                self.line_graph.change_max_bound(7)
