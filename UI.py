from tkinter import *
import tkinter.messagebox
import socket
from SocketWrapper import *

IP = '127.0.0.1'
PORT = 8822


class Application(Frame):

    def open_socket(self):
        self.server_socket = socket.socket()
        self.server_socket.connect((IP, PORT))
        self.socket_wrapper = socket_wrapper(self.server_socket)

    def close_socket(self):
        self.server_socket.close()

    def signup(self):
        self.passFrame.pack_forget()
        self.passConfirmFrame.pack({"side": "bottom"})
        self.passFrame.pack({"side": "bottom"})
        user_name = self.userFrame.children[str(self.userName).split('.')[3]].get("1.0",END)
        user_pass = self.passFrame.children[str(self.userPass).split('.')[3]].get("1.0",END)
        user_passconfirm = self.passConfirmFrame.children[str(self.userConfPass).split('.')[3]].get("1.0",END)
        if not user_pass == user_passconfirm:
            print("Your password is not the same as the confirm password.")
        else:
            self.open_socket()
            self.socket_wrapper.send_with_len("signon")
            self.socket_wrapper.send_with_len(user_name)
            self.socket_wrapper.send_with_len(user_pass)

            data_from_server = self.socket_wrapper.read_with_len()
            print(data_from_server)
            tkinter.messagebox.showinfo(title=None, message=data_from_server)
            self.close_socket()

    def login(self):
        self.passConfirmFrame.pack_forget()
        user_name = self.userFrame.children[str(self.userName).split('.')[3]].get("1.0",END)
        user_pass = self.passFrame.children[str(self.userPass).split('.')[3]].get("1.0",END)
        self.open_socket()
        self.socket_wrapper.send_with_len("login")
        self.socket_wrapper.send_with_len(user_name)
        self.socket_wrapper.send_with_len(user_pass)

        data_from_server = self.socket_wrapper.read_with_len()
        print(data_from_server)
        tkinter.MessageBox.showinfo(title=None, message=data_from_server)
        self.close_socket()

    def createWidgets(self):

        self.buttonsFrame = Frame(self)
        self.buttonsFrame.pack({"side": "bottom"})

        self.passFrame = Frame(self)
        self.passFrame.pack({"side": "bottom"})

        self.passConfirmFrame = Frame(self)

        self.userFrame = Frame(self)
        self.userFrame.pack()

        varUserNameLanel = StringVar()
        varUserNameLanel.set("user name")
        self.userLabel = Label(self.userFrame, textvariable=varUserNameLanel, relief=RAISED, height=2, bd=10, fg="blue", bg="light pink")
        self.userLabel.pack({"side": "left"})

        self.userName = Text(self.userFrame, height=2, bd=10)
        self.userName.pack({"side": "left"})

        varUserPassLanel = StringVar()
        varUserPassLanel.set("password")
        self.passLabel = Label(self.passFrame, textvariable=varUserPassLanel, relief=RAISED, height=2, bd=10, fg="blue", bg="light pink")
        self.passLabel.pack({"side": "left"})

        self.userPass = Text(self.passFrame, height=2, bd=10)
        self.userPass.pack({"side": "left"})

        varUserPassConfLanel = StringVar()
        varUserPassConfLanel.set("confirm password")
        self.passConfLabel = Label(self.passConfirmFrame, textvariable=varUserPassConfLanel, relief=RAISED, height=2, bd=10, fg="blue", bg="light pink")
        self.passConfLabel.pack({"side": "left"})

        self.userConfPass = Text(self.passConfirmFrame, height=2, bd=10)
        self.userConfPass.pack({"side": "left"})


        self.loginBtn = Button(self.buttonsFrame)
        self.loginBtn["text"] = "Login"
        self.loginBtn["fg"] = "blue"
        self.loginBtn["bg"] = "light pink"
        self.loginBtn["command"] = self.login # -*-Calls for login action -*-
        self.loginBtn.pack({"side": "left"})

        self.signupBtn = Button(self.buttonsFrame)
        self.signupBtn["text"] = "Signup"
        self.signupBtn["fg"] = "blue"
        self.signupBtn["bg"] = "light pink"
        self.signupBtn["command"] = self.signup

        self.signupBtn.pack({"side": "left"})


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


def main():

    root = Tk()
    app = Application(master=root)
    app.mainloop()
    root.destroy()
if __name__ == '__main__':
    main()
