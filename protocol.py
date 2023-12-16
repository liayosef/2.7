"""
Author:lia yosef
Date:14.12.23
program name: 2.7
"""


def send_protocol(message):
    """
    returns a string with the lenght
    :param message: the message
    :return: the message with her lenght
    """
    length = str(len(message))
    message1 = length.zfill(4)
    message = message1 + message
    return message


def recv_protocol(socket):
    """
    gets the socket the lenght and the message
    :param socket:the socket contaninig the full message
    :return:the messag without her lenght
    """
    length = " "
    print("HELLO")
    message = " "
    try:
        while len(length) < 4:
            length += socket.recv(4-len(length))
        while len(message) < int(length):
            message += socket.recv(int(length)-len(message))
    except:
        print("NMOI")
        message = "error"
    return message
