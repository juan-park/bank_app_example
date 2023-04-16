import tkinter as tk
from tkinter import ttk

count = 0
def clicked(): # without event because I use `command=` instead of `bind`
    global count
    count = count + 1
    label1.configure(text=f'Button was clicked {count} times!!!')

windows = tk.Tk()
windows.title("My Application")

label = tk.Label(windows, text="Hello World")
label.grid(column=0, row=0)

label1 = tk.Label(windows)
label1.grid(column=0, row=1)

custom_button = ttk.Button(windows, text="Click on me", command=clicked)
custom_button.grid(column=1, row=0)

windows.mainloop()