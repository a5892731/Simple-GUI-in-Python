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

frame = Frame(window)
frame.pack()

Button(frame, text= "W", font=("Consolas", 25), width=3).pack(side = TOP)
Button(frame, text= "A", font=("Consolas", 25), width=3).pack(side = LEFT)
Button(frame, text= "S", font=("Consolas", 25), width=3).pack(side = LEFT)
Button(frame, text= "D", font=("Consolas", 25), width=3).pack(side = LEFT)




#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants