import tkinter as tk
from tkinter import *

class gui1:
	def __init__(self, master):
		self.master = master
		master.title = "basic gui 1 using tkinter"
		self.label_1 = Label(master, text = "label_1", fg = "red", bg = "grey")
		self.label_1.pack()
		self.button_1 = Button(master, text = "button_1", bg = "green", command=self.saludo)
		self.button_1.pack()
		self.button_2 = Button(master, text = "SALIR", bg = "red", fg = "light grey", command=master.quit)
		self.button_2.pack()
	
	def saludo(self):
		print("hola!")

root = Tk()
my_gui = gui1(root)
root.mainloop()