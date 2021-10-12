#
# author: a5892731
# date: 2021-10-12
# update:
#
# Source:
# http://matrix.umcs.lublin.pl/~akrajka/PYTHON-I/Wyklady/Python_cw01.pdf
# Zad. 4.2. Pola tekstowe


from tkinter import *
from tkinter import ttk

import tkinter as tk
from PIL import ImageTk
from PIL import Image

class SimpleApp(object):
    def __init__(self, **kwargs):
        self.window_width = 500
        self.window_height = 500
        self.window = Tk()

        self.update = self.draw().__next__
        self.window.after(100, self.update)

    def draw(self):
        self.draw_window_atributes()
        self.draw_on_grid()
        self.window.mainloop()

    def draw_window_atributes(self):
        self.window.title("Testowanie pól tekstowych")
        #icon = PhotoImage(file = "files/icon.png")
        self.window.geometry("{}x{}".format(self.window_width, self.window_height))
        self.window.resizable(width=False, height=False)
        #self.window.iconphoto(True, icon) # icon in upper, left corner of program window
        self.window.config(background = "#cfd1cf") # "hex color picker" search in google



    def draw_on_grid(self):
        self.window.columnconfigure(0, minsize =10)
        self.window.rowconfigure(0, minsize =10)

        entry0 = self.draw_entry_widget().grid(column=0, row=0)  #columnspan=3, rowspan=2
        entry1 = self.draw_entry_widget().grid(column=1, row=0)
        entry2 = self.draw_entry_widget().grid(column=0, row=1)
        entry3 = self.draw_entry_widget().grid(column=1, row=1)






    def draw_entry_widget(self, width=10):
        return Entry(self.window, font=("Arial", 20),  width=width)


#-----------------------------------------------------------------------------------------------------------------------

app = SimpleApp()
