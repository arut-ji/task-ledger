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

        self.setFixedSize(1000, 600)

        for i in range(1,8):
            set_sun.append(i)

        self.series = QtCharts.QBarSeries()
        self.series.append(set_sun)

        self.chart = QtCharts.QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Karma Points")
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        axisX = QtCharts.QBarCategoryAxis()
        axisX.append(["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"])
        # axisX.append("MON")
        # axisX.append("TUE")
        # axisX.append("WED")
        # axisX.append("THU")
        # axisX.append("FRI")
        # axisX.append("SAT")

        self.chart.createDefaultAxes()
        self.chart.setAxisX(axisX, self.series)
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

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

