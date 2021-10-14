#
# author: a5892731
# date: 2021-10-14
# update:
#
# Source:
# http://matrix.umcs.lublin.pl/~akrajka/PYTHON-I/Wyklady/Python_cw01.pdf
# Zad. 4.3. Pola tekstowe


from tkinter import *
from PIL import Image, ImageTk



class SimpleApp(object):
    def __init__(self, **kwargs):
        self.window_width = 600
        self.window_height = 400
        self.window = Tk()

        self.image_size=100
        #self.image = PhotoImage(file="picture.png")
        my_img= Image.open('picture.png')
        self.my_img = my_img.resize((self.image_size, self.image_size), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.my_img)

        self.update = self.draw().__next__
        self.window.after(100, self.update)

    def draw(self):
        self.draw_window_atributes()
        self.grid_settings()
        self.draw_on_grid()
        self.window.mainloop()

    def draw_window_atributes(self):
        self.window.title("Przykład geometrii grid")
        #icon = PhotoImage(file = "files/icon.png")
        self.window.geometry("{}x{}".format(self.window_width, self.window_height))
        #self.window.resizable(width=False, height=False)
        #self.window.iconphoto(True, icon) # icon in upper, left corner of program window
        #self.window.config(background = "#cfd1cf") # "hex color picker" search in google

    def grid_settings(self):
        self.window.columnconfigure(0, minsize =100)
        self.window.columnconfigure(1, minsize=150)
        self.window.columnconfigure(2, minsize=150)
        self.window.columnconfigure(3, minsize=150)
        self.window.rowconfigure(0, minsize =40)
        self.window.rowconfigure(1, minsize =40)
        self.window.rowconfigure(2, minsize =40)
        self.window.rowconfigure(3, minsize =40)

    def draw_on_grid(self):
        A1 = self.draw_label_widget("Pierwszy").grid(column=0, row=0, sticky=W)
        A2 = self.draw_label_widget("Drugi").grid(column=0, row=1, sticky=W)
        A4 = self.draw_checbox_widget("Rozwiń").grid(column=0, row=3, sticky=W)

        B1 = self.draw_entry_widget().grid(column=1, row=0, sticky=W)
        B2 = self.draw_entry_widget().grid(column=1, row=1, sticky=W)

        C3 = self.draw_button_widget("Powiększ", self.resize_image_up).grid(column=2, row=2, sticky=E)
        C3 = self.draw_button_widget("Zmniejsz", self.resize_image_down).grid(column=3, row=2, sticky=W)

        CD12 = self.draw_picture_widget().grid(column=2, row=0, columnspan=2, rowspan=2)

    def draw_entry_widget(self, text="", show="", state=NORMAL, width=22):
        textEntry = StringVar()
        textEntry.set(text)
        return Entry(self.window, font=("Arial", 12), textvariable=textEntry, show=show, state=state, width=width)

    def draw_label_widget(self, text):
        return Label(self.window, font=("Arial", 12), text = text)

    def draw_button_widget(self, text, command = ""):
        return Button(self.window, font=("Arial", 12), text=text, fg="red", width = 15, border=3, command=command)

    def draw_checbox_widget(self, text):
        return Checkbutton(self.window, font=("Arial", 12), text=text)

    def draw_picture_widget(self):
        return Label(self.window, image = self.image)

    def resize_image_up(self):
        self.resize_image(50)

    def resize_image_down(self):
        self.resize_image(-50)


    def resize_image(self, factor):
        self.image_size = self.image_size + factor
        if self.image_size < 50:
            self.image_size = 50
        self.my_img = self.my_img.resize((self.image_size, self.image_size), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.my_img)
        self.draw_on_grid()


#-----------------------------------------------------------------------------------------------------------------------

app = SimpleApp()
