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
window.geometry("420x620")
window.title("GUI window title")
icon = PhotoImage(file ="icon.png")
window.iconphoto(True, icon) # icon in upper, left corner of program window
window.config(background = "#cfd1cf") # "hex color picker" surch in google
#-------------------------------------------------------------
lable_text= "hello world"
label = Label(window, text= lable_text, font= ('Arial', 40, 'bold'),
              bg = "#cfd1cf", fg = 'green')
#-----------------------------
lable_text2= "hello world2"
label2 = Label(window, text= lable_text2, font= ('Arial', 40, 'bold'),
              bg = "#cfd1cf", fg = 'green',
              relief=RAISED,
              bd = 5,)
#-----------------------------
lable_text3= "hello world3"
label3 = Label(window, text= lable_text3, font= ('Arial', 40, 'bold'),
              bg = "#cfd1cf", fg = 'green',
              relief=RAISED,
              bd = 5,
              padx = 20, pady = 20)
#-----------------------------
photo = PhotoImage(file='icon.png')
label4 = Label(window, font= ('Arial', 40, 'bold'),
              bg = "#cfd1cf", fg = 'green',
              relief=RAISED,
              bd = 5,
              padx = 20, pady = 20,
              image = photo)
#-----------------------------
#photo = PhotoImage(file='icon.png')
label5 = Label(window, text = "photo", font= ('Arial', 40, 'bold'),
              bg = "#cfd1cf", fg = 'green',
              relief=RAISED,
              bd = 5,
              padx = 20, pady = 20,
              image = photo,
              compound = "bottom")
#-----------------------------

label.pack() # place in center
label2.pack() # place in center
label3.pack() # place in center
label4.place(x = 10, y = 270) # place in direction
label5.place(x = 200, y = 280) # place in direction
#-------------------------------------------------------------


#-------------------------------------------------------------
window.mainloop() # place window on computer screen. listen for evants