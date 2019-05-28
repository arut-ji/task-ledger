class Task:
    def __init__(self, task_id, user, topic, desc, created_at, start_at, status):
        self.id = task_id
        self.user = user
        self.topic = topic
        self.desc = desc
        self.created_at = created_at
        self.start_at = start_at
        self.status = status

    def update(self, task_id, user, topic, desc, created_at, start_at, status):
        self.id = task_id
        self.user = user
        self.topic = topic
        self.desc = desc
        self.created_at = created_at
        self.start_at = start_at
        self.status = status

    def __str__(self):
        return str({
            "id": self.id,
            "user": self.user,
            "topic": self.topic,
            "description": self.desc,
            "created_at": self.created_at,
            "start_at:": self.start_at,
            "status": self.status
        })
