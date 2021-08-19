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
    print("the temperature is {} degrees C".format(scale.get()))

window = Tk() # instantiate an instance of a window

scale = Scale(window, from_ =100, to = 0, font = ("Arial", 20),
              length = 600,
              orient = VERTICAL,
              tickinterval = 10,
              showvalue = 0, # hide current value
              resolution = 5,
              #troughcolor = "#69EAFF",
              #fg = "#FF1C00",
              #bg = "#111111"
              )
scale.set((scale["from"]-scale["to"]/2)+scale["to"])
scale.pack()

button = Button(window, text = "submit", command = submit)

button.pack()


#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants