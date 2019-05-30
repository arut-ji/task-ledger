from PySide2.QtCore import QTime, QDate
from dateutil import parser
from datetime import datetime

class DatetimeParser:
    @staticmethod
    def parse(datetime_string: str):
        return parser.parse(datetime_string)

    @staticmethod
    def fromQDateAndQTime(qdate: QDate, qtime: QTime):
        native_date = qdate.toPython()
        native_time = qtime.toPython()
        return datetime.combine(native_date, native_time)


