from typing import Dict

from client.Code.utility.parsers import DatetimeParser


class Validator:
    def validate(self, data):
        pass


class TaskValidator(Validator):
    """
        :param
        data: Dictionay containing task details

    """

    def validate(self, data: Dict):
        keys = [
            'user',
            'topic',
            'description',
            'created_at',
            'start_at',
            'end_at',
            'status',
            'location'
        ]

        for key in keys:
            try:
                data[key]
            except KeyError:
                return False

        start_at = DatetimeParser.parse(data['start_at'])
        end_at = DatetimeParser.parse(data['end_at'])

        return start_at < end_at


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
