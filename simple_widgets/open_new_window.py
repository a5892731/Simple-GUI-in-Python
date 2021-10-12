#
# author: a5892731
# date: 2021-08-20
# update:
#
# description: this is a program with simple GUI for Python
#
# source: Bro Code --> https://www.youtube.com/watch?v=TuLxsvK4svQ

from tkinter import *

def create_window():
    new_window = Toplevel() # new window on top

window = Tk() # instantiate an instance of a window
window.geometry("420x420")


Button(window, text = "open new window", command = create_window).pack()


#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants