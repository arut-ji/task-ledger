from typing import List
from PySide2 import QtWidgets, QtCore, QtGui

from client.Code.controller.models.models import TaskList, Task

class HistoryUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(HistoryUI, self).__init__(parent)
        self.label_history = QtWidgets.QLabel(parent)
        self.tableWidget = QtWidgets.QTableWidget(parent)

    def setupUi(self, parent=None):
        self.label_history.setGeometry(QtCore.QRect(290, 40, 131, 51))
        self.label_history.setText("History")
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(42)
        self.label_history.setFont(font)
        self.label_history.setObjectName("label_4")

        self.tableWidget.setGeometry(QtCore.QRect(20, 100 , 661, 481))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem("Topic")
        item.setFont("Roboto Light")
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem("Start Date")
        item.setFont("Roboto Light")
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem("Start Time")
        item.setFont("Roboto Light")
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem("Done Date")
        item.setFont("Roboto Light")
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem("End Date")
        item.setFont("Roboto Light")
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem("End Time")
        item.setFont("Roboto Light")
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(108)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(27)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(25)

    def update_data(self, task_list: TaskList):
        task_list = task_list.get_task_list()
        inactive_task_list = list(
            filter(
                lambda task: task.status, task_list
            )
        )
        inactive_task_list.sort(key=lambda item: item.done_at)
        self.update_table(inactive_task_list)

        super(HistoryUI, self).update()

    def update_table(self, task_list: List[Task]):
        row_count = len(task_list)
        column_count = 6

        self.tableWidget.setRowCount(row_count)
        self.tableWidget.setColumnCount(column_count)

        for i in range(row_count):
            task = task_list[i]
            detail = [
                task.topic,
                str(task.start_at.date()),
                str(task.start_at.time()),
                str(task.done_at.date()),
                str(task.end_at.date()),
                str(task.end_at.time()),
            ]
            for k in range(6):
                if i % 2 == 0:
                    self.brush = QtGui.QBrush(QtGui.QColor(247, 249, 251))
                else:
                    self.brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))

                cell = QtWidgets.QTableWidgetItem()
                cell.setText(detail[k])
                cell.setForeground(self.brush)
                cell.setBackground(self.brush)
                cell.setTextColor(QtGui.QColor(40, 19, 18))
                self.tableWidget.setFont("Roboto Light")
                self.tableWidget.setItem(i - 1, k, cell)
