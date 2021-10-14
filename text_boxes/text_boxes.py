#
# author: a5892731
# date: 2021-10-14
# update:
#
# Source:
# http://matrix.umcs.lublin.pl/~akrajka/PYTHON-I/Wyklady/Python_cw01.pdf
# Zad. 4.2. Pola tekstowe


from tkinter import *

import tkinter as tk
from PIL import ImageTk
from PIL import Image

class SimpleApp(object):
    def __init__(self, **kwargs):
        self.window_width = 500
        self.window_height = 120
        self.window = Tk()

        self.update = self.draw().__next__
        self.window.after(100, self.update)

    def draw(self):
        self.draw_window_atributes()
        self.grid_settings()
        self.draw_on_grid()
        self.window.mainloop()

    def draw_window_atributes(self):
        self.window.title("Testowanie pól tekstowych")
        #icon = PhotoImage(file = "files/icon.png")
        self.window.geometry("{}x{}".format(self.window_width, self.window_height))
        self.window.resizable(width=False, height=False)
        #self.window.iconphoto(True, icon) # icon in upper, left corner of program window
        self.window.config(background = "#cfd1cf") # "hex color picker" search in google

    def grid_settings(self):
        self.window.columnconfigure(0, minsize =245)
        self.window.columnconfigure(1, minsize=10)
        self.window.columnconfigure(2, minsize=245)
        self.window.rowconfigure(0, minsize =5)
        self.window.rowconfigure(1, minsize =30)
        self.window.rowconfigure(2, minsize =30)

    def draw_on_grid(self):
        entry0 = self.draw_entry_widget().grid(column=0, row=1, sticky=E)
        entry1 = self.draw_entry_widget("Wpisz tekst tutaj").grid(column=2, row=1, sticky=W)
        entry2 = self.draw_entry_widget("Pole nieedytowalne", "", DISABLED).grid(column=0, row=2, sticky=E)
        entry3 = self.draw_entry_widget("", "*").grid(column=2, row=2, sticky=W)
        # another atributes #columnspan=3, rowspan=2

    def draw_entry_widget(self, text="", show="", state=NORMAL, width=18):
        textEntry = StringVar()
        textEntry.set(text)
        return Entry(self.window, font=("Arial", 14), textvariable=textEntry, show=show, state=state, width=width)


#-----------------------------------------------------------------------------------------------------------------------

app = SimpleApp()
