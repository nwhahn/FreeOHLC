import requests
import enum


class Alert(enum):
    INFO = 1
    WARN = 2
    ERROR = 3


class Alerting:
    def __init__(self):
        self.alert_dict = {}
        self.alert_level = Alert.INFO

    def info(self, message):
        self.alert_dict[message] = 'INFO'

    def warn(self, message):
        self.alert_dict[message] = "WARN"
        self.alert_level = Alert.WARN

    def error(self, message):
        self.alert_dict[message] = "ERROR"
        self.alert_level = Alert.ERROR

    def __str__(self):
        str = f"Alerting level: {}"
        for k,v in self.dict:


alert = Alerting()


def info(message):
    alert.info(message)


def warn(message):
    alert.warn(message)


def error(message):
    alert.error(message)


def send_message():



if __name__ == '__main__':
    pass