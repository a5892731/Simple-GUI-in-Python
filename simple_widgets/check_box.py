#
# author: a5892731
# date: 2021-08-19
# update:
#
# description: this is a program with simple GUI for Python
#
# source: Bro Code --> https://www.youtube.com/watch?v=TuLxsvK4svQ

from tkinter import *


def display():
    if (x.get()==1):
        print("its on")
    else:
        print("its off")


window = Tk() # instantiate an instance of a window
window.geometry("420x420")

x = IntVar()


check_box = Checkbutton(window,
                        text = "check if on ",
                        variable = x,
                        onvalue = 1,
                        offvalue = 0,
                        command = display)


check_box.pack()
#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants