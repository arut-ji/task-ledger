import unittest
from client.Code.controller.services.services import AuthService, TaskService
from client.Code.controller.models.models import TaskList


class AuthServiceTest(unittest.TestCase):

    def testLogin(self):
        username = 'admin'
        password = 'admin'
        result = AuthService.login(username, password)
        token = result['key']
        user = result['user']

        self.assertGreater(len(token), 1)
        self.assertEqual(user['username'], username)

    def testRegister(self):
        pass


class TaskServiceTest(unittest.TestCase):

    def testCreateTask(self):
        mock_data = {
            "topic": "Test Service",
            "description": "Test Service",
            "start_at": "2019-06-02T06:00:00Z",
            "end_at": "2019-06-02T06:00:00Z",
            "status": False,
            "location": "KMITL",
            "user": 1
        }
        token = 'token 6bdf6d2c610e585fd8584f2bc51127df87fcec71'
        result = TaskService.create_task(token, mock_data)
        self.assertEqual(result.topic, mock_data["topic"])
        self.assertEqual(result.description, mock_data["description"])
        self.assertEqual(result.start_at, mock_data["start_at"])
        self.assertEqual(result.end_at, mock_data["end_at"])
        self.assertEqual(result.status, mock_data["status"])
        self.assertEqual(result.location, mock_data["location"])
        self.assertEqual(result.user, mock_data["user"])

    def testRetrieveTask(self):
        mock_data = {
            "topic": "Test Service",
            "description": "Test Service",
            "start_at": "2019-06-02T06:00:00Z",
            "end_at": "2019-06-02T06:00:00Z",
            "status": False,
            "location": "KMITL",
            "user": 1
        }
        result = TaskService.create_task(mock_data)
        task = TaskService.retrieve_task(result.id)
        self.assertEqual(task.id, result.id)

    def testUpdateTask(self):
        mock_data = {
            "topic": "Test Update Service",
            "description": "Test Service",
            "start_at": "2019-06-02T06:00:00Z",
            "end_at": "2019-06-02T06:00:00Z",
            "status": True,
            "location": "KMITL",
            "user": 1
        }
        task = TaskService.update_task(26, mock_data)
        self.assertEqual(task.id, 26)
        self.assertEqual(task.topic, mock_data["topic"])
        self.assertEqual(task.description, mock_data["description"])
        self.assertEqual(task.status, mock_data["status"])
        self.assertEqual(task.location, mock_data["location"])

    def testDeleteTask(self):
        pass

    def testListAllTask(self):
        task_list = TaskService.list_task(1)
        self.assertEqual(type(task_list), TaskList)
