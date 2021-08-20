#
# author: a5892731
# date: 2021-08-20
# update:
#
# description: this is a program with simple GUI for Python
#
# source: Bro Code --> https://www.youtube.com/watch?v=TuLxsvK4svQ

from tkinter import *

def press_key(event):
    print(event.keysym)
    label.config(text=event.keysym)

window = Tk() # instantiate an instance of a window


window.bind("<Key>", press_key)

label = Label(window)
label.pack()



#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants