import datetime

from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt
from PySide2.QtGui import QPainter, QColor, QPen
from PySide2.QtWidgets import QWidget, QVBoxLayout

from client.Code.controller.models.models import TaskList
from client.Code.utility.parsers import TaskAnalyser, DatetimeParser


class BarChart(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        bar_set = QtCharts.QBarSet("ME")
        bar_set.setColor(QColor(231, 119, 32))
        self.task_list = None
        self.setFont("Roboto Light")

        self.max_bound: datetime = datetime.datetime.now()

        self.setFixedSize(651, 421)
        self.interval = 7

        self.series = QtCharts.QBarSeries()
        self.chart = QtCharts.QChart()
        self.chart.addSeries(self.series)
        self.chart.setFont("Roboto Light")
        self.chart.setTitle("Task Done")
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        self.axisX = QtCharts.QBarCategoryAxis()
        self.axisY = QtCharts.QValueAxis()

        self.chart.setAxisY(self.axisY, self.series)
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

    def set_interval(self, interval):
        self.interval = interval
        self.update_chart(self.task_list)

    def set_max_bound(self, max_bound_date):
        self.max_bound = max_bound_date
        self.update_chart(self.task_list)

    def change_max_bound(self, offset: int):
        if offset > 0:
            self.max_bound += datetime.timedelta(days=offset)
        else:
            self.max_bound -= datetime.timedelta(days=-offset)

        self.update_chart(self.task_list)

    def update_chart(self, task_list: TaskList, current_date=None):
        self.axisX.clear()
        self.series.clear()
        self.task_list = task_list

        result = TaskAnalyser.countDoneTaskFromInteval(task_list, self.max_bound, self.interval)

        self.axisX.append(
            [
                self.date_to_string(self.max_bound - datetime.timedelta(days=i)) for i in range(self.interval - 1, - 1, -1)
            ]
        )

        self.axisY.setRange(min(result), max(result) + max(result) * 0.3)

        bar_set = QtCharts.QBarSet("Done tasks in each day")
        bar_set.setColor(QColor(231, 119, 32))
        bar_set.append(result)
        self.series.append(bar_set)
        self.update()

    def date_to_string(self, date):
        return date.strftime("%d") + ' ' + date.strftime("%b")

class LineChart(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.series = QtCharts.QLineSeries()
        self.series.setName("Karma points")

        self.task_list = None
        self.max_bound: datetime = datetime.datetime.now()
        self.interval = 7
        self.karma_point = 0

        self.chart = QtCharts.QChart()
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.chart.addSeries(self.series)
        self.chart.setTitle("Karma Points")
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        self.axisX = QtCharts.QDateTimeAxis()
        self.axisX.setFormat("dd MMM")
        self.axisX.setTickCount(self.interval)
        self.axisY = QtCharts.QValueAxis()

        self.chart.setAxisX(self.axisX, self.series)
        self.chart.setAxisY(self.axisY, self.series)

        self.chartView = QtCharts.QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.chartView)
        self.setLayout(self.main_layout)
        self.setFixedSize(651, 421)


    def set_interval(self, interval):
        self.interval = interval
        self.update_chart(self.task_list)

    def set_max_bound(self, max_bound_date):
        self.max_bound = max_bound_date
        self.update_chart(self.task_list)

    def change_max_bound(self, offset: int):
        if offset > 0:
            self.max_bound += datetime.timedelta(days=offset)
        else:
            self.max_bound -= datetime.timedelta(days=-offset)
        self.update_chart(self.task_list)

    def update_chart(self, task_list, current_date=None):
        self.chart.removeSeries(self.series)
        self.task_list = task_list

        result = TaskAnalyser.getPointFromTasks(self.task_list, self.max_bound, self.interval)
        self.axisX.setMin(self.max_bound - datetime.timedelta(days=self.interval-1))
        self.axisY.setRange(min(result), max(result))

        self.qdate = DatetimeParser.fromDateToQDate(str(self.max_bound.date()))
        self.axisX.setMax(self.max_bound)

        self.series = QtCharts.QLineSeries()
        self.series.setName("Karma points")
        self.axisX.setTickCount(self.interval)
        result.reverse()

        for i in range(len(result)):
            self.series.append(self.qdate.addDays(-self.interval-1-i).toMSecsSinceEpoch(), result[i])

        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(242, 183, 54))
        pen.setCapStyle(Qt.RoundCap)
        self.series.setPen(pen)
        self.chart.addSeries(self.series)
        self.update()

