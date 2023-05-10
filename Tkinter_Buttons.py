from tkinter import *
from paramiko import SSHClient, AutoAddPolicy
import time
import threading
import logging
try:
    import tkinter as tk # Python 3.x
    import tkinter.scrolledtext as ScrolledText
except ImportError:
    import Tkinter as tk # Python 2.x
    import ScrolledText

class TextHandler(logging.Handler):
    # This class allows you to log to a Tkinter Text or ScrolledText widget
    # Adapted from Moshe Kaplan: https://gist.github.com/moshekaplan/c425f861de7bbf28ef06

    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)

        def append():
            self.text.configure(state='normal')
            self.text.insert(tk.END, msg + '\n')
            self.text.configure(state='disabled')
            # Autoscroll to the bottom
            self.text.yview(tk.END)

        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)

root = Tk()  # here we specify the logic of GUI
client = SSHClient()
# GUI Logic

root.geometry("500x400")

def hello():
    print("Hello Buttons")

def name():
    print("My name is chirag")

#here we used the frame keyword to create the frame
f1 = Frame(root, bg="pink", borderwidth=5)  #in frame we mentioned root as we want to frame the roor
f1.pack(anchor="nw", side=RIGHT)    #here we used the side method of pack

f2 = Frame(root, bg="pink", borderwidth=5)  #in frame we mentioned root as we want to frame the roor
f2.pack(anchor="nw", side=LEFT)

L2 = Label(f2, text="Please select the server", fg="red")
L2.pack(pady=15)

b1 = Button(f1, text="GCP", fg="green", command=hello)
b1.pack(side=LEFT, padx=20, pady=10)

b2 = Button(f1, text="Maruti", fg="blue", command=name)
b2.pack(side=LEFT, padx=20)

b3 = Button(f1, text="QA", fg="blue")
b3.pack(side=LEFT, padx=20)

root.mainloop() # it is used to make GUI interactive