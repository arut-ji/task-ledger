from typing import Dict, List, Optional
import json

# from client.Code.utility.validators import TaskValidator
from client.Code.utility.parsers import DatetimeParser
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
            'status',
            'location',
            'user'
        ]

        self.__dict__ = data

        self.created_at = DatetimeParser.parse(self.created_at)
        self.end_at = DatetimeParser.parse(self.end_at)
        self.start_at = DatetimeParser.parse(self.start_at)

    def update(self, data):
        self.__dict__ = data

    def json(self):
        return json.dumps(self.__dict__)

    def get_detail(self):
        return self.__dict__

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

    def json(self) -> str:
        return json.dumps([task.json() for task in self.tasks])

# # mock_task_data = {
# #     "id": 20,
# #     "topic": "Project Deadline",
# #     "description": "Send SEP project.",
# #     "created_at": "2019-05-29T09:18:23.223777Z",
# #     "start_at": "2019-06-02T06:00:00Z",
# #     "end_at": "2019-06-02T09:00:00Z",
# #     "status": False,
# #     "location": "International College, KMITL",
# #     "user": 1
# # }
# #
# # task = Task(mock_task_data)
# print(task)
