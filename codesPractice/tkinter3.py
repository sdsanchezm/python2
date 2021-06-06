from tkinter import *
from tkinter import ttk
from tkinter import Menu
 
window = Tk()
window.title("Python Gui principles, using TK")
window.geometry('850x750')

vt1 = StringVar()


def x1():
 print(vt1)
 print(vt1.get())
 vt1.set("Text on screen 1")

def x2():
 vt1.set("Another text on screen 2")

tabControl1 = ttk.Notebook(window)

FrameTab1 = Frame(tabControl1)
FrameTab2 = Frame(tabControl1)
FrameTab3 = Frame(tabControl1)

tabControl1.add(FrameTab1, text = "first")
tabControl1.add(FrameTab2, text = "second")
tabControl1.add(FrameTab3, text = "third")

label1 = Label(FrameTab1, text = 'label1').grid(sticky = W)
label2 = Label(FrameTab2, text = 'label2').grid(sticky = W)
label3 = Label(FrameTab3, text = 'label3').grid(sticky = W)
label4 = Label(FrameTab1, textvariable = vt1, font=("Arial Bold", 40)).grid(column = 0, row = 4)
button1 = Button(FrameTab1, text="Exit Button", command = window.quit, bg = 'black', fg = 'white').grid(column=0, row=10, sticky = W)
button2 = Button(FrameTab1, text="Write Button 2", command = x1).grid(column=0, row=1, sticky = W)
button3 = Button(FrameTab1, text="Write Button 3", command = x2).grid(column=0, row=2, sticky = W)

tabControl1.pack(expand = 1, fill = 'both')

window.mainloop()