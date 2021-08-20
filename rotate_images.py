#
# author: a5892731
# date: 2021-08-20
# update:
#
# description: this is a program with simple GUI for Python
#
# source: Bro Code --> https://www.youtube.com/watch?v=TuLxsvK4svQ
#         Stack: https://stackoverflow.com/questions/15736530/python-tkinter-rotate-image-animation/37577230

from tkinter import *

import tkinter as tk
from PIL import ImageTk
from PIL import Image

class SimpleApp(object):
    def __init__(self, master, filename, **kwargs):
        self.master = master
        self.filename = filename
        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()

        self.update = self.draw().__next__
        master.after(100, self.update)

    def draw(self):
        image = Image.open(self.filename)
        angle = 0
        while True:
            tkimage = ImageTk.PhotoImage(image.rotate(angle))
            canvas_obj = self.canvas.create_image(
                250, 250, image=tkimage)
            self.master.after_idle(self.update)
            yield
            self.canvas.delete(canvas_obj)
            angle += 10
            angle %= 360

root = tk.Tk()
app = SimpleApp(root, 'icon.png')
root.mainloop()