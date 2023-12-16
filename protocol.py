"""
Author:lia yosef
Date:14.12.23
program name: 2.7
"""


def send_protocol(message):
    length = str(len(message))
    message1 = length.zfill(15)
    message = message1 + message
    return message


def recv_protocol(socket):
    length = socket.recv(15).decode()
    message = socket.recv(int(length)).decode()
    return message