from tkinter import *

root = Tk()  # here we specify the logic of GUI

# GUI Logic

root.geometry("500x400")

#here we used the frame keyword to create the frame
f1 = Frame(root, bg="pink", borderwidth=5)  #in frame we mentioned root as we want to frame the roor
f1.pack(side=LEFT,fill="y")    #here we used the side method of pack

f2 = Frame(root, bg="pink", borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l = Label(f1, text="Hello")  #here we mention f1 as we want to add label in that frame
l.pack(pady=180,fill="y")

l = Label(f2, text="Welcome")  #here we mention f1 as we want to add label in that frame
l.pack(padx=180,fill="x")

root.mainloop() # it is used to make GUI interactive

