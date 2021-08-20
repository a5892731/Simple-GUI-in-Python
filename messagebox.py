#
# author: a5892731
# date: 2021-08-20
# update:
#
# description: this is a program with simple GUI for Python
#
# source: Bro Code --> https://www.youtube.com/watch?v=TuLxsvK4svQ

from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title = "this is a message box",
                        message = " F* YOU!")

def click2():
    messagebox.showwarning(title = "this is a message box",
                        message = " F* YOU!")

def click3():
    messagebox.showerror(title = "this is a message box",
                        message = " F* YOU!")

def click4():
    if messagebox.askokcancel(title = "que???",
                        message = " ok or not ok?",
                           ):
        print("OK")
    else:
        print("CANCEL")



window = Tk() # instantiate an instance of a window
window.geometry("220x220")


button = Button(window, command = click, text = "click me")
button.pack()

button2 = Button(window, command = click2, text = "click me")
button2.pack()

button3 = Button(window, command = click3, text = "click me")
button3.pack()

button4 = Button(window, command = click4, text = "click me")
button4.pack()

#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants