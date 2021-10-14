from tkinter import *
from PIL import ImageTk, Image
root=Tk()

image = Image.open('picture.png')
# The (450, 350) is (height, width)
image = image.resize((450, 350), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
my_img = Label(image = my_img)
my_img.pack()

root.mainloop()