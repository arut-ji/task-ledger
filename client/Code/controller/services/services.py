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
            Request to API endpoint to verify user credentials
            Return True if successful
            Return False if credentials does not match
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
            Return True if user created succesfully
            Return False if created successfully
        """

        payload = {
            "username": username,
            "password1": password1,
            "password2": password2
        }

        response = requests.post(REGISTRATION_API, data=payload)

        if response.status_code == 201:
            return response.json()

        return None


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
