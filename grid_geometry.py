#
# author: a5892731
# date: 2021-08-20
# update:
#
# description: this is a program with simple GUI for Python
#
# source: Bro Code --> https://www.youtube.com/watch?v=TuLxsvK4svQ

from tkinter import *



window = Tk() # instantiate an instance of a window
window.geometry("420x420")

titleLabel = Label(window, text = "TITLE",
                   font = ("Arial, 25")).grid(row = 0, column=0,
                                              columnspan = 4)
firstNameLabel = Label(window, text = "A").grid(row = 1, column=1)
firstNameLabel = Label(window, text = "B").grid(row = 1, column=2)
firstNameLabel = Label(window, text = "C").grid(row = 1, column=3)
firstNameLabel = Label(window, text = "1").grid(row = 2, column=0)
firstNameLabel = Label(window, text = "2").grid(row = 3, column=0)
firstNameLabel = Label(window, text = "3").grid(row = 4, column=0)

A1 = Entry(window).grid(row = 2, column=1)
A2 = Entry(window).grid(row = 3, column=1)
A3 = Entry(window).grid(row = 4, column=1)

B1 = Entry(window).grid(row = 2, column=2)
B2 = Entry(window).grid(row = 3, column=2)
B3 = Entry(window).grid(row = 4, column=2)

C1 = Entry(window).grid(row = 2, column=3)
C2 = Entry(window).grid(row = 3, column=3)
C3 = Entry(window).grid(row = 4, column=3)



#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants