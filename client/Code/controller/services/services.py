import datetime

import requests
from typing import Dict, List
from client.Code.controller.models.models import Task, TaskList
import json

# Base API endpoints
BASE_API = "http://task-ledger.appspot.com/"

# REST Authentication API endpoints
AUTHENTICATION_API = BASE_API + "rest-auth/"
LOGIN_API = AUTHENTICATION_API + "login/"
REGISTRATION_API = AUTHENTICATION_API + "registration/"

# Tasks API endpoint
TASKS_API = BASE_API + 'api/tasks/'
USER_TASKS_API = BASE_API + "api/users/{}/tasks/"


class BaseService:
    pass


class AuthService(BaseService):

    @staticmethod
    def login(username, password):

        """
            :param username: user's username
            :type username: str

            :param password: user's password
            :type password: str

            :return user's id details and token
            :rtype  Dict or None

        """

        payload = {
            "username": username,
            "password": password
        }

        response = requests.post(LOGIN_API, data=payload)

        if response.status_code == 200:
            return response.json()

        return None

    @staticmethod
    def register(username, password1, password2):
        """
            Request to to API endpoint to create new user

            :param username: user's username
            :type username: str
            :param password1: user's password
            :type password1: str
            :param password2: user's confirmed password
            :type password2: str

            :return empty list if successful, error messages if unsuccessful
            :rtype list or dict
        """

        payload = {
            "username": username,
            "password1": password1,
            "password2": password2
        }

        response = requests.post(REGISTRATION_API, data=payload)

        if response.status_code == 201:
            return []
        return response.json()


class TaskService(BaseService):

    @staticmethod
    def create_task(payload: Dict):
        response = requests.post(
            url=TASKS_API,
            data=payload
        )

        if response.status_code == 201:
            return Task(response.json())
        else:
            return None

    @staticmethod
    def update_task(task_id, payload):
        update_task_endpoint = TASKS_API + str(task_id) + '/'

        if payload['status']:
            payload['done_at'] = str(datetime.datetime.now())

        response = requests.put(
            url=update_task_endpoint,
            data=payload
        )

        if response.status_code == 200:
            return Task(response.json())
        return None

    @staticmethod
    def retrieve_task(task_id):
        retrieve_task_endpoint = TASKS_API + str(task_id) + '/'
        response = requests.get(
            url=retrieve_task_endpoint,
        )

        if response.status_code == 200:
            return Task(response.json())
        return None

    @staticmethod
    def delete_task(task_id):
        delete_task_endpoint = TASKS_API + str(task_id) + '/'
        response = requests.delete(
            url=delete_task_endpoint
        )

        if response.status_code == 204:
            return True
        else:
            return False

    @staticmethod
    def list_task(user_id):
        api_endpoint = USER_TASKS_API.format(str(user_id))
        response = requests.get(
            url=api_endpoint
        )
        if response.status_code == 200:
            return TaskList(response.json())
        return None
