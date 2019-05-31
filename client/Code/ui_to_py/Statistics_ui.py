import datetime
import math
import sys
from random import randrange

from PySide2.QtCore import QAbstractTableModel, QModelIndex, QRect, Qt, QSize
from PySide2.QtGui import QColor, QPainter, QFont, QPen, QIcon
from PySide2.QtWidgets import (QApplication, QHeaderView,
                               QTableView, QWidget, QVBoxLayout, QLabel, QFrame, QPushButton, QComboBox)
from PySide2.QtCharts import QtCharts

from client.Code.controller.models.models import TaskList
from client.Code.ui_to_py.bar_chart import BarChart


class StatisticsUI(QWidget):
    def __init__(self, parent=None):
        super(StatisticsUI, self).__init__(parent)
        self.task_list = None

    def setupUI(self, parent=None):
        self.stat_label = QLabel(parent)
        self.stat_label.setGeometry(QRect(280, 40, 200, 51))
        font = QFont()
        font.setFamily("Helvetica")
        font.setPointSize(42)
        self.stat_label.setFont(font)
        self.stat_label.setObjectName("stat_label")
        self.stat_label.setText("Statistics")

        self.stat_frame = QFrame(parent)
        self.stat_frame.setObjectName("stat_frame")
        self.stat_frame.setGeometry(20, 100, 671, 451)

        self.stat_graph = BarChart(self.stat_frame)
        self.stat_graph.setGeometry(0, 30, 671, 451)
        self.stat_graph.show()


        self.left_arrow = QPushButton(parent)
        self.left_arrow.setGeometry(QRect(50, 110, 41, 41))
        self.left_arrow.setText("")
        self.left_arrow.setIcon(QIcon("../Assets/arrow_left.png"))
        self.left_arrow.setFlat(True)
        self.left_arrow.setIconSize(QSize(21, 21))
        self.left_arrow.setObjectName("left_arrow")
        self.left_arrow.clicked.connect(self.change_chart_backward)

        self.right_arrow = QPushButton(parent)
        self.right_arrow.setGeometry(QRect(100, 110, 41, 41))
        self.right_arrow.setText("")
        self.right_arrow.setIcon(QIcon("../Assets/arrow_right.png"))
        self.right_arrow.setFlat(True)
        self.right_arrow.setIconSize(QSize(21, 21))
        self.right_arrow.setObjectName("right_arrow")
        self.right_arrow.clicked.connect(self.change_chart_forward)

        self.combo_box = QComboBox(parent)
        self.combo_box.setGeometry(QRect(150, 110, 121, 36))
        self.combo_box.addItem("Weekly")
        self.combo_box.addItem("Monthly")
        self.combo_box.setCurrentIndex(0)

        # if self.combo_box.currentData()

    def update_data(self, task_list: TaskList):
        self.task_list = task_list
        self.stat_graph.update_chart(task_list, datetime.datetime.now())
        self.update()

    def change_chart_backward(self):
        self.stat_graph.change_max_bound(-7)
        # self.stat_graph.update()

    def change_chart_forward(self):
        self.stat_graph.change_max_bound(7)
        # self.stat_graph.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TableWidget()
    w.show()
    sys.exit(app.exec_())
