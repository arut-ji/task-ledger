class Task:
    """
        When loading tasks from database no fields shall be None value
        When creating new tasks to be added, task_id and created_at have to be have value None
        sdate and edate are QDate Objects which is used to verify date before POST request to api endpoint
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

        self.start_date_object = None
        self.end_date_object = None
        self.start_time_object = None
        self.end_time_object = None

    def set_date_time_object(self, sdate, edate, stime, etime):
        self.start_date_object = sdate
        self.end_date_object = edate
        self.start_time_object = stime
        self.end_time_object = etime

    def check_format(self):
        if self.start_date_object <= self.end_date_object:
            a = self.start_time_object <= self.end_time_object
            if self.start_date_object < self.end_date_object:
                return True
            elif self.start_time_object <= self.end_time_object:
                return True
        return False

    def update(self, data):
        """
            Is used when refreshing data from the database
        """

        self.id = data["id"]
        self.topic = data["topic"]
        self.desc = data["description"]
        self.created_at = data["created_at"]
        self.start_at = data["start_at"]
        self.end_at = data["end_at"]
        self.status = data["status"]
        self.location = data["location"]
        self.user = data["user"]

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
