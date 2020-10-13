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
    return (datetime.now() - timedelta(days=9)).strftime("%Y-%m-%d")


def start():
    # define base_dir and target directory
    base_dir = os.path.join('/', 'home', 'pi', 'webcam')
    target_dir = os.path.join('/', 'home', 'pi', 'flask_app', 'app', 'static')

    # create target folders
    list_last_ten_days = find_last_ten_days()
    for item in list_last_ten_days:
        os.chdir(target_dir)
        if not os.path.isdir('./' + item):
            os.mkdir(item)
            print('Directory ' + item + 'created')

    # move pictures to new folder
    os.chdir(base_dir)
    print(base_dir)
    for item in list_last_ten_days:
        new_target_dir = os.path.join(target_dir, item)
        for picture in os.listdir():
            if picture.startswith(item):
                shutil.move(picture, new_target_dir)
                print('picture ' + picture + 'moved')

    # removes folders that is 10 days old
    os.chdir(target_dir)
    ten_days = ten_days_prior()
    for folder in os.listdir():
        if folder.startswith(ten_days) and os.path.isdir(folder):
            shutil.rmtree(folder)
            print('Folder gefunden und gelöscht')


if __name__ == "__main__":
    start()
