import requests
import json


class AuthService:
    def __init__(self):
        """
            Represents the user and manages its API calls to authenticate user
            Verify the credentials
            Update credentials
            Get user information through JWT
        """
        self.__username = None
        self.__token = None
        self.__user_id = 1  # For testing

        self.login_url = "http://task-ledger.appspot.com/rest-auth/login/"
        self.registration_url = "http://task-ledger.appspot.com/rest-auth/registration/"
        self.task_url = None
        self.all_tasks_url = "http://task-ledger.appspot.com/api/tasks/"

    def get_token(self):
        return self.__token

    def set_token(self, token):
        self.__token = token

    def get_name(self):
        return self.__username

    def set_name(self, username):
        self.__username = username

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_user_id(self):
        return self.__user_id

    def login(self, username, password):
        """
            Request to API endpoint to verify user credentials
            Return True if successful
            Return False if credentials does not match
        """

        payload = {
            "username": username,
            "password": password
        }

        res = requests.post(self.login_url, data=payload)

        if res.status_code == 200:
            res_data = json.loads(res.text)
            self.__token = res_data["key"]
            self.__username = username
            self.__user_id = res_data["user"]["id"]
            self.task_url = "http://task-ledger.appspot.com/api/users/{}/tasks/".format(self.__user_id)
            return True
        # print("hello")
        return False

    def registration(self, username, password1, password2):
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

        res = requests.post(self.registration_url, data=payload)

        res_data = json.loads(res.text)
        print(res_data)

        if res.status_code == 201:
            res_data = json.loads(res.text)
            self.__token = res_data["key"]
            self.__username = username
            self.__user_id = res_data["user"]["id"]
            self.task_url = "http://task-ledger.appspot.com/api/users/{}/tasks/".format(self.__user_id)
            return True
        return False

    # def get_user_details(self):
    #     res = requests.get(self.user_url, headers={"Authorization": "Token {}".format(self.__token)})
    #     res_data = json.loads(res.text())
    #     self.__user_id = res_data["id"]


# u = UserAuth()
# u.login("admin", "admin")
# u.get_user_task()

# params = {"status": False}
# res = requests.get("http://task-ledger.appspot.com/api/users/10/tasks", params=params)
# print(res.status_code)
# print(res.json())
