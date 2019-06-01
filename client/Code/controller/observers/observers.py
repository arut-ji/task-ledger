import abc

from PySide2.QtWidgets import QWidget

from client.Code.controller.subjects.subjects import Observable


class ObserverWidget(QWidget):
    """
        Define an updating interface for objects that should be notified of
        changes in a subject.
    """
    def update_data(self):
        pass

    def bind(self, subject: Observable):
        pass

