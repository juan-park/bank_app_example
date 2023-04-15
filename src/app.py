import tkinter as tk  
from tkinter import font as tkfont
from .app_windows import LogIn, Dashboard, AccountBalance, CreateAccount


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # App level variables
        self.userID = tk.IntVar()

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        # Add new windows here.
        for F in (LogIn, Dashboard, AccountBalance, CreateAccount):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LogIn")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        self.geometry(f'{frame.width}x{frame.height}')
        if '_update_on_load' in dir(frame):
            frame._update_on_load()
        frame.tkraise() # brings a frame to the top.