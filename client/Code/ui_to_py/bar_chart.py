import datetime
import sys

from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt
from PySide2.QtGui import QPainter, QColor
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout

from client.Code.controller.models.models import TaskList


class BarChart(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        bar_set = QtCharts.QBarSet("ME")
        bar_set.setColor(QColor(231, 119, 32))
        self.task_list = None

        self.max_bound: datetime = None
        self.min_bound: datetime = None

        self.setFixedSize(651, 431)

        # for i in range(len(self.lst)):
        #     bar_set.append(self.lst[i])

        self.series = QtCharts.QBarSeries()
        self.series.append(bar_set)

        self.chart = QtCharts.QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Karma Points")
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        self.axisX = QtCharts.QBarCategoryAxis()
        # self.update_chart(datetime.date.today())
        # print(self.date_now - datetime.timedelta(days=6))

        self.chart.createDefaultAxes()
        self.chart.setAxisX(self.axisX, self.series)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chartView = QtCharts.QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.chartView)
        self.setLayout(self.main_layout)

    def set_task_list(self, task_list):
        self.task_list = task_list

    def set_max_bound(self, max_bound_date):
        self.max_bound = max_bound_date
        self.update_chart(task_list=self.task_list)

    def change_max_bound(self, offset: int):
        if offset > 0:
            self.max_bound += datetime.timedelta(days=offset)
        else:
            self.max_bound -= datetime.timedelta(days=-offset)
        self.update_chart(self.task_list)

    def update_chart(self, task_list: TaskList, current_date=None):
        self.axisX.clear()
        if current_date is not None:
            self.max_bound = current_date


        self.axisX.append([self.date_to_string(self.max_bound - datetime.timedelta(days=6)),
                           self.date_to_string(self.max_bound - datetime.timedelta(days=5)),
                           self.date_to_string(self.max_bound - datetime.timedelta(days=4)),
                           self.date_to_string(self.max_bound - datetime.timedelta(days=3)),
                           self.date_to_string(self.max_bound - datetime.timedelta(days=2)),
                           self.date_to_string(self.max_bound - datetime.timedelta(days=1)),
                           self.date_to_string(self.max_bound)])
        self.update()

    def date_to_string(self, date):
        return date.strftime("%d") + ' ' + date.strftime("%b")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = BarChart([0, 1, -1, -9, 2, 3, -2])
    w.show()
    sys.exit(app.exec_())
