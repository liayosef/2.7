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
import socket


ERR = "an error happened"


def dir_filename(path):
    """
     returns list of files
    :param path:the path a string
    :return:file list
    """
    try:
        file_name = r'' + path + '\\*.*'
        file_list = glob.glob(file_name)
        file_list = ",".join(file_list)
        return file_list
    except ValueError:
        return ERR


def delete(path):
    """
    delets a file
    :param path: name of the file
    :return: none
    """
    os.remove(path)


def copy(file_name, file_destination):
    """
    copies a file into another destnation
    :param file_name: the name of the file
    :param file_destination: the name of the destnation
    :return: none
    """
    shutil.copy(r''+file_name, r''+file_destination)


def execute(path):
    """
    cheacks if the program works well
    :param path:the name of the program
    :return: a string comment
    """
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
        ImageGrab.grab(all_screens=True).save(file_path)
        with open(file_path, 'rb') as img:
            comment = base64.b64encode(img.read()).decode('utf-8')

        print(comment)
        print(len(comment))
    except (OSError, socket.error) as err:
        comment = "could not take a picture:" + str(err)
    return comment


def send_photo():
    """
    opens the photo
    :return: a string comment
    """
    if os.path.isfile("screen.jpg"):
        with open("screen.jpg", "rb") as imageFile:
            comment = base64.b64decode(imageFile.read())
        comment = comment.decode()
    else:
        comment = ERR
    return comment
