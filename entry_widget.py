#
# author: a5892731
# date: 2021-08-19
# update:
#
# description: this is a program with simple GUI for Python
#
# source: Bro Code --> https://www.youtube.com/watch?v=TuLxsvK4svQ

from tkinter import *

def submit():
    username = entry.get()
    print("Hello {}".format(username))

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk() # instantiate an instance of a window
window.geometry("520x120")

entry = Entry(window, font=("Arial", 20))
entry.pack(side = LEFT)

submit_button = Button(window, text = "submit", command = submit)
submit_button.pack(side = RIGHT)

delete_button = Button(window, text = "delete", command = delete)
delete_button.pack(side = RIGHT)

backspace_button = Button(window, text = "backspace", command = backspace)
backspace_button.pack(side = RIGHT)


#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants