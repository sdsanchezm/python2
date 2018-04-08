import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("Widget Example")
#window.wm_iconbitmap('icon.ico')

lbl_1 = tkinter.Label(window, text = "username:")
ent_1 = tkinter.Entry(window)
lbl_2 = tkinter.Label(window, text = "username:")
ent_2 = tkinter.Entry(window)
btn_1 = tkinter.Button(window, text = "Login")

lbl_1.pack()
ent_1.pack()
lbl_2.pack()
ent_2.pack()
btn_1.pack()

window.mainloop()

def donothing():
	filewin = Topleve(root)
	btn_3 = Button(filewin, text = "Do nothing button")
	btn_3.pack()

def test_function():
	print("hell world")

root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "New", command = test_function)
filemenu.add_command(label = "Open", command = test_function)
filemenu.add_command(label = "Save", command = test_function)
filemenu.add_command(label = "Save as...", command = test_function)
filemenu.add_command(label = "Close", command = test_function)

filemenu.add_separator()

filemenu.add_command(label = "Exit", command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)
editmenu = Menu(menubar, tearoff = 0)
editmenu.add_command(label = "Undo", command = test_function)

editmenu.add_separator()

editmenu.add_command(label = "Cut", command = test_function)
editmenu.add_command(label = "Copy", command = test_function)
editmenu.add_command(label = "Paste", command = test_function)
editmenu.add_command(label = "Delete", command = test_function)
editmenu.add_command(label = "Select All", command = test_function)

menubar.add_cascade(label = "Edit", menu = editmenu)

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "Help Index", command = test_function)
helpmenu.add_command(label = "About...", command = test_function)
menubar.add_cascade(label = "Help", menu = helpmenu)

root.config(menu = menubar)
root.mainloop()