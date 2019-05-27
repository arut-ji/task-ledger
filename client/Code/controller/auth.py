import requests
import json


class UserAuth:
    def __init__(self):
        """
        Represents the user and manages its API calls to authenticate user
        Verify the credentials
        Update credentials
        """
        self.__username = None
        self.__token = None
        self.login_url = "http://task-ledger.appspot.com/rest-authlogin/"
        self.registration_url = "http://task-ledger.appspot.com/rest-auth/registration/"

    def get_token(self):
        return self.__token

    def set_token(self, token):
        self.__token = token

    def get_name(self):
        return self.__username

    def set_name(self, username):
        self.__username = username

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
            return True
        return False

    def registration(self, username, password1, password2):
        """
            Request to to API endpoint to create new user
            Return True if user created succesfully
            Return False if created successfully
        """
        if len(password1) < 8:
            return False
        elif password1 != password2:
            return False

        payload = {
            "username": username,
            "password1": password1,
            "password2": password2
        }

        res = requests.post(self.registration_url, data=payload)
        if res.status_code == 201:
            res_data = json.loads(res.text)
            self.__token = res_data["key"]
            self.__username = username
            return True
        return False


u = UserAuth()
print(u.login("admin", "admin"))
