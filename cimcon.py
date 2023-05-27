from tkinter import *
from tkinter import ttk
import urllib.request
import paramiko
import tkinter.messagebox as tmsg
import time


root = Tk() # here we specify the logic of GUI
client = paramiko.client.SSHClient()  #for SSH Login


#Private Key path and Password
gcp_key = paramiko.RSAKey.from_private_key_file("/home/chirag/Documents/GCP.pem", password='cimcon@123')
maruti_key = paramiko.RSAKey.from_private_key_file("/home/chirag/Documents/cimcon.pem")

# GCP Credential
GCPhost = "35.226.41.240"
GCPusername = "cimcon_digital904"
GCPpassword = "cimcon@123"

# QA Credential
QAhost = "203.88.135.128"
QAusername = "thingsboard"
QApassword = "cimcon@123"


# Maruti Credential
MarutiHost = "3.109.7.153"
MarutiUsername = "ubuntu"


#Define Tkinter variable for Server Button
server = StringVar()
server.set("Radio")

#define Tkinter variable for Service Button
service = StringVar()
service.set("Radio")

# GUI Logic
root.geometry("700x500")
root.configure(background="white")


#Different Functions

#connection check
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen("https://www.google.com")
        return True
    except:
        return False


def checkserver():
    if server.get() == "GCP":
        connetGCP()
    elif server.get() == "Maruti":
         connectMaruti()
    else:
         connetQA()

def checkservice():
    if service.get() == "FFT":
        FFT()
    elif service.get() == "ADR":
        ADR()
    else:
        publish()

def preview():
    if server.get() == 'Radio':
        tmsg.showinfo("Error", "kindly Select the server")
    elif service.get() == 'Radio':
        tmsg.showinfo("Error", "kindly Select the service")
    else:
        Priview = tmsg.askquestion("Preview", f"{server.get()} server selected. \n{service.get()} service selected \nDo you want to proceed ?")
        if Priview == "yes":
            checkserver()
            checkservice()
        else:
            tmsg.showinfo("Do Not Proceed", "We are not proceeding further")

def pgbar():
    if server.get() == 'Radio':
        pass
    elif service.get() == 'Radio':
        pass
    else:
        progress["value"] = 33.3
        time.sleep(1)
        progress["value"] += 33.3

#Connect To GCP
def connetGCP():
    try:
        client.set_missing_host_key_policy((paramiko.AutoAddPolicy()))
        client.connect(hostname=GCPhost, username=GCPusername, password=GCPpassword, pkey=gcp_key)
        log.insert(ANCHOR, "GCP server connected successfully")
    except Exception as e:
        log.insert(ANCHOR, f"We have got the error {e}")

#Connect Maruti
def connectMaruti():
    try:
        client.set_missing_host_key_policy((paramiko.AutoAddPolicy()))
        client.connect(hostname=MarutiHost, username=MarutiUsername, pkey=maruti_key)
        log.insert(ANCHOR, "Maruti server connected successfully")
    except Exception as e:
        log.insert(ANCHOR, f"We have got the error {e}")

#Connect to QA
def connetQA():
    try:
        client.set_missing_host_key_policy((paramiko.AutoAddPolicy()))
        client.connect(hostname=QAhost, username=QAusername, password=QApassword)
        log.insert(ANCHOR, "QA Server connected successfully")
        time.sleep(2)
        pgbar()
    except Exception as e:
        log.insert(ANCHOR, f"We have got the error {e}")


#Functions for Services
def FFT():
    pass
def ADR():
    pass

def publish():
    log.insert(ANCHOR, f"{service.get()} service selected")
    time.sleep(2)
    _stdin, _stdout, _stderr = client.exec_command("df -Th")
    error=_stderr.readlines()
    for i in _stdout.readlines():
        log.insert(ANCHOR, f"{i}")
        progress["value"] += 33.4
    if error:
        log.insert(ANCHOR, f"Oops, there is an error: {error}")

def serverclose():
    client.close()


if connect():
    #Checking Internet
    print("Internet is available.")
    root.title("CIMCON Digital")

    #Application Label
    f1 = Frame(root, bg="#00A0DC", borderwidth=5,)
    f1.pack(fill="both")
    Label(f1, text="InstaAIWeb", font='Helvetica 20 bold', fg="white", bg="#00A0DC").pack()

    #For Server Selection
    f2 = Frame(root, bg='white', borderwidth=8, width=1000)
    f2.pack(fill="x", anchor='w')
    Label(f2, text="Select the Server: ", font='cosmacsansms 13', bg="white").pack(side=LEFT, padx=13, pady=10, anchor="nw")
    Radiobutton(f2, text='GCP', variable=server, value="GCP", bg="#f4f4f4", padx=5).pack(side=LEFT, padx=5, pady=11, anchor='nw')
    Radiobutton(f2, text='Maruti', variable=server, value="Maruti", bg="#f4f4f4",padx=5).pack(side=LEFT, padx=5, pady=11, anchor='nw')
    Radiobutton(f2, text='QA', variable=server, value="QA", bg="#f4f4f4",padx=5).pack(side=LEFT, padx=5, pady=11, anchor='nw')

    f5 = Frame(root, bg='grey', borderwidth=8, width=1000)
    f5.pack(fill="x", anchor='w')

    #For Service Selection
    f3 = Frame(root, bg='white', borderwidth=8, width=1000)
    f3.pack(fill="x", anchor="w")
    Label(f3, text="Select the Service: ", font='cosmacsansms 13', bg="white").pack(side=LEFT,padx=10, pady=10, anchor="nw")
    Radiobutton(f3, text='FFT', variable=service, value="FFT", bg="#f4f4f4", padx=5).pack(side=LEFT, padx=5, pady=11, anchor='nw')
    Radiobutton(f3, text='ADR', variable=service, value="ADR", bg="#f4f4f4", padx=5).pack(side=LEFT, padx=5, pady=11, anchor='nw')
    Radiobutton(f3, text='Thingsboard build', variable=service, value="publish",bg="#f4f4f4", padx=5).pack(side=LEFT, padx=5, pady=11, anchor='nw')

    f4 = Frame(root, bg='grey', borderwidth=8, width=1000)
    f4.pack(fill="both", anchor="n", side=BOTTOM)
    Label(f4, text="Progress Status").pack(side=TOP, pady=5, anchor="w")

    f6 = Frame(root, bg='white', borderwidth=8, width=1000)
    f6.pack(fill="x", anchor='w',padx=200,pady=20)
    Button(f6, text="Submit", command= lambda:[pgbar(),preview()]).pack(side=LEFT, anchor="nw", padx=50)
    Button(f6, text="Close",command=quit).pack(side=LEFT, anchor="nw")

    scrollbar = Scrollbar(f4)
    scrollbar.pack(side=RIGHT, fill="y")

    progress = ttk.Progressbar(root, orient = HORIZONTAL,length = 1000, mode = 'determinate',maximum=100)
    progress.pack()

    log = Listbox(f4,yscrollcommand=scrollbar.set)
    scrollbar.config(command=log.yview)
    log.pack(fill="both", side=LEFT, expand=True)

    log.insert(END, "Logs are here")
    log.insert(END, "Connection Established")
    root.mainloop()
else:
    print("Internet is not available.")
    lab = Label(text="Internet is not there")
    lab.pack()
    root.mainloop()