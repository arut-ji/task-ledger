from abc import ABCMeta, abstractmethod
from typing import Dict

from client.Code.controller.models.models import TaskList
from client.Code.controller.models.models import Task
from client.Code.controller.observers.observers import Observer

from client.Code.controller.services.services import AuthService
from client.Code.controller.services.services import TaskService
from client.Code.utility.validators import TaskValidator


class Observable(metaclass=ABCMeta):
    def __init__(self):
        self._observers = set()
        self._subject_state = None

    def attach(self, observer):
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.discard(observer)

    @abstractmethod
    def _notify_observers(self):
        pass


class TaskLedgerSystem(Observable):

    def __init__(self):
        super().__init__()
        self.task_list = TaskList()
        self.auth_service = AuthService()
        self.task_service = TaskService()
        self.task_validator = TaskValidator()
        self.user = None
        self.token = None

    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self.task_list)

    def set_current_user(self, user):
        self.user = user

    def set_current_token(self, token):
        self.token = token

    def set_task_list(self, task_list: TaskList):
        self.task_list = task_list
        self._notify_observers()

    def login(self, username, password):

        response = AuthService.login(username, password)

        if response:
            self.set_current_user(response['user'])
            self.set_current_token(response['key'])
            task_list = TaskService.list_task(self.user["id"])
            self.set_task_list(task_list)
            return True
        return False

    def create_task(self, details: Dict):

        details.update({'user': self.user['id']})
        is_valid = self.task_validator.validate(details)
        print(is_valid)
        if is_valid:
            new_task = self.task_service.create_task(details)
            self.task_list.add_task(new_task)
            self._notify_observers()

    # TODO: implement update_task
    def update_task(self, task_id, details):
        pass

    # TODO: implement delete_task
    def delete_task(self, task_id):
        pass

    def set_loading(self, loading_status):
        self.loading = loading_status

#
#     def update_task(self, task_id, task_data):
#         res = self.task_service.update_task(task_id, task_data)
#         if res:
#             self.task_list.update_task(task_id, task_data)
#             self.set_subject_state("Updated Task", self.task_list)
#             return True
#

# system = TaskLedgerSystem()
# system.attach(ConcreteObserver())
#
# system.login('admin', 'admin')
# system.create_task({
#     "topic": "Project Deadline",
#     "description": "Send SEP project.",
#     "created_at": "2019-05-29T09:18:23.223777Z",
#     "start_at": "2019-06-02T06:00:00Z",
#     "end_at": "2019-06-02T09:00:00Z",
#     "status": False,
#     "location": "International College, KMITL",
# })