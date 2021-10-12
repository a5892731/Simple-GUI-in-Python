#
# author: a5892731
# date: 2021-08-20
# update:
#
# description: this is a program with simple GUI for Python
#
# source: Bro Code --> https://www.youtube.com/watch?v=TuLxsvK4svQ

from tkinter import *
from tkinter import filedialog

def openfile():
     filepath = filedialog.askopenfilename()
     print(filepath)
     file = open(filepath, "r")
     print(file.read())
     file.close()

def savefile():
    file = filedialog.asksaveasfile()
    filetext = str(text.get(1.0, END))

    file.write(filetext)
    file.close()


window = Tk() # instantiate an instance of a window
window.geometry("420x420")

button = Button(text = "open file", comman = openfile)
button.pack()

button2 = Button(text = "save file", comman = savefile)
button2.pack()

text = Text(window)
text.pack()

#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants