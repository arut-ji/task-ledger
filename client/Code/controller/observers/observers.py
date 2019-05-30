import abc


class TaskListObserver(metaclass=abc.ABCMeta):
    """
        Define an updating interface for objects that should be notified of
        changes in a subject.
    """

    def __init__(self):
        self._subject = None
        self._observer_state = None
        self.ui = None

    def set_ui(self, ui):
        self.ui = ui

    @abc.abstractmethod
    def update(self, arg):
        pass

    @abc.abstractmethod
    def state_initialize(self, arg):
        pass

    @abc.abstractmethod
    def state_updated_task(self, arg):
        pass


class IncompleteTasks(TaskListObserver):
    """
        Observer for Active Task List
    """

    def __init__(self):
        super().__init__()

    def update(self, arg):
        state = self._subject.get_subject_state()

        if state == "Initialize":
            pass
        if state == "Created Task":
            pass
        if state == "Updated Task":
            pass

    def state_initialize(self, arg):
        pass

    def state_created_task(self, arg):
        pass

    def state_updated_task(self, arg):
        pass


class CompletedTasks(TaskListObserver):
    """
    Observer for Completed Task List
    """
    def __init__(self):
        super().__init__()

    def update(self, arg):
        state = self._subject.get_subject_state()

        if state == "Initialize":
            pass
        if state == "Updated Task":
            pass

    def state_initialize(self, arg):
        pass

    def state_updated_task(self, arg):
        pass
