from PySide2 import QtCore, QtGui, QtWidgets

from client.Code.controller.subjects.subjects import TaskLedgerSystem

class CalendarWidget(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        super(CalendarWidget, self).__init__(parent,
            verticalHeaderFormat=QtWidgets.QCalendarWidget.NoVerticalHeader,
            gridVisible=False)

        self.cur_day = QtGui.QTextCharFormat()
        self.brush = QtGui.QBrush()
        self.today = QtCore.QDate.currentDate()
        self.setFont("Roboto Light")
        self.system: TaskLedgerSystem = None
        for d in (QtCore.Qt.Saturday, QtCore.Qt.Sunday,):
            fmt = self.weekdayTextFormat(d)
            fmt.setForeground(QtCore.Qt.black)
            self.setWeekdayTextFormat(d, fmt)
        self.show()

    def bind(self, system):
        self.system = system

    def get_selected_date(self):
        return self.selectedDate().toPython()

    def get_color(self, color):
        switcher = {
            0: "#1E73D9",
            1: "#E09042",
            2: "#499255",
            3: "#F2B736",
            4: "#C5523F"
        }
        return switcher.get(color)

    def paintCell(self, painter, rect, date):
        is_busy = self.system.is_busy(date)
        if is_busy:
            painter.save()
            painter.fillRect(rect, QtGui.QColor("white"))
            painter.setPen(QtCore.Qt.NoPen)
            color = (date.day() % 5)

            # selection
            painter.setBrush(QtGui.QColor(self.get_color(color)))
            r = QtCore.QRect(QtCore.QPoint(), min(rect.width() - 5, rect.height() - 5)*QtCore.QSize(1, 1))
            r.moveCenter(rect.center())
            painter.drawEllipse(r)
            painter.setFont("Roboto Light")
            painter.setPen(QtGui.QPen(QtGui.QColor("white")))
            painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))
            painter.restore()
        else:
            super(CalendarWidget, self).paintCell(painter, rect, date)
