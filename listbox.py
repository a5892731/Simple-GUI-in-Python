#
# author: a5892731
# date: 2021-08-19
# update:
#
# description: this is a program with simple GUI for Python
#
# source: Bro Code --> https://www.youtube.com/watch?v=TuLxsvK4svQ

from tkinter import *

def lb_command():
    x = listbox.get(listbox.curselection())
    print(x)

window = Tk() # instantiate an instance of a window
window.geometry("420x420")

listbox = Listbox(window, font = ("Times New Roman", 20))
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "hotdog")
listbox.insert(4, "hamburger")
listbox.insert(5, "soup")
listbox.insert(6, "crapy chicken")
listbox.config(height = listbox.size())

submit_button = Button(window,  text = "submit", font = ("Times New Roman", 20),
                       command = lb_command)
submit_button.pack()

#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants