from abc import ABCMeta, abstractmethod
from typing import Dict, Set

from PySide2.QtCore import QDate

from client.Code.controller.models.models import TaskList
from client.Code.controller.models.models import Task
from client.Code.controller.observers.observers import Observer

from client.Code.controller.services.services import AuthService
from client.Code.controller.services.services import TaskService
from client.Code.utility.validators import TaskValidator


class Observable(metaclass=ABCMeta):
    def __init__(self):
        self._observers = set()

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
        self.loading = False

    def _notify_observers(self):
        for observer in self._observers:
            observer.update_data(self.task_list)

    def set_current_user(self, user: Dict):
        self.user = user

    def set_current_token(self, token: str):
        self.token = token

    def set_task_list(self, task_list: TaskList):
        self.task_list = task_list
        self._notify_observers()

    def login(self, username, password) -> bool:

        response = AuthService.login(username, password)

        if response:
            self.set_current_user(response['user'])
            self.set_current_token(response['key'])
            task_list = TaskService.list_task(self.user["id"])
            self.set_task_list(task_list)
            return True
        return False

    def is_authenticated(self) -> bool:
        return self.token is not None

    def register(self, username, password1, password2) -> Dict:
        response = AuthService.register(username, password1, password2)

        if len(response) == 0:
            return {}
        else:
            return response

    def create_task(self, details: Dict) -> bool:
        details.update({'user': self.user['id']})
        is_valid = self.task_validator.validate(details)
        if is_valid:
            new_task = self.task_service.create_task(details)
            self.task_list.add_task(new_task)
            self._notify_observers()
            return True
        return False

    def update_task(self, task_id: int, details: Dict):
        details.update({'user': self.user['id']})
        is_valid = self.task_validator.validate(details)

        if is_valid:
            updated_task = TaskService.update_task(task_id, details)
            self.task_list.update_task(task_id, updated_task)
            self._notify_observers()
            return True
        return False

    def delete_task(self, task_id):
        deleted_task = self.task_list.delete_task(task_id)

        is_delete_success = False

        if deleted_task is not None:
            is_delete_success = TaskService.delete_task(task_id)

        if is_delete_success:
            self._notify_observers()
            return True

        return False

    def set_loading(self, loading_status):
        self.loading = loading_status

    def is_busy(self, date: QDate) -> bool:
        return self.task_list.is_busy(date)

class ConcreteObserver(Observer):
    def update_data(self, task_list: TaskList):
        for task in task_list.get_task_list():
            print(task)

