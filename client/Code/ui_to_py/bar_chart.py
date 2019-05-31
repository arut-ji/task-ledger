import sys

from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QWidget, QApplication, QVBoxLayout
from PySide2 import QtCore


class BarChart(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        set_sun = QtCharts.QBarSet("ME")

        self.setFixedSize(651, 431)

        set_sun.append(1)
        set_sun.append(-2)
        set_sun.append(-3)
        set_sun.append(4)
        set_sun.append(5)
        set_sun.append(6)
        set_sun.append(7)
        set_sun.append(-2)

        self.series = QtCharts.QBarSeries()
        self.series.append(set_sun)

        self.chart = QtCharts.QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Karma Points")
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        axisX = QtCharts.QBarCategoryAxis()
        axisX.append(["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"])

        self.chart.createDefaultAxes()
        self.chart.setAxisX(axisX, self.series)
        self.chart.legend().setVisible(True)
        # self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chartView = QtCharts.QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.chartView)
        self.setLayout(self.main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = BarChart()
    w.show()
    sys.exit(app.exec_())

