"""
Author:lia yosef
Date:14.12.23
program name: 2.7
"""
import glob
import os
import shutil
import subprocess
from PIL import ImageGrab
import base64


ERR = "an error happened"


def dir_filename(path):
    """

    :param path:
    :return:
    """
    try:
        file_name = r'' + path + '\\*.*'
        file_list = glob.glob(file_name)
        file_list = ",".join(file_list)
        return file_list
    except ValueError:
        return ERR


def delete(path):
    os.remove(path)


def copy(file_name, file_destination):
    shutil.copy(r''+file_name, r''+file_destination)


def execute(path):
    comment = "works well"
    try:
        subprocess.call(path)
    except Exception as err:
        comment = str(err)
    return comment


def take_screenshot():
    comment = "taken"
    try:
        file_path = "screen.jpg"
        screenshot = ImageGrab.grab()
        screenshot.save(file_path, 'jpg')
    except Exception as err:
        comment = "could not take a picture:" + str(err)
    return comment


def send_photo():
    if os.path.isfile("screen.jpg"):
        with open("screen.jpg", "rb") as imageFile:
            comment =base64.b64decode(imageFile.read())
        comment = comment.decode()
    else:
        comment = ERR
    return comment
