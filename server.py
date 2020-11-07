import socket
from SocketWrapper import *
from sql import *

username = "null"
password = "null"
con_pass = "null"
IP = '0.0.0.0'
PORT = 8821

incorrect_message = "one of the details is incorrect"

class server:

    def receive_client_request(self):
        command = self.socket_wrapper.read_with_len()
        username = self.socket_wrapper.read_with_len()
        password = self.socket_wrapper.read_with_len()
        if command == "login":
            self.login(username, password)
        elif command == "signon":
            self.signup(username, password)

    def login(self, username, password):
        result = self.db.get_user(username)
        if result == None:
            self.socket_wrapper.send_with_len(incorrect_message)
        else:
            if password == result[1]:
                self.socket_wrapper.send_with_len("user logged in sucessfully")
            else:
                self.socket_wrapper.send_with_len(incorrect_message)


    def signup(self, username, password):
        result = self.db.insert_user(username, password)
        if result == True:
            self.socket_wrapper.send_with_len("user inserted sucessfully")
        else:
            self.socket_wrapper.send_with_len("user logged in sucessfully")

    def __init__(self):
        self.db = DB()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((IP, PORT))
        self.server_socket.listen(1)
        print("Server is up and running")
        while True:
            (client_socket, client_address) = self.server_socket.accept()
            print("client connected")
            self.socket_wrapper = socket_wrapper(client_socket)
            self.receive_client_request()
            client_socket.close()
        self.server_socket.close()

def main():
    server()

if __name__ == '__main__':
    main()

