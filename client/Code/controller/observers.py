import abc
import client.Code.controller.task as task_definition


class TaskListObserver(metaclass=abc.ABCMeta):
    """
        Define an updating interface for objects that should be notified of
        changes in a subject.
    """

    def __init__(self):
        self._subject = None
        self._observer_state = None
        self.task_list = []

    @abc.abstractmethod
    def update(self, arg):
        pass

    @abc.abstractmethod
    def update_display(self, arg):
        pass

    @abc.abstractmethod
    def get_list(self, arg):
        pass

    def init_list(self, status):
        """
            Initialize the active list
        """

        tasks = self._subject.get_tasks(status)

        for item in tasks:
            t = task_definition.Task(item["id"], item["topic"], item["description"], item["created_at"],
                                     item["start_at"], item["end_at"], item["status"], item["location"], item["user"])
            self.add_task(t)

    def add_task(self, arg):
        self.task_list.append(arg)

    def delete_task(self, arg):
        self.task_list.remove(arg)


class ActiveTasksList(TaskListObserver):
    """
        Observer for Active Task List
    """

    def __init__(self):
        super().__init__()

    def update(self, arg):
        state = self._subject.get_subject_state()

        if state == "Initialize":
            self.init_list(False)
        if state == "Created Task":
            self.created_new_task(arg)

    def created_new_task(self, arg):
        self.task_list.append(arg)

    def update_display(self, arg):
        pass

    def get_list(self, arg):
        pass

    def mark_complete(self, arg):
        """
            Mark the task as completed once time has passed
            Remove it from ActiveTaskList
        """
        pass


class CompletedTasksList(TaskListObserver):
    """
    Observer for Completed Task List
    """
    def __init__(self):
        super().__init__()

    def update(self, arg):
        state = self._subject.get_subject_state()

        if state == "Initialize":
            self.init_list(True)

    def update_display(self, arg):
        pass

    def get_list(self, arg):
        pass
