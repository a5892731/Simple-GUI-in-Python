#
# author: a5892731
# date: 2021-08-20
# update:
#
# description: this is a program with simple GUI for Python
#
# source: Bro Code --> https://www.youtube.com/watch?v=TuLxsvK4svQ

from tkinter import *
from tkinter.ttk import *
import time


def start():
    tasks = 10
    x = 0
    while (x<tasks):
        time.sleep(1)
        bar['value']+=10
        x+=1
        percent.set((str(x/tasks *100) + " %"))
        window.update_idletasks()


window = Tk() # instantiate an instance of a window

percent = StringVar()

bar = Progressbar(window, orient = HORIZONTAL, length = 300)
bar.pack(pady = 10)

percentLabel = Label(window, textvariable = percent).pack()

button = Button(window, text = "progress", command = start)
button.pack()




#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants