from tkinter import *  
from PIL import ImageTk,Image  

root = Tk()  
canvas = Canvas(root, width = 300, height = 300)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("fb1.png"))  
canvas.create_image(20, 20, anchor=NW, image=img) 
self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
root.mainloop()