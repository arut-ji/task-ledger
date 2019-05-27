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


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(970, 600)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        Form.setFont(font)
        css_file = open('../Stylesheet/main_stylesheet.css').read()
        Form.setStyleSheet(css_file)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 274, 600))
        self.label.setStyleSheet("QWidget{\n"
"    background-color: rgb(242, 247, 247);\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(50, 30, 167, 38))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../Assets/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.create_button = QtWidgets.QPushButton(Form)
        self.create_button.setGeometry(QtCore.QRect(30, 100, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.create_button.setFont(font)
        self.create_button.setObjectName("create_button")
        self.schedule = QtWidgets.QLabel(Form)
        self.schedule.setGeometry(QtCore.QRect(30, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.schedule.setFont(font)
        self.schedule.setObjectName("schedule")
        self.calendar = QtWidgets.QLabel(Form)
        self.calendar.setGeometry(QtCore.QRect(30, 240, 89, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.calendar.setFont(font)
        self.calendar.setObjectName("calendar")
        self.history = QtWidgets.QLabel(Form)
        self.history.setGeometry(QtCore.QRect(30, 290, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.history.setFont(font)
        self.history.setObjectName("history")
        self.statistic = QtWidgets.QLabel(Form)
        self.statistic.setGeometry(QtCore.QRect(30, 340, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.statistic.setFont(font)
        self.statistic.setObjectName("statistic")
        self.notification = QtWidgets.QLabel(Form)
        self.notification.setGeometry(QtCore.QRect(30, 390, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.notification.setFont(font)
        self.notification.setObjectName("notification")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 550, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Assets/settings.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.calendarWidget = CalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(300, 80, 651, 391))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.create_button.setText(QtWidgets.QApplication.translate("Form", "+ Create", None, -1))
        self.schedule.setText(QtWidgets.QApplication.translate("Form", "Schedule", None, -1))
        self.calendar.setText(QtWidgets.QApplication.translate("Form", "Calendar", None, -1))
        self.history.setText(QtWidgets.QApplication.translate("Form", "History", None, -1))
        self.statistic.setText(QtWidgets.QApplication.translate("Form", "Statistic", None, -1))
        self.notification.setText(QtWidgets.QApplication.translate("Form", "Notifications", None, -1))


