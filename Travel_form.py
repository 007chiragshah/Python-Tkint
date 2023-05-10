from tkinter import *

root = Tk()  # here we specify the logic of GUI

def getvals():
    print("Welcome to Shah travels")
    with open(f"Customer List","a") as f:   #store the data in sheet
        f.write(f"Name ={namevalue.get()},Phone={phonevalue.get()},Gender={gendervalue.get()},Emergency_Contace={emergencyvalue.get()},Payement_Mode={paymentmodevalue.get()},Food={foodservicevalue.get()}\n")
# GUI Logic
root.geometry("500x400")

#heading
Title = Label(root, text="Shah Travels Agency", font='comicsansms 20 bold')
Title.grid(column=1,pady=8)

#Labels for the form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
paymentmode = Label(root, text="Payment Mode")


#packing labels with grid method
name.grid(row=1)    #here we can mention the row and column, which is by default 0
phone.grid(row=2)    #here we can mention the row and column, which is by default 0
gender.grid(row=3)    #here we can mention the row and column, which is by default 0
emergency.grid(row=4)    #here we can mention the row and column, which is by default 0
paymentmode.grid(row=5)    #here we can mention the row and column, which is by default 0


#Tkinter variables
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

#Created the Entries for form to store the value
nameentry =  Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)


#packing the entries
nameentry.grid(row=1, column=1)
phoneentry.grid(row=2, column=1)
genderentry.grid(row=3,column=1)
emergencyentry.grid(row=4,column=1)
paymentmodeentry.grid(row=5,column=1)

#check box

foodservice = Checkbutton(text="Prebook your meal", variable=foodservicevalue)
foodservice.grid(row=7, column=1)

#Submit button
submit = Button(text="Submit Your Form", command=getvals).grid()

root.mainloop() # it is used to make GUI interactive

