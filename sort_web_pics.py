import os
import shutil
from datetime import datetime


def find_today():
    return datetime.now().strftime("%Y-%m-%d")


def find_ten_days_prior():
    pass


def start():
    base_dir = os.path.join('home', 'pi', 'webcam')
    os.chdir(base_dir)
    today = find_today()
    # ten_days_prior = find_ten_days_prior()
    os.mkdirs(today)
    for picture in os.listdir():
        if picture.startswith(today):
            shutil.move(picture, today)

    pass


if __name__ == "__main__":
    start()
