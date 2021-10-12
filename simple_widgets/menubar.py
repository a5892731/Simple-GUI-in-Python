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

def exit():
    quit()

def help():
    print("need help? LOL")

window = Tk() # instantiate an instance of a window
window.geometry("420x420")

text = Text(window)
text.pack()



menubar = Menu(window)
window.config(menu = menubar)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label= "File", menu = filemenu)
filemenu.add_command(label = "open", command = openfile)
filemenu.add_command(label = "save", command = savefile)
filemenu.add_command(label = "exit", command = exit)

helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label= "Help", menu = helpmenu)
helpmenu.add_command(label = "help", command = help)


#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants