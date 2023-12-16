"""
Author:lia yosef
Date:15.12.23
program name: 2.7
"""
import socket
import logging
import fanctions
import protocol
import os
import shutil

QUEUE_LEN = 1
logging.basicConfig(filename="client.log", level="DEBUG")


def getting_parameter_from_the_client(client_socket, message1):
    """
    gets the parmter from the client
    :param client_socket: a socket
    :param message1: a string message
    :return: the message from the client
    """
    client_socket.send(protocol.send_protocol(message1).encode())
    logging.debug("sending a message request" + message1)
    message2 = protocol.recv_protocol(client_socket)
    logging.debug("i have gotten the parameter:" + message2)
    return message2


def checking_the_existence_of_the_file(path):
    """
    cheacks if the file exsist on the computre
    :param path: the path to the file
    :return: a string contaning error or the path
    """
    if not os.path.isfile(path):
        path = "error"
    return path


def checking_message_dir(path):
    """
    cheacks if the file is one the computure
    :param path:the path to the file
    :return:a string conaning the path or error
    """
    if not os.path.isdir(path):
        path = "error"
    return path


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        my_socket.bind(('0.0.0.0', 1729))
        my_socket.listen(QUEUE_LEN)
        while True:
            client_socket, client_address = my_socket.accept()
            try:
                request = protocol.recv_protocol(client_socket)
                logging.debug("getting the request" + request)
                while request != "EXIT":
                    if request == "DIR":
                        path = getting_parameter_from_the_client(client_socket, "enter path")
                        path = checking_message_dir(path)
                        if path == "error":
                            comment = "the path dose not exist"
                        else:
                            comment = fanctions.dir_filename(path)
                    elif request == "DELETE":
                        path = getting_parameter_from_the_client(client_socket, "enter path")
                        path = checking_the_existence_of_the_file(path)
                        if path == "error":
                            comment = "the path dose not exist"
                        else:
                            fanctions.delete(path)
                            comment = "deleted"
                    elif request == "COPY":
                        path_copy = getting_parameter_from_the_client(client_socket, "enter path to copy")
                        path_copy = checking_the_existence_of_the_file(path_copy)
                        path_paste = getting_parameter_from_the_client(client_socket, "enter path to paste")
                        if path_copy == "error":
                            comment = "the path dose not exists"
                        else:
                            fanctions.copy(path_copy,path_paste)
                            comment = "copied"
                    elif request == "EXECUTE":
                        path = getting_parameter_from_the_client(client_socket, " enter path")
                        comment = fanctions.execute(path)
                    elif request == "SEND PHOTO":
                        comment = fanctions.take_screenshot()

                    else:
                        comment = "illegal request pls enter DIR,DELETE,COPY,EXECUTE,SEND PHOTO,EXIT"
                    logging.debug("sending a comment " + comment)
                    client_socket.send(protocol.send_protocol(comment).encode())
                    request = protocol.recv_protocol(client_socket)
                    logging.debug("getting a request " + request)
            except socket.error as err:
                logging.error('received socket error on client socket' + str(err))
                print('received socket error on client socket' + str(err))

            finally:
                msg = "EXIT"
                try:
                    client_socket.send(protocol.send_protocol(msg).encode())
                except socket.error as err:
                    logging.error("could not disconnect" + str(err))
                client_socket.close()
    except socket.error as err:
        logging.error('received socket error on server socket' + str(err))
        print('received socket error on server socket' + str(err))

    finally:
        my_socket.close()


if __name__ == "__main__":
    main()

