from dateutil import parser


class DatetimeParser:
    @staticmethod
    def parse(datetime_string: str):
        return parser.parse(datetime_string)



