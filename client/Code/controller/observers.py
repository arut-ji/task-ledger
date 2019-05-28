import abc
import client.Code.controller.task as task


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
    def init_list(self, arg):
        pass

    @abc.abstractmethod
    def update_display(self, arg):
        pass

    @abc.abstractmethod
    def get_list(self, arg):
        pass

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
            self.init_list(arg)

    def init_list(self, arg):
        """
            Initialize the active list
        """

        for item in arg:
            if item["status"]:
                t = task.Task(item["id"], item["user"], item["topic"], item["description"], item["created_at"],
                              item["start_at"], item["status"])
                self.add_task(t)

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
            self.init_list(arg)

    def init_list(self, arg):
        """
        Initialize the completed list
        """

        for item in arg:
            if item["status"] is False:
                t = task.Task(item["id"], item["user"], item["topic"], item["description"], item["created_at"],
                              item["start_at"], item["status"])
                self.add_task(t)

    def update_display(self, arg):
        pass

    def get_list(self, arg):
        pass
