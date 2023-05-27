import time
from tkinter import *
from tkinter import ttk
import time
root = Tk()  # here we specify the logic of GUI
root.geometry("734x600")

def pg():
    for i in range(3):
        time.sleep(1)
        progress["value"] += 20

progress = ttk.Progressbar(root, orient = HORIZONTAL,length = 1000, mode = 'determinate',maximum=100)
progress.pack()


Button(root, text="Submit", bg="grey", fg='black', command=pg).pack()

root.mainloop()

