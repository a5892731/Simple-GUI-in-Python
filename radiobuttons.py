#
# author: a5892731
# date: 2021-08-19
# update:
#
# description: this is a program with simple GUI for Python
#
# source: Bro Code --> https://www.youtube.com/watch?v=TuLxsvK4svQ

from tkinter import *

def radio_check():
    if x.get() == 0:
        print("pizza")
    if x.get() == 1:
        print("hot dog")
    if x.get() == 2:
        print("hamburger")

food = ["pizza", "hot dog", "hamburger"]

window = Tk() # instantiate an instance of a window
window.geometry("420x420")

x = IntVar()
for index in range(len(food)):
    radiobutton = Radiobutton(window, text=food[index],
                              variable = x, value = index,
                              command = radio_check)
    radiobutton.pack()



#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants