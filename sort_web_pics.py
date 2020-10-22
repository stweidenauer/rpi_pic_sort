#!/usr/bin/python3

import os
import shutil
from datetime import datetime, timedelta


# returns ten days prior string formatted: YYYY-MM-DD
def find_last_ten_days():
    day_list = []
    today = datetime.now()
    for i in range(10):
        day_list.append((today - timedelta(days=i)).strftime("%Y-%m-%d"))
    return day_list


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

        # move pictures to new folder
        os.chdir(base_dir)
        new_target_dir = os.path.join(target_dir, item)
        for picture in os.listdir():
            if picture.startswith(item):
                shutil.move(picture, new_target_dir)

    # removes folder that is older than 10 days
    os.chdir(target_dir)
    for folder in os.listdir():
        if folder[:10] in list_last_ten_days:
            continue
        elif os.path.isdir(folder):
            shutil.rmtree(folder)


if __name__ == "__main__":
    start()
