#
# author: a5892731
# date: 2021-10-12
# update:
#
# Source:
# http://matrix.umcs.lublin.pl/~akrajka/PYTHON-I/Wyklady/Python_cw01.pdf
# Zad. 4.1. Etykiety i przyciski


from tkinter import *

import tkinter as tk
from PIL import ImageTk
from PIL import Image

class SimpleApp(object):
    def __init__(self, **kwargs):
        self.window_width = 300
        self.window_height = 175
        self.window = Tk()

        self.update = self.draw().__next__
        self.window.after(100, self.update)

    def draw(self):
        self.draw_window_atributes()
        self.draw_labels()
        self.draw_buttons()
        self.window.mainloop()

    def draw_window_atributes(self):
        self.window.title("Etykiety i przyciski")
        #icon = PhotoImage(file = "files/icon.png")
        self.window.geometry("{}x{}".format(self.window_width, self.window_height))
        self.window.resizable(width=False, height=False)
        #self.window.iconphoto(True, icon) # icon in upper, left corner of program window
        self.window.config(background = "#cfd1cf") # "hex color picker" search in google

    def draw_buttons(self):
        def hej():
            print("Hej")

        def quit():
            sys.exit(0)

        def button_attributes(text, func, foreground_color = "black"):
            return Button(self.window,
                         text=text,
                         font=('Arial', 14),
                         image=self.pixel_virtual, # with this we can resize button in pixel scale
                         compound=CENTER,
                         relief=RAISED,
                         bd=1,
                         width= button_width,
                         height = button_height,
                         fg = foreground_color,
                         command=func)

        button_width = 180
        button_height = 50
        self.pixel_virtual = PhotoImage(width=1, height=1)  # must be SELF, otherwise button will not work
        x = (self.window_width - button_width) / 2
        y = 60
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        button0 = button_attributes("Hej", hej)
        button0.place(x=x,  y=y + (button_height + 8) * 0)

        button1 = button_attributes("QUIT", quit, "red")
        button1.place(x=x, y=y + (button_height + 8) * 1)

    def draw_labels(self):
        label_width = 180
        label_height = 25
        self.image = PhotoImage(file="image.png")
        x = (self.window_width - label_width) / 2
        y = 10

        lable_text0 = "Etykieta tekstowa"
        label0 = Label(self.window, text=lable_text0, font=('Arial', 14),
                      bg="#cfd1cf", fg='black')
        label0.pack()

        lable_text1 = "Etykieta tekstowa z ikoną "
        label1 = Label(self.window,  text=lable_text1, font=('Arial', 14),
                      bg="#cfd1cf", fg='black', image = self.image, compound = RIGHT)

        label1.pack()


#-----------------------------------------------------------------------------------------------------------------------

app = SimpleApp()
