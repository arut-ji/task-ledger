import datetime
import sys

from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt, QDateTime
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout
from PySide2 import QtCore


class BarChart(QWidget):
    def __init__(self, lst, parent=None):
        QWidget.__init__(self, parent)
        set_sun = QtCharts.QBarSet("ME")
        self.lst = lst

        self.setFixedSize(651, 431)

        for i in range(len(self.lst)):
            set_sun.append(self.lst[i])

        self.series = QtCharts.QBarSeries()
        self.series.append(set_sun)

        self.chart = QtCharts.QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Karma Points")
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        axisX = QtCharts.QBarCategoryAxis()
        self.date_now = datetime.date.today()
        print(self.date_to_string(self.date_now - datetime.timedelta(days=6)))
        axisX.append([self.date_to_string(self.date_now - datetime.timedelta(days=6)),
                      self.date_to_string(self.date_now - datetime.timedelta(days=5)),
                      self.date_to_string(self.date_now - datetime.timedelta(days=4)),
                      self.date_to_string(self.date_now - datetime.timedelta(days=3)),
                      self.date_to_string(self.date_now - datetime.timedelta(days=2)),
                      self.date_to_string(self.date_now - datetime.timedelta(days=1)),
                      self.date_to_string(self.date_now)])

        self.chart.createDefaultAxes()
        self.chart.setAxisX(axisX, self.series)
        self.series.attachAxis(axisX)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chartView = QtCharts.QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.chartView)
        self.setLayout(self.main_layout)

    def date_to_string(self, date):
        return date.strftime("%d") + ' ' + date.strftime("%b")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = BarChart([0, 1, -1, -9, 2, 3, -2])
    w.show()
    sys.exit(app.exec_())

