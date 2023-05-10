from tkinter import *

root = Tk()  # here we specify the logic of GUI
root.geometry("734x600")

def myfunc():
    print("Hello from Manu")
'''
# Manu withoud dropdown
mymenu = Menu(root)      #it will add the menubar in the root window
mymenu.add_command(label="file",command=myfunc) #this will  be different menus in menubar
mymenu.add_command(label="Exit",command=quit)
'''

# Manu with dropdown
filemanu = Menu(root)    #it will add the menubar in the root window
m1 = Menu(filemanu, tearoff=0)    #It will create menu menubar
m1.add_command(label="New File", command=myfunc)     #different dropdown in first menu
m1.add_command(label="Open", command=myfunc)
m1.add_separator()
m1.add_command(label="Save", command=myfunc)
m1.add_command(label="Save as", command=myfunc)

root.config(menu=filemanu)           #Configured the in root window
filemanu.add_cascade(label="File", menu=m1) #Give the name of firstmanu as File and add the dropdown in that using cascade

root.mainloop()