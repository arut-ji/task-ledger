class TaskLedgerSystem:
    """
        Acts as the manager of the tasks instances of the respective user instance
        The TaskLedgerSystem is the the subject to be observed
    """

    def __init__(self, user_auth=None):
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

    def create_task(self):
        pass

    def delete_task(self):
        pass

