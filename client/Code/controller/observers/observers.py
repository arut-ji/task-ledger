import abc

from PySide2.QtWidgets import QWidget


class ObserverWidget(QWidget):
    """
        Define an updating interface for objects that should be notified of
        changes in a subject.
    """
    def update_data(self, data):
        pass

