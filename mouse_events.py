#
# author: a5892731
# date: 2021-08-20
# update:
#
# description: this is a program with simple GUI for Python
#
# source: Bro Code --> https://www.youtube.com/watch?v=TuLxsvK4svQ

from tkinter import *

def dosomething(event):
    print("You mouse coordinates = {}, {}".format(event.x, event.y))

window = Tk() # instantiate an instance of a window
window.geometry("420x420")

window.bind("<Button-1>", dosomething) # left mouse cluck
window.bind("<Button-3>", dosomething) # right mouse click



#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants