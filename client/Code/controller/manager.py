import requests
import client.Code.controller.task as task_definition


class TaskLedgerSystem:
    """
        Acts as the manager of the tasks instances of the respective user instance
        The TaskLedgerSystem is the the subject to be observed
    """

    def __init__(self, user_auth=None):
        self.user_auth = user_auth
        self._observers = set()
        self._subject_state = None
        self.loading = False

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

    def create_task(self, topic, description, start_at, end_at, status, location):
        data = {
            "topic": topic,
            "description": description,
            "start_at": start_at,
            "end_at": end_at,
            "status": status,
            "location": location,
            "user": self.user_auth.get_user_id()
        }

        t = task_definition.Task(None, None, topic, description, start_at, end_at, status, location, data["user"])

        res = requests.post(self.user_auth.all_tasks_url, data=data)
        if res.status_code == 201:
            t.update(res.json())
            self.set_subject_state("Created Task", t)
            return True
        return False

    def delete_task(self):
        pass

    def get_tasks(self, status=False):
        params = {"status": status}
        params = {
            "status": status
        }

        res = requests.get(self.user_auth.task_url, params=params)

        if res.status_code == 200:
            return res.json()
        return False

    def set_loading(self, loading_status):
        self.loading = loading_status

