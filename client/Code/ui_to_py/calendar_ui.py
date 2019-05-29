from PySide2 import QtCore, QtGui, QtWidgets

#TODO:: today selection-hover

class CalendarWidget(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        super(CalendarWidget, self).__init__(parent,
            verticalHeaderFormat=QtWidgets.QCalendarWidget.NoVerticalHeader,
            gridVisible=False)

        self.cur_day = QtGui.QTextCharFormat()
        self.brush = QtGui.QBrush()
        # self.brush.setColor(self, QtGui.QColor(212, 175, 55))
        # self.cur_day.setBackground(QtGui.QBrush.setColor())
        self.today = QtCore.QDate.currentDate()
        # print(self.today)
        self.setDateTextFormat(self.today, self.cur_day)

        for d in (QtCore.Qt.Saturday, QtCore.Qt.Sunday,):
            fmt = self.weekdayTextFormat(d)
            fmt.setForeground(QtCore.Qt.black)
            self.setWeekdayTextFormat(d, fmt)
        self.show()

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
        # if date == self.today.day():
        #     painter.setBrush(QtGui.QColor("black"))
        #     h = QtCore.QRect(QtCore.QPoint(), min(rect.width()/4, rect.height()/4)*QtCore.QSize(1, 1))
        #     h.moveRight(rect.right())
        #     # painter.drawEllipse(h, )
        # # painter.setPen(QtGui.QPen(QtGui.QColor("black")))
        # # print(str(self.today), str(date.day()))
        # painter.drawText(rect )
        #     # painter.restore()

        if date == self.selectedDate():
            painter.save()
            painter.fillRect(rect, QtGui.QColor("white"))
            painter.setPen(QtCore.Qt.NoPen)
            color = (date.day() % 5)

            #selection
            painter.setBrush(QtGui.QColor(self.get_color(color)))
            r = QtCore.QRect(QtCore.QPoint(), min(rect.width(), rect.height())*QtCore.QSize(1, 1))
            r.moveCenter(rect.center())
            painter.drawEllipse(r)
            painter.setPen(QtGui.QPen(QtGui.QColor("black")))
            painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))
            painter.restore()
        else:
            super(CalendarWidget, self).paintCell(painter, rect, date)
