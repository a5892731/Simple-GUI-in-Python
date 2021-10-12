#
# author: a5892731
# date: 2021-08-20
# update:
#
# description: this is a program with simple GUI for Python
#
# source: Bro Code --> https://www.youtube.com/watch?v=TuLxsvK4svQ

from tkinter import *

def click():
    text = testarea.get("1.0", END)
    print(text)

window = Tk() # instantiate an instance of a window
window.geometry("420x420")

testarea = Text(window)
testarea.pack()
button = Button(text = 'click', command = click)
button.pack()

#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants