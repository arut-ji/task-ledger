from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
import datetime


# mockTaskList = [
#     {
#         "id": 19,
#         "topic": "TestEvent",
#         "description": "TestDescription",
#         "created_at": "2019-05-28T21:20:27.905367Z",
#         "start_at": "2019-06-03T03:00:00Z",
#         "end_at": "2019-06-03T05:00:00Z",
#         "status": False,
#         "location": "TestLocation",
#         "user": 1
#     },
#     {
#         "id": 20,
#         "topic": "Project Deadline",
#         "description": "Send SEP project.",
#         "created_at": "2019-05-29T09:18:23.223777Z",
#         "start_at": "2019-06-02T06:00:00Z",
#         "end_at": "2019-06-02T09:00:00Z",
#         "status": False,
#         "location": "International College, KMITL",
#         "user": 1
#     }
# ]

class Observer:
    def update(self, payload):
        pass


class Schedule_ui(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Schedule_ui, self).__init__(parent)
        # self.tasks = mockTaskList
        self.date_now = datetime.date.today()

        self._subject = None
        self._observer_state = None


    def setupUi(self, parent=None):
        # Button
        self.left_arrow = QtWidgets.QPushButton(parent)
        self.left_arrow.setGeometry(QtCore.QRect(30, 55, 41, 41))
        self.left_arrow.setText("")
        self.left_arrow.setIcon(QIcon("../Assets/arrow_left.png"))
        self.left_arrow.setFlat(True)
        self.left_arrow.setIconSize(QSize(21, 21))
        self.left_arrow.setObjectName("left_arrow")
        self.left_arrow.clicked.connect(self.prev_date)

        self.right_arrow = QtWidgets.QPushButton(parent)
        self.right_arrow.setGeometry(QtCore.QRect(80, 55, 41, 41))
        self.right_arrow.setText("")
        self.right_arrow.setIcon(QIcon("../Assets/arrow_right.png"))
        self.right_arrow.setFlat(True)
        self.right_arrow.setIconSize(QSize(21, 21))
        self.right_arrow.setObjectName("right_arrow")
        self.right_arrow.clicked.connect(self.next_date)

        self.today_label = QtWidgets.QLabel(parent)
        self.today_label.setGeometry(QtCore.QRect(130, 20, 200, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(32)
        self.today_label.setFont(font)
        self.today_label.setObjectName("today_label")

        self.date = QtWidgets.QLabel(parent)
        self.date.setGeometry(QtCore.QRect(120, 60, 500, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(42)
        self.date.setFont(font)
        self.date.setObjectName("label_3")

        self.list_view = QtWidgets.QListView(parent)
        self.list_view.setGeometry(80, 120, 590, 450)

        self.model = QtGui.QStandardItemModel(self.list_view)
        self.list_view.setModel(self.model)
        self.model.clear()

        self.update_label(self.date_now)

        # self.checkBox_3 = QtWidgets.QCheckBox(parent)
        # self.checkBox_3.setGeometry(QtCore.QRect(100, 170, 271, 41))
        # self.checkBox_3.setObjectName("checkBox_3")
        # self.checkBox_3.setText('hi')
        #
        # self.checkBox_4 = QtWidgets.QCheckBox(parent)
        # self.checkBox_4.setGeometry(QtCore.QRect(100, 120, 271, 41))
        # self.checkBox_4.setObjectName("checkBox_4")
        # self.checkBox_4.setText('hi')

    def next_date(self):
        self.date_now += datetime.timedelta(days=1)
        self.update_label(self.date_now)

    def prev_date(self):
        self.date_now -= datetime.timedelta(days=1)
        self.update_label(self.date_now)

    def update_label(self, date):
        self.date.setText(self.get_str_date(self.date_now))
        self.today_label.setText(date.strftime("%A"))

    def get_date(self):
        return self.date_now

    def set_date(self, date):
        self.date_now = date

    def get_str_date(self, date):
        return ' ' + date.strftime("%d") + ' ' \
               + date.strftime("%B") + ' ' + date.strftime("%Y")

    def update(self, arg):
        self.state_initialize(arg)
        super(Schedule_ui, self).update()

    def state_initialize(self, arg):
        self.model.clear()
        for task in arg.tasks:
            if task.get_detail()["status"] is False:
                task_list_item = QtGui.QStandardItem(task.get_detail()['topic'])
                task_list_item.setCheckable(True)
                self.model.appendRow(task_list_item)
