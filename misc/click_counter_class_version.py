import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def clicked(self):
        self.count.set(self.count.get()+1)
        cnt = self.count.get()
        self.label1['text'] =f'Button was clicked {cnt} times!!!'

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("My Application")
        self.count = tk.IntVar(self, 0)
        
        self.label = tk.Label(self, text="Hello World")
        self.label.grid(column=0, row=0)

        self.label1 = tk.Label(self)
        self.label1.grid(column=0, row=1)

        self.custom_button = ttk.Button(self, text="Click on me", command=self.clicked)
        self.custom_button.grid(column=1, row=0)

if __name__ == '__main__':
    app = App()
    app.mainloop()