#
# author: a5892731
# date: 2021-10-14
# update:
#
# Source:
# http://matrix.umcs.lublin.pl/~akrajka/PYTHON-I/Wyklady/Python_cw01.pdf
# Zad. 4.4. Geometria pack


from tkinter import *
from PIL import Image, ImageTk



class SimpleApp(object):
    def __init__(self, **kwargs):
        self.window_width = 600
        self.window_height = 400
        self.window = Tk()
        self.image_size=100

        self.update = self.draw().__next__
        self.window.after(100, self.update)

    def draw(self):
        self.draw_window_atributes()
        self.frame_settings()
        self.draw_on_frame()
        self.window.mainloop()

    def draw_window_atributes(self):
        self.window.title("Geometria pack")
        #icon = PhotoImage(file = "files/icon.png")
        self.window.geometry("{}x{}".format(self.window_width, self.window_height))
        #self.window.resizable(width=False, height=False)
        #self.window.iconphoto(True, icon) # icon in upper, left corner of program window
        #self.window.config(background = "#cfd1cf") # "hex color picker" search in google

    def frame_settings(self):
        #self.left_frame = LabelFrame(self.window, text = "This is my frame", padx = 25, pady =25)
        self.left_frame = Frame(self.window)
        self.left_frame.pack(side = LEFT)
        self.frame_inside_left_frame = Frame(self.window)
        self.frame_inside_left_frame.pack(side = LEFT)

        self.right_frame = Frame(self.window)
        self.right_frame.pack(side = RIGHT)

    def draw_on_frame(self):

        przycisk11 = self.draw_button_widget(self.frame_inside_left_frame, "Przycisk 11", "").pack(side = TOP)
        przycisk12 = self.draw_button_widget(self.frame_inside_left_frame, "Przycisk 12", "").pack(side = TOP)
        przycisk13 = self.draw_button_widget(self.frame_inside_left_frame, "Przycisk 12", "").pack(side = TOP)

        przycisk21 = self.draw_button_widget(self.right_frame, "Przycisk 21", "").pack(side = RIGHT)
        przycisk22 = self.draw_button_widget(self.right_frame, "Przycisk 22", "", 30).pack(side = RIGHT)
        przycisk23 = self.draw_button_widget(self.right_frame, "Przycisk 22", "").pack(side = RIGHT)


    def draw_button_widget(self, frame, text, command = "", width = 10):
        return Button(frame, font=("Arial", 12), text=text, width = width, border=3, command=command)




#-----------------------------------------------------------------------------------------------------------------------

app = SimpleApp()
