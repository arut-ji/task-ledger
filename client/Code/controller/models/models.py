import datetime
from typing import Dict, List, Optional
import json

# from client.Code.utility.validators import TaskValidator
from PySide2.QtCore import QDate

from client.Code.utility.parsers import DatetimeParser, TaskAnalyser
from client.Code.utility.validators import TaskValidator


class Task:
    """
        When loading tasks from database no fields shall be None value
        When creating new tasks to be added, task_id and created_at have to be have value None
        sdate and edate are QDate Objects which is used to verify date before POST request to api endpoint
    """

    def __init__(self, data):
        self.__slots__ = [
            'id',
            'topic',
            'description',
            'created_at',
            'start_at',
            'end_at',
            'done_at'
            'status',
            'location',
            'user'
        ]
        self.id = self.topic = self.description = self.created_at = self.start_at = self.end_at = self.done_at = self.status = self.location = self.user = None
        self.__dict__ = data

        if isinstance(self.start_at, str):
            self.created_at = DatetimeParser.parse(self.created_at)
        if isinstance(self.end_at, str):
            self.end_at = DatetimeParser.parse(self.end_at)
        if isinstance(self.start_at, str):
            self.start_at = DatetimeParser.parse(self.start_at)

        if self.done_at is not None:
            if isinstance(self.done_at, str):
                self.done_at = DatetimeParser.parse(self.done_at)

    def update(self, data):
        self.__dict__ = data

    def json(self):
        return json.dumps(self.__dict__)

    def get_detail(self):
        return {
            "topic": self.topic,
            "description": self.description,
            "start_at": str(self.start_at),
            "end_at": str(self.end_at),
            "status": self.status,
            "location": self.location,
            "done_at": self.done_at
        }

    def get_point(self):
        if self.status:
            return 5 if self.done_at.date() < self.end_at.date() else -1 * (self.done_at.date() - self.end_at.date()).days
        else:
            return -1 * (
                        datetime.datetime.now().date() - self.end_at.date()).days if datetime.datetime.now().date() > self.end_at.date() else 0

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.id == other.id


class TaskList:

    def __init__(self, tasks: List[Dict] = None):
        self._validator = TaskValidator()
        if tasks is None:
            self.tasks: List[Task] = []
        else:
            self.tasks: List[Task] = [Task(data=task) for task in tasks]

    def add_task(self, new_task: Task):
        self.tasks += [new_task]

    def update_task(self, task_id: int, updated_task: Task) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                task.__dict__ = updated_task.__dict__
                task.id = task_id
                return task

    def get_task(self, task_id: int):
        for task in self.tasks:
            if task_id == task.id:
                return task
        return None

    def delete_task(self, task_id: int):
        for task in self.tasks:
            if task_id == task.id:
                result = task
                self.tasks.remove(task)
                return result
        return None

    def count(self) -> int:
        return len(self.tasks)

    def get_task_list(self) -> List[Task]:
        return self.tasks

    def is_busy(self, date: QDate):
        native_date = DatetimeParser.fromQDateToDate(date)
        return len(
            list(
                filter(
                    lambda
                        task: task.start_at.date() <= native_date and task.end_at.date() >= native_date and not task.status,
                    self.tasks
                )
            )
        ) > 0

    def json(self) -> str:
        return json.dumps([task.json() for task in self.tasks])

    def get_task_from_date(self, date: datetime.date):
        return list(
            filter(
                lambda
                    task: task.start_at.date() <= date and task.end_at.date() >= date,
                self.tasks
            )
        )


mock_task_data = {
    "id": 20,
    "topic": "Project Deadline",
    "description": "Send SEP project.",
    "created_at": "2019-05-29T09:18:23.223777Z",
    "start_at": "2019-05-02T06:00:00Z",
    "end_at": "2019-05-02T09:00:00Z",
    "status": True,
    "location": "International College, KMITL",
    "done_at": "2019-05-29T09:18:23.223777Z",
    "user": 1
}
mock_task_data_2 = {
    "id": 20,
    "topic": "Project Deadline",
    "description": "Send SEP project.",
    "created_at": "2019-05-29T09:18:23.223777Z",
    "start_at": "2019-05-02T06:00:00Z",
    "end_at": "2019-05-02T09:00:00Z",
    "status": True,
    "location": "International College, KMITL",
    "done_at": "2019-05-30T09:18:23.223777Z",
    "user": 1
}
#
# task = Task(mock_task_data)
#
# print(task.get_point())
# tasks = TaskList()
# tasks.add_task(task)
# tasks.add_task(Task(mock_task_data_2))
# print(TaskAnalyser.countDoneTaskFromInteval(tasks, datetime.datetime.now(), 7))
# print(task)
#
# # print(task.start_at.date())
# # print(task.end_at.date())
# print(tasks.is_busy(QDate(2019, 6, 2)))
