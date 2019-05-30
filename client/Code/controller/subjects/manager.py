from client.Code.controller.models.models import TaskList
from client.Code.controller.models.models import Task

from client.Code.controller.services.services import AuthService
from client.Code.controller.services.services import TaskService


class TaskLedgerSystem:
    """
        Acts as the manager of the tasks instances of the respective user instance
        The TaskLedgerSystem is the the subject to be observed
    """

    def __init__(self):
        self.auth_service = AuthService()
        self.task_service = TaskService()

        self.task_list = TaskList()

        self._observers = set()
        self._subject_state = None
        self.loading = False

        self.user = None

    def attach(self, observer):
        """
            Attach an observer to the subject
        """

        observer._subject = self
        self._observers.add(observer)
        if self.task_list is not None:
            self._notify(self.task_list)

    def detach(self, observer):
        """
            Remove an observer from the Subject
        """

        observer._subject = None
        self._observers.discard(observer)

    def _notify(self, arg=None):
        """
        Notify all the Observers of the change in Subject state
        """

        for observer in self._observers:
            observer.update(arg)

    def get_subject_state(self):
        """
            Return Subject's current state
        """

        return self._subject_state

    def set_subject_state(self, state, arg=None):
        """
            Set the Subject's current state
        """

        self._subject_state = state
        self._notify(arg)

    def login(self, username, password):
        """
            Login - Authenticate using the AuthService class
            Returns True if success
            Returns False if error occurs

            Make request to load tasks then notify observers if success
        """

        res = self.auth_service.login(username, password)

        if res:
            self.user = res["user"]
            self.task_list = self.task_service.list_task(self.user["id"])
            self.set_subject_state("Initialize", self.task_list)
            return True
        return False

    def register(self, username, pw1, pw2):
        """
            Register - Authenticate using the AuthService class
            Returns True if success
            Returns False if error occurs

            Make request to load tasks then notify observers if success
        """

        res = self.auth_service.register(username, pw1, pw2)

        if res:
            self.user = res["user"]
            self.task_list = self.task_service.list_task(self.user["id"])
            self.set_subject_state("Initialize")
            return True
        return False

    def create_task(self, task_data, time_object=None):
        """
            Create Task - Create Task Object and make POST request
            Return True if success
            Return False if error occurs

            Make request creates new task, loads it into task list then notify observers of the change
        """

        task = Task(task_data)
        task.set_date_time_object(time_object)

        if task.check_format():
            if self.task_service.create_task(task_data):
                self.task_list.add_task(task_data)
                self.set_subject_state("Created Task", self.task_list)
                return True
        return False

    def update_task(self, task_id, task_data):
        res = self.task_service.update_task(task_id, task_data)
        if res:
            self.task_list.update_task(task_id, task_data)
            self.set_subject_state("Updated Task", self.task_list)
            return True

    def set_loading(self, loading_status):
        self.loading = loading_status
