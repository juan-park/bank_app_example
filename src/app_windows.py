import tkinter as tk  
from tkinter import font as tkfont
from .db import validate_login, add_user, get_user_name

class AccountBalance(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # TODO: Create your own set of windows here!
        pass

class Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.width = 400
        self.height = 300
        self.controller = controller
        
        self.welcome_message = tk.Label(self, text="placeholder", font=controller.title_font)
        self.welcome_message.pack(side="top", fill="x", pady=10)
        account_balance_button = tk.Button(self, text="View account balance",
                           command=lambda: "Place your own code here!")
        account_balance_button.pack()
        update_button = tk.Button(self, text="Update user information",
                           command=lambda: "Place your own code here!")
        update_button.pack()
        withdraw_button = tk.Button(self, text="Withdraw money",
                           command=lambda: "Place your own code here!")
        withdraw_button.pack()
        deposit_button = tk.Button(self, text="Deposit money",
                           command=lambda: "Place your own code here!")
        deposit_button.pack()
        logout_button = tk.Button(self, text="Log out",
                           command=lambda: controller.show_frame("LogIn"))
        logout_button.pack()
    
    def _update_on_load(self):
        """Custom function that runs everytime this page displays."""
        user_id = self.controller.userID.get()
        firstname, lastname = get_user_name(user_id)
        print(f"Welcome {firstname} {lastname}!")
        self.welcome_message['text'] = f"Welcome {firstname} {lastname}!"

class CreateAccount(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.width = 480
        self.height = 400
        self.controller = controller
        
        label = tk.Label(self, text="Create account page", font=controller.title_font)
        label.grid(row=0, column=0)
        
        usernameLabel = tk.Label(self, text="Username", font=controller.title_font).grid(row=1, column=0)
        self.username = tk.StringVar()
        usernameEntry = tk.Entry(self, textvariable=self.username, font=controller.title_font).grid(row=1, column=1)  

        firstnameLabel = tk.Label(self, text="First Name", font=controller.title_font).grid(row=2, column=0)
        self.firstname = tk.StringVar()
        firstnameEntry = tk.Entry(self, textvariable=self.firstname, font=controller.title_font).grid(row=2, column=1)  

        lastnameLabel = tk.Label(self, text="Last Name", font=controller.title_font).grid(row=3, column=0)
        self.lastname = tk.StringVar()
        lastnameEntry = tk.Entry(self, textvariable=self.lastname, font=controller.title_font).grid(row=3, column=1)  

        birthdayLabel = tk.Label(self, text="birthday", font=controller.title_font).grid(row=4, column=0)
        self.birthday = tk.StringVar()
        birthdayEntry = tk.Entry(self, textvariable=self.birthday, font=controller.title_font).grid(row=4, column=1)  

        phonenumberLabel = tk.Label(self, text="phonenumber", font=controller.title_font).grid(row=5, column=0)
        self.phonenumber = tk.StringVar()
        phonenumberEntry = tk.Entry(self, textvariable=self.phonenumber, font=controller.title_font).grid(row=5, column=1)  
        
        emailLabel = tk.Label(self, text="email", font=controller.title_font).grid(row=6, column=0)
        self.email = tk.StringVar()
        emailEntry = tk.Entry(self, textvariable=self.email, font=controller.title_font).grid(row=6, column=1)  

        addressLabel = tk.Label(self, text="address", font=controller.title_font).grid(row=7, column=0)
        self.address = tk.StringVar()
        addressEntry = tk.Entry(self, textvariable=self.address, font=controller.title_font).grid(row=7, column=1)  

        passwordLabel = tk.Label(self, text="password", font=controller.title_font).grid(row=8, column=0)
        self.password = tk.StringVar()
        passwordEntry = tk.Entry(self, textvariable=self.password, font=controller.title_font).grid(row=8, column=1)  

        create_button = tk.Button(self, text="Create Account",  
                           command=self.create_account)
        create_button.grid(row=9, column=1)  
        
        back_button = tk.Button(self, text="Back",
                           command=lambda: controller.show_frame("LogIn"))
        back_button.grid(row=9, column=0)
    
    def create_account(self):
        try:
            user_id = add_user(self.username.get(), self.firstname.get(), self.lastname.get(), self.birthday.get(),self.phonenumber.get(), self.email.get(), self.address.get(), self.password.get(), 0)
            self.controller.userID.set(user_id)
            print(user_id)
            self.controller.show_frame("Dashboard")
        except Exception as e:
            raise_window('Retry please!', f'Error occured {e}')
        return 

class LogIn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.width = 580
        self.height = 200

        label = tk.Label(self, text="Welcome to simple bank!", font=controller.title_font).grid(row=0,column=0)

        # controller.geometry('400x150')  
        self.controller.title("Simple bank")
        # parent.title('Tkinter Login Form - pythonexamples.org')

        #username label and text entry box
        usernameLabel = tk.Label(self, text="Username", font=controller.title_font).grid(row=1, column=0)
        self.username = tk.StringVar()
        usernameEntry = tk.Entry(self, textvariable=self.username, font=controller.title_font).grid(row=1, column=1)  

        #password label and password entry box
        passwordLabel = tk.Label(self,text="Password", font=controller.title_font).grid(row=2, column=0)  
        self.password = tk.StringVar()
        passwordEntry = tk.Entry(self, textvariable=self.password, show='*', font=controller.title_font).grid(row=2, column=1)  

        #login button
        loginButton = tk.Button(self, text="Login", command=self.log_in, font=controller.title_font)
        loginButton.grid(row=5, column=0)  
        #login button
        createButton = tk.Button(self, text="Create New Account", command=self.create_account, font=controller.title_font)
        createButton.grid(row=6, column=0)  

    def log_in(self):
        self.controller.userID.set(validate_login(self.username.get(), self.password.get()))
        user_id = self.controller.userID.get()
        if user_id == -1:
            raise_window('Retry please!', 'Wrong username/password!')
            return
        self.controller.show_frame("Dashboard")
        return 
    
    def create_account(self):
        self.controller.show_frame("CreateAccount")
        return 
    
def raise_window(title: str, message: str):
    top= tk.Tk()
    top.title(title)
    label = tk.Label(top, text= message, font=('Mistral 18 bold'))
    label.pack()