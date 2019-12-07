from tkinter import *
from PIL import Image, ImageTk


root = Tk()

photo2 = PhotoImage(file = "fb2.png")
label2 = Label(root, image = photo2)
label2.pack()

# using PIL stuff
image1 = Image.open("ins1.jpg")
photo1 = ImageTk.PhotoImage(image1)
label1 = Label(image = photo1)
label1.image = photo2 # keep a reference!
label1.pack()

image3 = Image.open("ins1.jpg")
image3 = image3.resize((50, 50), Image.ANTIALIAS)
image3 = ImageTk.PhotoImage(image3)
label3 = Label(root, image = image3)
label3.pack()

root.mainloop()