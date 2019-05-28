class Task:
    """
        When loading tasks from database no fields shall be None value
        When creating new tasks to be added, task_id and created_at have to be have value None
    """

    def __init__(self, task_id, topic, desc, created_at, start_at, end_at, status, location, user):
        self.id = task_id
        self.topic = topic
        self.desc = desc
        self.created_at = created_at
        self.start_at = start_at
        self.end_at = end_at
        self.status = status
        self.location = location
        self.user = user

    def update(self, task_id, topic, desc, created_at, start_at, end_at, status, location, user):
        """
            Is used when refreshing data from the database
        """

        self.id = task_id
        self.topic = topic
        self.desc = desc
        self.created_at = created_at
        self.start_at = start_at
        self.end_at = end_at
        self.status = status
        self.location = location
        self.user = user

    def __str__(self):
        return str({
            "id": self.id,
            "topic": self.topic,
            "description": self.desc,
            "created_at": self.created_at,
            "start_at:": self.start_at,
            "end_at": self.end_at,
            "status": self.status,
            "location": self.location,
            "user": self.user
        })
