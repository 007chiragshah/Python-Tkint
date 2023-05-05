from tkinter import *

root = Tk()  # here we specify the logic of GUI

# GUI Logic


#Simple Window
#order is width x height
root.geometry("644x434")    #it desides the height and width of the GUI, we can min or max it any level

#order is width,height
root.minsize(200,100)
root.maxsize(800, 720)    #these will lock window with min and max size

lable = Label(text="Hello, I am Chirag")  #to create lable we need to use this
lable.pack()             #to show lable on GUI we need to use pack method

root.mainloop() # it is used to make GUI interactive