#! /usr/bin/python3

import os
import shutil
from datetime import datetime, timedelta


# returns today string formatted: YYYY-MM-DD
def find_today():
    return datetime.now().strftime("%Y-%m-%d")


# returns ten days prior string formatted: YYYY-MM-DD
def find_ten_days_prior():
    ten_days = timedelta(days=10)
    return (datetime.today() - ten_days).strftime("%Y-%m-%d")


def start():
    # define base_dir and change to
    base_dir = os.path.join('/', 'home', 'pi', 'webcam')
    os.chdir(base_dir)

    # finds today and 10 days prior in a formated type
    today = find_today()
    ten_days_prior = find_ten_days_prior()

    # copies pictures of today in an folder with the same name
    if not os.path.isdir('./' + today):
        os.mkdir(today)
    for picture in os.listdir():
        if picture.startswith(today):
            shutil.move(picture, today)

    # removes folders that is 10 days old
    for folder in os.listdir():
        if folder.startswith(ten_days_prior) and os.path.isdir(folder):
            shutil.rmtree(folder)


if __name__ == "__main__":
    start()
