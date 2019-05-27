import requests
import json


class UserAuth:
    def __init__(self):
        """
        Represents the user and manages its API calls to authenticate user
        Verify the credentials
        Update credentials
        """
        self.__name = None
        self.__token = None

    def get_token(self):
        return self.__token

    def set_token(self, token):
        self.__token = token

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def authenticate(self, name, password):
        """
            Request to API endpoint to verify user credentials
            Return True if successful
            Return False if credentials does not match
        """
        pass

    def create_new_user(self, name, password1, password2):
        """
            Request to to API endpoint to create new user
            Return True if user created succesfully
            Return False if created successfully
        """
        pass
