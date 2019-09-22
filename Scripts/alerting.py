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

    def info(self, message: str):
        self.alert_dict[message] = 'INFO'

    def warn(self, message: str):
        self.alert_dict[message] = "WARN"
        self.alert_level = Alert.WARN

    def error(self, message: str):
        self.alert_dict[message] = "ERROR"
        self.alert_level = Alert.ERROR

    def send_message(self):
        if self.alert_level:
            alert_color = 'green box'
        elif self.alert_level == Alert.WARN:
            alert_color = 'yellow box'
        else:
            alert_color = "red box"

        post_message = f'{{"bot_id": "ac960a6f08227f9b603e8d8859", "text": {self.alert_dict}, "attachments": ' \
                       f'[{{"type": "image", "url": "{alert_color}"}}]}}'

        print(post_message)

    def __str__(self):
        alert_str = f"Alerting level: {self.alert_level}\n"
        for k, v in self.alert_dict.items():
            alert_str += f"{k}: {v}"


alert = Alerting()


def info(message: str):
    alert.info(message)


def warn(message: str):
    alert.warn(message)


def error(message: str):
    alert.error(message)


def send_message():
    alert.send_message()


if __name__ == '__main__':
    pass
