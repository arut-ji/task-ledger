from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QSize, QDate, QTime
from PySide2.QtGui import QIcon, QStandardItem
import datetime

from client.Code.controller.models.models import TaskList, Task
import client.Code.ui_to_py.dialog_ui as dialog
from client.Code.controller.subjects.manager import TaskLedgerSystem
from client.Code.utility.parsers import DatetimeParser


class Schedule_ui(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Schedule_ui, self).__init__(parent)
        self.date_now = datetime.date.today()
        self.active_task_list = None
        self.selected_task = None
        self.system: TaskLedgerSystem = None

    def bind_system(self, system):
        self.system = system

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

        self.list_view.clicked.connect(self.itemClicked)
        self.update_label(self.date_now)

    def itemClicked(self, index):
        task: Task = self.model.itemFromIndex(index).data()
        self.selected_task = task
        checked = self.model.itemFromIndex(index).checkState()
        if not checked:
            self.dialog = dialog.Display_dialog()
            self.dialog.setupUi(self.dialog)
            self.dialog.show()

            self.start_date = QDate.fromString(task.start_at.strftime("%d/%m/%Y"), 'dd/MM/yyyy')
            self.end_date = QDate.fromString(task.end_at.strftime("%d/%m/%Y"), 'dd/MM/yyyy')
            self.start_time = QTime.fromString(task.start_at.strftime("%H:%M:%S"), 'hh:mm:ss')
            self.end_time = QTime.fromString(task.end_at.strftime("%H:%M:%S"), 'hh:mm:ss')
            self.topic = task.topic
            self.location = task.location
            self.desc = task.description

            self.dialog.title.setText(self.topic)
            self.dialog.location.setText(self.location)
            self.dialog.from_dateEdit.setDate(self.start_date)
            self.dialog.to_dateEdit.setDate(self.end_date)
            self.dialog.textEdit_desc.setText(self.desc)
            self.dialog.timeEdit.setTime(self.start_time)
            self.dialog.to_timeEdit.setTime(self.end_time)
            self.dialog.edit_btn.clicked.connect(self.edit_dialog)

        else:
            details = task.get_detail()
            details['status'] = True
            self.system.update_task(task.id, details)

    def update_task(self):

        task_id = self.selected_task.id
        topic = self.dialog.title.text()
        location = self.dialog.location.text()
        start_date = self.dialog.from_dateEdit.date()
        end_date = self.dialog.to_dateEdit.date()
        start_time = self.dialog.timeEdit.time()
        end_time = self.dialog.to_timeEdit.time()
        description = self.dialog.textEdit_desc.toPlainText()
        status = self.selected_task.status

        start_at = DatetimeParser.fromQDateAndQTime(start_date, start_time)
        end_at = DatetimeParser.fromQDateAndQTime(end_date, end_time)

        details = {
            "topic": topic,
            "description": description,
            "start_at": str(start_at),
            "end_at": str(end_at),
            "status": status,
            "location": location
        }

        # TODO: Error Dialog
        is_update_success = self.system.update_task(task_id, details)

    def edit_dialog(self):
        self.dialog = dialog.Edit_dialog()
        self.dialog.setupUi(self.dialog)
        self.dialog.title.setText(self.topic)
        self.dialog.location.setText(self.location)
        self.dialog.from_dateEdit.setDate(self.start_date)
        self.dialog.to_dateEdit.setDate(self.end_date)
        self.dialog.textEdit_desc.setText(self.desc)
        self.dialog.timeEdit.setTime(self.start_time)
        self.dialog.to_timeEdit.setTime(self.end_time)
        self.dialog.save_btn.clicked.connect(self.update_task)
        self.dialog.save_btn.clicked.connect(self.dialog.close)
        self.dialog.show()

    def next_date(self):
        self.date_now += datetime.timedelta(days=1)
        self.update_label(self.date_now)
        self.update_task_list_view()

    def prev_date(self):
        self.date_now -= datetime.timedelta(days=1)
        self.update_label(self.date_now)
        self.update_task_list_view()

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

    def update_task_list_view(self):
        self.model.clear()
        current_date_tasks = list(
            filter(
                lambda task: task.start_at.date() <= self.date_now and task.end_at.date() >= self.date_now,
                self.active_task_list
            )
        )

        for task in current_date_tasks:
            topic = task.topic
            item = QStandardItem(topic)
            item.setData(task)
            item.setCheckable(True)
            item.setData(task)
            item.setEditable(False)
            self.model.appendRow(item)

        # TODO: No Task display
        if len(current_date_tasks) == 0:
            # item = QStandardItem("No task for this day.")
            pass

    # Subscribe to Observable
    def update_data(self, task_list: TaskList):
        task_list = task_list.get_task_list()
        self.active_task_list = list(
            filter(
                lambda task: not task.status,
                task_list
            )
        )

        self.update_task_list_view()
        super(Schedule_ui, self).update()
