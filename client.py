import socket
import os
import logging
import protocol
import base64
from PIL import Image

IP = "127.0.0.1"
PORT = 1729
logging.basicConfig(filename="client.log", level="DEBUG")


def sending_parameter(response, my_socket):
    print("server requested " + response)
    path = input("pls enter a message: ")
    logging.debug("sending a path " + path)
    my_socket.send(protocol.send_protocol(path).encode())
    response = protocol.recv_protocol(my_socket)
    logging.debug("getting a response " + response)
    return response


def checking_the_msg(message):
    if (message == "DIR" or message == "DELETE" or message == "COPY" or message == "EXECUTE" or
            message == " TAKE SCREENSHOT " or message == "SEND PHOTO"):
        return True
    else:
        return False


def main():
    my_socket = socket.socket()
    try:
        my_socket.connect((IP, PORT))
        msg = input("pls enter a request: ")
        while checking_the_msg(msg):
            my_socket.send(protocol.send_protocol(msg).encode())
            response = protocol.recv_protocol(my_socket)
            logging.debug("server responded with " + response)
            while response != "EXIT":
                if msg == "DIR":
                    response = sending_parameter(response, my_socket)
                elif msg == "DELETE":
                    response = sending_parameter(response, my_socket)
                elif msg == "EXECUTE":
                    response = sending_parameter(response, my_socket)
                elif msg == "COPY":
                    response = sending_parameter(response, my_socket)
                    response = sending_parameter(response, my_socket)
                elif msg == "SEND PHOTO":
                    if response != "error":
                        img = base64.b64decode(response)
                        file_name = "screen.jpg"
                        with open(file_name, 'wb') as f:
                            f.write(img)
                        image = Image.open(file_name)
                        image.show()
                    else:
                        print("there isn't a picture")
                print(response)
                msg= input("pls enter a request:")
                my_socket.send(protocol.send_protocol(msg).encode())
                response = protocol.recv_protocol(my_socket)
                logging.debug("server responded with" + response)

    except socket.error as error:
        logging.debug("socket error:" + str(error))
        print("socket error:" + str(error))

    finally:
        my_socket.close()


if __name__ == "__main__":
    main()