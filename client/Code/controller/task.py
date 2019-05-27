import requests
import json
import time

from client.Code.controller import auth


class Task:
    def __int__(self, start, end, task_time, location, description):
        self.start = start
        self.end = end
        self.task_time = task_time
        self.location = location
        self.description = description


class Manager:
    def __int__(self, user_auth):
        """
        Accepts one user authentication instance
        Acts as the manager of the tasks instances of the respective user instance
        """
        self.user_auth = user_auth

