#
# author: a5892731
# date: 2021-10-14
# update:
#
# Source:
# http://matrix.umcs.lublin.pl/~akrajka/PYTHON-I/Wyklady/Python_cw01.pdf
# Zad. 4.5. Geometria place i przeglądarka


from tkinter import *
from PIL import Image, ImageTk



class SimpleApp(object):
    def __init__(self, **kwargs):
        self.window_width = 600
        self.window_height = 700
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
        self.window.title("Geometria place i przeglądarka")
        #icon = PhotoImage(file = "files/icon.png")
        self.window.geometry("{}x{}".format(self.window_width, self.window_height))
        self.window.resizable(width=False, height=False)
        #self.window.iconphoto(True, icon) # icon in upper, left corner of program window
        #self.window.config(background = "#cfd1cf") # "hex color picker" search in google

    def frame_settings(self):
        self.top_frame = LabelFrame(self.window, height=50, background = "#cfd1cf", bd = 5)
        self.top_frame.pack(fill="both")
        self.center_frame = Frame(self.window)
        self.center_frame.pack(fill="both", expand="yes")
        self.bottom_frame = LabelFrame(self.window, height=50, background = "#cfd1cf", bd = 5)
        self.bottom_frame.pack(fill="both",)


    def draw_on_frame(self):
        self.draw_picture_widget(self.center_frame)
        self.center_frame.columnconfigure(0, minsize=600)

        for column in range(12):
            self.bottom_frame.columnconfigure(column, minsize=50)
        for row in range(3):
            self.bottom_frame.rowconfigure(row, minsize=5)


        for column in range(1, 11):
            self.draw_button_widget(self.bottom_frame, str(column),
                                    lambda x=column: self.button_click(x)
                                    ).grid(column=column-1, row=1)



        self.draw_button_widget(self.bottom_frame, "Koniec", quit, 10, "red", "yellow").grid(
            column=10, row=1, columnspan=2)

    def draw_button_widget(self, frame, text, command = "", width = 2, bg="black", fg = "white"):
        return Button(frame, font=("Arial", 8), text=text, width = width, border=3, command=command, bg = bg, fg = fg)

    def draw_picture_widget(self, frame, addres = 'foto/pic1.jpg'):

        def re_sizer(image, max = 600):
            width, height = image.size

            if height > width:
                scale = height/max
                width = width / scale
                height = height / scale
            else:
                scale = width/max
                width = width / scale
                height = height / scale
            return int(width), int(height)

        my_img = Image.open(addres)
        width, height = re_sizer(my_img)

        self.my_img = my_img.resize((width, height), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.my_img)
        return Label(frame, image = self.image).grid(column=0, row=0)

    def button_click(self, pic_num):
        self.draw_picture_widget(self.center_frame, "foto/pic{}.jpg".format(pic_num))



#-----------------------------------------------------------------------------------------------------------------------

app = SimpleApp()
