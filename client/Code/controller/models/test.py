import unittest
from client.Code.controller.models.models import Task, TaskList

mock_task_data = {
    "id": 20,
    "topic": "Project Deadline",
    "description": "Send SEP project.",
    "created_at": "2019-05-29T09:18:23.223777Z",
    "start_at": "2019-06-02T06:00:00Z",
    "end_at": "2019-06-02T09:00:00Z",
    "status": False,
    "location": "International College, KMITL",
    "user": 1
}


class TaskModelTest(unittest.TestCase):
    def setUp(self):
        self.task = Task(mock_task_data)

    def testInitialization(self):
        for key in mock_task_data:
            result = self.task.__dict__[key]
            self.assertEqual(result, mock_task_data[key])

    def testUpdateTaskData(self):
        new_data = {
            "id": 20,
            "topic": "Project Deadline",
            "description": "Send SEP project.",
            "created_at": "2019-05-29T09:18:23.223777Z",
            "start_at": "2019-06-02T06:00:00Z",
            "end_at": "2019-06-02T09:00:00Z",
            "status": False,
            "location": "International College, KMITL",
            "user": 1
        }
        self.task.update(new_data)
        for key in new_data.keys():
            result = self.task.__dict__[key]
            self.assertEqual(result, new_data[key])


class TaskListModelTest(unittest.TestCase):

    def testInitializationWithEmptyTask(self):
        tasks = TaskList()
        size = tasks.count()
        self.assertEqual(size, 0)

    def testInitializationWithJson(self):
        tasks = [
            mock_task_data,
            mock_task_data.copy(),
            mock_task_data.copy()
        ]
        task_list = TaskList(tasks)
        size = task_list.count()
        self.assertEqual(size, 3)

    def testAddTask(self):
        task = Task(mock_task_data)
        tasks = [
            mock_task_data,
            mock_task_data.copy(),
            mock_task_data.copy()
        ]
        task_list = TaskList(tasks)
        task_list.add_task(mock_task_data)
        result = task_list.tasks[-1]
        self.assertEqual(result, task)

    def testGetTask(self):
        task = Task(mock_task_data)
        tasks = [
            mock_task_data,
            mock_task_data.copy(),
            mock_task_data.copy()
        ]
        task_list = TaskList(tasks)
        result = task_list.get_task(task.id)
        self.assertEqual(result, task)

    def testUpdateTask(self):
        task = Task(mock_task_data)
        mock_task_data_2 = mock_task_data.copy()
        mock_task_data_3 = mock_task_data.copy()
        mock_task_data_2['id'] = 1
        mock_task_data_3['id'] = 2
        tasks = [
            mock_task_data,
            mock_task_data_2,
            mock_task_data_3
        ]
        task_list = TaskList(tasks)
        new_data = mock_task_data.copy()
        new_data['topic'] = "hello world"
        result = task_list.update_task(task.id, new_data)

        self.assertEqual(result.topic, "hello world")
        self.assertEqual(result, task_list.get_task(task.id))

    def testDeleteTask(self):
        task = Task(mock_task_data)
        mock_task_data_2 = mock_task_data.copy()
        mock_task_data_3 = mock_task_data.copy()
        mock_task_data_2['id'] = 1
        mock_task_data_3['id'] = 2
        tasks = [
            mock_task_data,
            mock_task_data_2,
            mock_task_data_3
        ]
        task_list = TaskList(tasks)
        task_list.delete_task(1)
        self.assertEqual(task_list.get_task(1), None)

    def testCountTask(self):
        task = Task(mock_task_data)
        mock_task_data_2 = mock_task_data.copy()
        mock_task_data_3 = mock_task_data.copy()
        mock_task_data_2['id'] = 1
        mock_task_data_3['id'] = 2
        tasks = [
            mock_task_data,
            mock_task_data_2,
            mock_task_data_3
        ]
        task_list = TaskList(tasks)
        self.assertEqual(task_list.count(), 3)
