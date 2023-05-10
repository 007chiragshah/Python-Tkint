from tkinter import *

root = Tk()  # here we specify the logic of GUI

canvas_width = 800
canvas_height = 400

root.geometry = (f"{canvas_height}x{canvas_width}")
root.title("Chirag ka GUI")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

can_widget.create_line(0,0,800,400, fill="red")
can_widget.create_line(0,400,800,0, fill="red")

can_widget.create_rectangle(3,5,799,399,fill='pink')

can_widget.create_line(0,0,800,400, fill="red")
can_widget.create_line(0,400,800,0, fill="red")

can_widget.create_text(200,200, text="Welcome")
root.mainloop() # it is used to make GUI interactive

