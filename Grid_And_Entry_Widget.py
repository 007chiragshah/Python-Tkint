from tkinter import *

root = Tk()  # here we specify the logic of GUI

# GUI Logic
root.geometry("500x400")

def getvals():
    print(f"The value of username is {uservalue.get()}") #to get the value of username
    print(f"The value of username is {passvalue.get()}") #to get the value of password

user = Label(root, text="username")
password = Label(root, text="password")

#this is also a method of packing
user.grid()    #here we can mention the row and column, which is by default 0
password.grid(row=1)

#4 variable classes
#BooleanVar, IntVar, StringVar, DoubleVar

uservalue = StringVar()  #to enter the string val
passvalue = StringVar()  #to enter the string vale

userentry =  Entry(root, textvariable=uservalue)  #making entry value for username
passentry = Entry(root, textvariable=passvalue)   #making entry value for password

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

submit = Button(text="Submit", command=getvals).grid()
root.mainloop() # it is used to make GUI interactive

