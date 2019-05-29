from typing import Dict, List


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

        self.start_date_object = None
        self.end_date_object = None
        self.start_time_object = None
        self.end_time_object = None

    def set_date_time_object(self, sdate, edate, stime, etime):
        self.start_date_object = sdate
        self.end_date_object = edate
        self.start_time_object = stime
        self.end_time_object = etime

    def check_format(self):
        if self.start_date_object <= self.end_date_object:
            if self.start_date_object < self.end_date_object:
                return True
            elif self.start_time_object <= self.end_time_object:
                return True
        return False

    def update(self, data):
        """
            Is used when refreshing data from the database
        """
        self.__dict__ = data

    def get_detail(self):
        return self.__dict__

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.id == other.id


class TaskList:

    def __init__(self, tasks: List[Dict] = None):
        if tasks is None:
            self.tasks: List[Task] = []
        else:
            self.tasks: List[Task] = [Task(data=task) for task in tasks]

    def add_task(self, new_task_payload: Dict):
        new_task = Task(new_task_payload)
        self.tasks += [new_task]

    def update_task(self, task_id: int, payload: Dict) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                task.__dict__ = payload
                task.id = task_id
                return task

    def get_task(self, task_id: int):
        for task in self.tasks:
            if task_id == task.id:
                return task
        return None

    def delete_task(self, task_id: int) -> Task:
        for task in self.tasks:
            if task_id == task.id:
                result = task
                self.tasks.remove(task)
                return result

    def count(self):
        return len(self.tasks)
