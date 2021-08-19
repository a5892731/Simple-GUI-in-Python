#
# author: a5892731
# date: 2021-08-19
# update:
#
# description: this is a program with simple GUI for Python
#
# source: Bro Code --> https://www.youtube.com/watch?v=TuLxsvK4svQ

from tkinter import *

count = 0
def click():
    global count
    count += 1
    print(count)



window = Tk() # instantiate an instance of a window
window.geometry("420x420")

button = Button(window, text = "click me",
                font= ('Arial', 40, 'bold'),
                relief=RAISED,
                bd=5,
                command = click)

button_text = "click me 2"
button2 = Button(window, text = button_text,
                font= ('Arial', 40, 'bold'),
                relief=RAISED,
                bd=5,
                command = click,
                fg = "green",
                bg = "grey",
                activeforeground = "red",
                activebackground= "black",)

button.pack()
button2.pack()



#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants