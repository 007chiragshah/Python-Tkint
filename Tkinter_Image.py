from tkinter import *
from PIL import Image, ImageTk

root = Tk()  # here we specify the logic of GUI

# GUI Logic


#Simple Window
#order is width x height
root.geometry("644x434")    #it desides the height and width of the GUI, we can min or max it any level

#order is width,height
root.minsize(200,100)
root.maxsize(800, 720)

image = Image.open("1.png")
photo = ImageTk.PhotoImage(image)

lab = Label(image=photo)     #to create lable we need to use this
lab.pack()                   #to show lable on GUI we need to use pack method


root.mainloop()