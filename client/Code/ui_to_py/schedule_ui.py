from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QSize, QDate, QTime
from PySide2.QtGui import QIcon, QStandardItem
import datetime

from client.Code.controller.models.models import Task
import client.Code.ui_to_py.dialog_ui as dialog
from client.Code.controller.observers.observers import ObserverWidget
from client.Code.controller.subjects.subjects import TaskLedgerSystem
from client.Code.utility.parsers import DatetimeParser

error_stylesheet = "border-color: red; color: red;"
normal_stylesheet = "border-color: black; color: black;"

class Schedule_ui(ObserverWidget):

    def __init__(self, parent=None):
        super(Schedule_ui, self).__init__(parent)
        self.date_now = datetime.date.today()
        self.active_task_list = None
        self.selected_task = None
        self.system: TaskLedgerSystem = None
        self.busy = 0
        self.date = QtWidgets.QLabel(parent)
        self.today_label = QtWidgets.QLabel(parent)
        self.list_view = QtWidgets.QListView(parent)
        self.model = QtGui.QStandardItemModel(self.list_view)
        self.is_update_success = False

    def bind(self, system):
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


        self.today_label.setGeometry(QtCore.QRect(130, 20, 200, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(32)
        self.today_label.setFont(font)
        self.today_label.setObjectName("today_label")


        self.date.setGeometry(QtCore.QRect(120, 60, 500, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(42)
        self.date.setFont(font)
        self.date.setObjectName("label_3")

        self.list_view.setGeometry(80, 120, 590, 450)
        self.list_view.setModel(self.model)
        self.model.clear()

        self.list_view.clicked.connect(self.itemClicked)
        self.update_label(self.date_now)

        self.graphic = QtWidgets.QLabel(parent)
        self.graphic.setObjectName("label_4")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_notask = QtWidgets.QLabel(parent)
        self.label_notask.setFont(font)

    def itemClicked(self, index):
        task: Task = self.model.itemFromIndex(index).data()
        self.selected_task = task
        checked = self.model.itemFromIndex(index).checkState()
        if not checked:
            self.dialog = dialog.Display_dialog()
            self.dialog.setupUi(self.dialog, task.topic)
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

        if topic == '':
            self.dialog.title.setStyleSheet(error_stylesheet)
        else:
            self.dialog.title.setStyleSheet(normal_stylesheet)
            self.is_update_success = self.system.update_task(task_id, details)

        if not self.is_update_success:
            if start_at.date() >= end_at.date():
                self.dialog.to_dateEdit.setStyleSheet(error_stylesheet)
                self.dialog.from_dateEdit.setStyleSheet(error_stylesheet)

            else:
                self.dialog.to_dateEdit.setStyleSheet(normal_stylesheet)
                self.dialog.from_dateEdit.setStyleSheet(normal_stylesheet)

            if start_time >= end_time:
                self.dialog.timeEdit.setStyleSheet(error_stylesheet)
                self.dialog.to_timeEdit.setStyleSheet(error_stylesheet)
            else:
                self.dialog.timeEdit.setStyleSheet(normal_stylesheet)
                self.dialog.to_timeEdit.setStyleSheet(normal_stylesheet)

        else:
            self.dialog.close()

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
        # self.dialog.save_btn.clicked.connect(self.dialog.close)
        self.dialog.show()

    def next_date(self):
        self.date_now += datetime.timedelta(days=1)
        self.update_label(self.date_now)
        self.update_task_list_view()

    def prev_date(self):
        self.date_now -= datetime.timedelta(days=1)
        self.update_label(self.date_now)
        self.update_task_list_view()

    def update_label(self, date_input):
        self.date.setText(self.get_str_date(self.date_now))
        self.today_label.setText(date_input.strftime("%A"))

    def get_date(self):
        return self.date_now

    def set_date(self, date):
        self.date_now = date
        self.update_label(self.date_now)
        self.update_task_list_view()

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

        self.busy = len(current_date_tasks)

        for task in current_date_tasks:
            topic = task.topic
            item = QStandardItem(topic)
            item.setData(task)
            item.setCheckable(True)
            item.setData(task)
            item.setEditable(False)
            self.model.appendRow(item)

        if len(current_date_tasks) == 0:
            self.graphic.setText("")
            self.graphic.setPixmap(QtGui.QPixmap("../Assets/no_task.png"))
            self.graphic.setScaledContents(True)
            self.graphic.setGeometry(QtCore.QRect(260, 195, 252, 211))
            self.label_notask.setGeometry(QtCore.QRect(280, 395, 221, 51))
            self.label_notask.setText("You are free on this day !")

        else:
            self.graphic.clear()
            self.label_notask.clear()


    # Subscribe to Observable
    def update_data(self):
        task_list = self.system.get_task_list().get_task_list()
        self.active_task_list = list(
            filter(
                lambda task: not task.status,
                task_list
            )
        )

        self.update_task_list_view()
        super(Schedule_ui, self).update()
