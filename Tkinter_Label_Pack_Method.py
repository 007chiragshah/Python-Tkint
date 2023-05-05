from tkinter import *

root = Tk()  # here we specify the logic of GUI

# GUI Logic

root.geometry("800x600")

# Important Label Option

# text      = adding text
# bd        = background
# fg        = foreground
# fonts     = set the fonts
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"
# padx      = x padding
# pady      = y padding
# relief    = border styling - SUNKEN, RAISED, GROOVE, RIDGE

# Example

title_label = Label(text = '''Software Engineer with 5 years of hands-on experience developing and maintaining
websites and web applications. Strong knowledge of javascript and its frameworks such as React and Nodejs with
cloud technology like AWS and GCP and a willingness to learn new tools and technologies. Able to work independently
or within a team environment to complete tasks. Fast learner who likes working with new technologies.''', bg='Black',
fg='White', font="comicsansms 19 bold", padx=20, pady= 20, borderwidth=3, relief=RAISED)


#important Pack method

#anchor = nw (northwest) -- used to place widget
#side   = Top, Bottom
#fill   = X or Y
#padx   = X padding
#pady   = Y padding

title_label.pack(side=TOP, anchor='se',fill=X,padx=12,pady=10)


root.mainloop() # it is used to make GUI interactive