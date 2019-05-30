import abc


class Observer(metaclass=abc.ABCMeta):
    """
        Define an updating interface for objects that should be notified of
        changes in a subject.
    """
    @abc.abstractmethod
    def update_data(self, data):
        pass

