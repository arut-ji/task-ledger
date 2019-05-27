import abc


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
    def update(self):
        pass

    @abc.abstractmethod
    def update_list(self, arg):
        pass

    @abc.abstractmethod
    def update_display(self, arg):
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

    def update(self):
        pass

    def update_list(self, arg):
        pass

    def update_display(self, arg):
        pass


class CompletedTasksList(TaskListObserver):
    """
    Observer for Completed Task List
    """
    def __init__(self):
        super().__init__()

    def update(self):
        pass

    def update_list(self, arg):
        pass

    def update_display(self, arg):
        pass
