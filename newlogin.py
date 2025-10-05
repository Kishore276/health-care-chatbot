import tkinter as tk
from tkinter import messagebox
import os

class AuthenticationSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x250")
        self.root.title("Account Login")
        self.main_account_screen()

    def main_account_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
        tk.Label(self.root, text="").pack()
        tk.Button(self.root, text="Login", height="2", width="30", command=self.login).pack()
        tk.Label(self.root, text="").pack()
        tk.Button(self.root, text="Register", height="2", width="30", command=self.register).pack()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def register(self):
        self.clear_screen()
        self.register_screen = self.root
        self.register_screen.title("Register")
        self.register_screen.geometry("300x250")

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        tk.Label(self.register_screen, text="Please enter the details below", bg="blue").pack()
        tk.Label(self.register_screen, text="").pack()
        tk.Label(self.register_screen, text="Username * ").pack()
        self.username_entry = tk.Entry(self.register_screen, textvariable=self.username)
        self.username_entry.pack()
        tk.Label(self.register_screen, text="Password * ").pack()
        self.password_entry = tk.Entry(self.register_screen, textvariable=self.password, show='*')
        self.password_entry.pack()
        tk.Label(self.register_screen, text="").pack()
        tk.Button(self.register_screen, text="Register", width=10, height=1, bg="blue", command=self.register_user).pack()

    def register_user(self):
        username_info = self.username.get()
        password_info = self.password.get()
        file = open(username_info, "w")
        file.write(username_info + "\n")
        file.write(password_info)
        file.close()

        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

        tk.Label(self.root, text="Registration Success", fg="green", font=("calibri", 11)).pack()
        tk.Button(self.root, text="Click Here to proceed", command=self.main_account_screen).pack()

    def login(self):
        self.clear_screen()
        self.login_screen = self.root
        self.login_screen.title("Login")
        self.login_screen.geometry("300x250")
        tk.Label(self.login_screen, text="Please enter details below to login").pack()
        tk.Label(self.login_screen, text="").pack()

        self.username_verify = tk.StringVar()
        self.password_verify = tk.StringVar()

        tk.Label(self.login_screen, text="Username * ").pack()
        self.username_login_entry = tk.Entry(self.login_screen, textvariable=self.username_verify)
        self.username_login_entry.pack()
        tk.Label(self.login_screen, text="").pack()
        tk.Label(self.login_screen, text="Password * ").pack()
        self.password_login_entry = tk.Entry(self.login_screen, textvariable=self.password_verify, show='*')
        self.password_login_entry.pack()
        tk.Label(self.login_screen, text="").pack()
        tk.Button(self.login_screen, text="Login", width=10, height=1, command=self.login_verify).pack()

    def login_verify(self):
        username1 = self.username_verify.get()
        password1 = self.password_verify.get()
        self.username_login_entry.delete(0, tk.END)
        self.password_login_entry.delete(0, tk.END)

        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                self.login_sucess()
            else:
                self.password_not_recognised()
        else:
            self.user_not_found()

    def login_sucess(self):
        messagebox.showinfo("Success", "Login Success")
        self.main_account_screen()

    def password_not_recognised(self):
        messagebox.showerror("Error", "Invalid Password")

    def user_not_found(self):
        messagebox.showerror("Error", "User Not Found")

if __name__ == "__main__":
    root = tk.Tk()
    app = AuthenticationSystem(root)
    root.mainloop()