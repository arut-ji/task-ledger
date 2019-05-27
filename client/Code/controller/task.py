import abc


class Observer(metaclass=abc.ABCMeta):
    """
        Define an updating interface for objects that should be notified of
        changes in a subject.
    """

    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def update_list(self, arg):
        pass


class TaskListObserver(Observer):
    """
        Class for tasks list
            - Upcoming / Active Tasks List
            - Completed Tasks
    """

    def __init__(self):
        super().__init__()

    def update_list(self, arg):
        pass

    def update_display(self):
        pass


class TaskLedgerSystem:
    """
        Acts as the manager of the tasks instances of the respective user instance
        The TaskLedgerSystem is the the subject to be observed
        The observers:
            - Task Lists
            - Karma Points
    """

    def __init__(self, user_auth):
        self.user_auth = user_auth
        self._observers = set()
        self._subject_state = None

    def attach(self, observer):
        """
            Attach an observer to the subject
        """

        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        """
            Remove an observer from the Subject
        """

        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        """
        Notify all the Observers of the change in Subject state
        """

        for observer in self._observers:
            observer.update(self._subject_state)

    def get_subject_state(self):
        """
            Return Subject's current state
        """

        return self._subject_state

    def set_subject_state(self, state):
        """
            Set the Subject's current state
        """

        self._subject_state = state
        self._notify()

    def create_task(self):
        pass

    def delete_task(self):
        pass

