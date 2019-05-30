from PySide2 import QtWidgets, QtCore, QtGui


class NavBarUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(NavBarUI, self).__init__(parent)
        
    def setupUI(self, parent=None):
        self.label = QtWidgets.QLabel(parent)
        self.label.setGeometry(QtCore.QRect(0, 0, 274, 600))
        self.label.setStyleSheet("QWidget{ background-color: rgb(242, 247, 247);}")
        self.label.setText("")
        self.label.setObjectName("label")

        # menu button
        self.schedule = QtWidgets.QPushButton(parent)
        self.schedule.setGeometry(QtCore.QRect(30, 190, 89, 32))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.schedule.setFont(font)
        self.schedule.setObjectName("schedule")
        self.schedule.setText("Schedule")


        self.calendar = QtWidgets.QPushButton(parent)
        self.calendar.setGeometry(QtCore.QRect(30, 240, 85, 32))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.calendar.setFont(font)
        self.calendar.setObjectName("calendar")
        self.calendar.setText("Calendar")


        self.history = QtWidgets.QPushButton(parent)
        self.history.setGeometry(QtCore.QRect(30, 290, 69, 32))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.history.setFont(font)
        self.history.setText("History")
        self.history.setObjectName("history")

        self.statistic = QtWidgets.QPushButton(parent)
        self.statistic.setGeometry(QtCore.QRect(30, 340, 88, 32))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.statistic.setFont(font)
        self.statistic.setText("Statistics")
        self.statistic.setObjectName("statistic")

        self.notification = QtWidgets.QPushButton(parent)
        self.notification.setGeometry(QtCore.QRect(30, 390, 110, 32))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.notification.setFont(font)
        self.notification.setText("Notification")
        self.notification.setObjectName("notification")

        # logo label
        self.logo = QtWidgets.QLabel(parent)
        self.logo.setGeometry(QtCore.QRect(50, 30, 167, 38))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../Assets/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        # create button
        self.create_button = QtWidgets.QPushButton(parent)
        self.create_button.setGeometry(QtCore.QRect(30, 100, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.create_button.setFont(font)
        self.create_button.setObjectName("create_button")
        self.create_button.setText("+ Create")

        # logout Button
        self.log_out = QtWidgets.QPushButton(parent)
        self.log_out.setGeometry(QtCore.QRect(15, 545, 51, 51))
        self.log_out.setText("")
        self.log_out.setIcon(QtGui.QIcon("../Assets/logout.png"))
        self.log_out.setIconSize(QtCore.QSize(31, 31))
        self.log_out.setObjectName("logout")


