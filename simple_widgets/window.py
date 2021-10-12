#
# author: a5892731
# date: 2021-08-19
# update:
#
# description: this is a program with simple GUI for Python
#
# source: Bro Code --> https://www.youtube.com/watch?v=TuLxsvK4svQ

from tkinter import *

window = Tk() # instantiate an instance of a window
window.geometry("420x420")
window.title("GUI window title")
icon = PhotoImage(file ="icon.png")
window.iconphoto(True, icon) # icon in upper, left corner of program window
window.config(background = "#cfd1cf") # "hex color picker" surch in google



#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants