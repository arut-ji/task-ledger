from PySide2.QtCore import QTime, QDate
from dateutil import parser
from datetime import datetime, date, timedelta
import time

# from client.Code.controller.models.models import TaskList, Task


class DatetimeParser:
    @staticmethod
    def parse(datetime_string: str):
        return parser.parse(datetime_string)

    @staticmethod
    def dateToDatetime(native_date: date):
        return datetime.combine(native_date, datetime.min.time())

    @staticmethod
    def fromQDateAndQTime(qdate: QDate, qtime: QTime):
        native_date = qdate.toPython()
        native_time = qtime.toPython()
        return datetime.combine(native_date, native_time)

    @staticmethod
    def fromQDateToDate(qdate: QDate) -> date:
        return qdate.toPython()

    @staticmethod
    def fromQTimeToTime(qtime: QTime) -> time:
        return qtime.toPython()

    # def fromQDateToDatetime(self, qdate: QDate) -> :

class TaskAnalyser:
    # pass
    @staticmethod
    def getPointFromTasks(task_list, max_date: datetime, backward_offset: int):

        min_date = (max_date - timedelta(days=backward_offset - 1)).date()
        max_date = max_date.date()
        date_counter = min_date
        point_list = []
        while date_counter <= max_date:
            point = sum(
                [
                    task.get_point() for task in task_list.get_task_from_date(date_counter)
                ]
            )
            point_list += [point]
            date_counter += timedelta(days=1)
        return point_list

    @staticmethod
    def countDoneTaskFromInteval(task_list, max_date: datetime, backward_offset: int):
        print(max_date)
        print(type(max_date))
        min_date = (max_date - timedelta(days=backward_offset - 1)).date()
        max_date = max_date.date()
        date_counter = min_date
        task_count_list = []
        while date_counter <= max_date:
            task_counter = len(
                [
                    task for task in task_list.get_task_list()
                    if task.done_at is not None and task.done_at.date() == date_counter
                ]
            )
            task_count_list += [task_counter]
            date_counter += timedelta(days=1)
        return task_count_list



mock_task_data = {
    "id": 20,
    "topic": "Project Deadline",
    "description": "Send SEP project.",
    "created_at": "2019-05-29T09:18:23.223777Z",
    "start_at": "2019-06-02T06:00:00Z",
    "end_at": "2019-06-02T09:00:00Z",
    "status": True,
    "location": "International College, KMITL",
    "user": 1
}

# task = Task(mock_task_data)
# tasks = TaskList()
# tasks.add_task(task)
# task.id = 21
# tasks.add_task(task)
# for item in tasks.get_task_list():
#     print(item)