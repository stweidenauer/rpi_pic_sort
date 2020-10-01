import os
from datetime import datetime


def find_today():
    today = datetime.today()
    pass


def find_ten_days_prior():
    pass


def start():
    today = find_today()
    ten_days_prior = find_ten_days_prior()
    path_to_pictures = os.join.path('webcam')
    for file in os.listdir(path_to_pictures):
        if file.startswith(today):
            os.mkdir()

    pass


if __name__ == "__main__":
    start()
