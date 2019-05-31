import math
import sys
from random import randrange

from PySide2.QtCore import QAbstractTableModel, QModelIndex, QRect, Qt
from PySide2.QtGui import QColor, QPainter, QFont, QPen
from PySide2.QtWidgets import (QApplication, QHeaderView,
                               QTableView, QWidget, QVBoxLayout, QLabel, QFrame)
from PySide2.QtCharts import QtCharts

class CustomTableModel(QAbstractTableModel):
    def __init__(self):
        QAbstractTableModel.__init__(self)
        self.input_data = []
        self.mapping = {}
        self.column_count = 2
        self.row_count = 7
        self.min_val = math.inf
        self.max_val = -math.inf

        for i in range(self.row_count):
            data_vec = [0]*self.column_count
            for k in range(len(data_vec)):
                if k == 0:
                    data_vec[k] = i + 1
                if k == 1:
                    data_vec[k] = randrange(100)
                    self.min_val = min(self.min_val, data_vec[k])
                    self.max_val = max(self.max_val, data_vec[k])
            self.input_data.append(data_vec)

    def rowCount(self, parent=QModelIndex()):
        return len(self.input_data)

    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            if section % 2 == 0:
                return "x"
            else:
                return "y"
        else:
            return "{}".format(section + 1)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.input_data[index.row()][index.column()]
        elif role == Qt.EditRole:
            return self.input_data[index.row()][index.column()]
        elif role == Qt.BackgroundRole:
            for color, rect in self.mapping.items():
                if rect.contains(index.column(), index.row()):
                    return QColor(color)
            # cell not mapped return white color
            return QColor(Qt.white);
        return None

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            self.input_data[index.row()][index.column()] = float(value)
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable

    def add_mapping(self, color, area):
        self.mapping[color] = area

    def clear_mapping(self):
        self.mapping = {}



class TableWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.model = CustomTableModel()

        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_view.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.chart = QtCharts.QChart()
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

        self.series = QtCharts.QLineSeries()
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(242, 183, 54))
        pen.setCapStyle(Qt.RoundCap)
        self.series.setPen(pen)
        self.series.setName("Weekly Karma Points")
        self.mapper = QtCharts.QVXYModelMapper(self)
        self.mapper.setXColumn(0)
        self.mapper.setYColumn(1)
        self.mapper.setSeries(self.series)
        self.mapper.setModel(self.model)
        self.chart.addSeries(self.series)

        # for storing color hex from the series
        seriesColorHex = "#000000"

        # get the color of the series and use it for showing the mapped area
        seriesColorHex = "{}".format(self.series.pen().color().name())
        self.model.add_mapping(seriesColorHex, QRect(0, 0, 2, self.model.rowCount()))

        # series 2
        # self.series = QtCharts.QLineSeries()
        # self.series.setName("Monthy")
        #
        # self.mapper = QtCharts.QVXYModelMapper(self)
        # self.mapper.setXColumn(2)
        # self.mapper.setYColumn(3)
        # self.mapper.setSeries(self.series)
        # self.mapper.setModel(self.model)
        # self.chart.addSeries(self.series)
        #
        # # get the color of the series and use it for showing the mapped area
        # seriesColorHex = "{}".format(self.series.pen().color().name())
        # self.model.add_mapping(seriesColorHex, QRect(2, 0, 2, self.model.rowCount()))

        axisX = QtCharts.QCategoryAxis()
        axisX.append("SUN", 1)
        axisX.append("MON", 2)
        axisX.append("TUE", 3)
        axisX.append("WED", 4)
        axisX.append("THU", 5)
        axisX.append("FRI", 6)
        axisX.append("SAT", 7)
        axisX.setRange(0, 7)

        axisY = QtCharts.QValueAxis()

        axisY.setRange(self.model.min_val, self.model.max_val)


        self.chart.addAxis(axisX, Qt.AlignBottom)
        self.chart.addAxis(axisY, Qt.AlignLeft)
        self.chart_view = QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setFixedSize(651, 431)

        # self.chart_view.setGeometry(20, 100, 671, 451)
        # create main layout
        self.main_layout = QVBoxLayout(self)
        # self.main_layout.addWidget(self.table_view, 1, 0)
        self.main_layout.addWidget(self.chart_view)
        # self.main_layout.setColumnStretch(1, 1)
        # self.main_layout.setColumnStretch(0, 0)
        self.setLayout(self.main_layout)


class StatisticsUI(QWidget):
    def __init__(self, parent=None):
        super(StatisticsUI, self).__init__(parent)

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

        self.stat_graph = TableWidget(self.stat_frame)
        self.stat_graph.setGeometry(0, 0, 671, 451)
        self.stat_graph.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TableWidget()
    w.show()
    sys.exit(app.exec_())
