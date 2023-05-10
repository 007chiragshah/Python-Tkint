from tkinter import *

def event(event):
    print("You clicked here")
root = Tk()  # here we specify the logic of GUI
root.title("Events")
root.geometry("644x334")

widget = Button(root, text='Click me please')
widget.pack()

#we need to bind the button to create an event on that button
widget.bind('<Button-1>',event)  #event on single click
widget.bind('<Double-Button-1>',quit)  #event on double click

root.mainloop() # it is used to make GUI interactive

