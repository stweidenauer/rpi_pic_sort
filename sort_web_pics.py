#! /usr/bin/python3

import os
import shutil
from datetime import datetime, timedelta


# returns today string formatted: YYYY-MM-DD
def find_today():
    return datetime.now().strftime("%Y-%m-%d")


# returns ten days prior string formatted: YYYY-MM-DD
def find_last_ten_days():
    day_list = []
    today = datetime.now()
    for i in range(10):
        day_list.append((today - timedelta(days=i)).strftime("%Y-%m-%d"))
    return day_list


def ten_days_prior():
    return (datetime.now()-timedelta(days=10)).strftime("%Y-%m-%d")


def start():
    # define base_dir and target directory
    base_dir = os.path.join('/', 'home', 'pi', 'webcam')
    target_dir = os.path.join('/', 'home', 'pi', 'flask_app', 'app', 'static')

    # create target folder
    os.chdir(target_dir)
    for item in find_last_ten_days():
        if not os.path.isdir('./' + item):
            os.mkdir(item)
        os.chdir(base_dir)
        for picture in os.listdir():
            if picture.startswith(item):
                shutil.move(picture, os.path.join(target_dir, item))

    # removes folders that is 10 days old
    for folder in os.listdir():
        if folder.startswith(ten_days_prior()) and os.path.isdir(folder):
            shutil.rmtree(folder)


if __name__ == "__main__":
    start()
