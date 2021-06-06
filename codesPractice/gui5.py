import tkinter as tk
from tkinter import *

root = tk.Tk()

label_w = tk.Label(root, text="hello tkinter")
label_w.pack()

counter = 0
def counter_label(label):
	def count():
		global counter
		counter += 1
		label.config(text=str(counter))
		label.after(1000, count)
	count()

root.title("contador!")
label = tk.Label(root, fg="green")
label.pack()
counter_label(label)
	
button = tk.Button(root, text="Stop & close", width=30, fg="red", bg = "black", command=root.destroy)
button.pack()

label_2 = tk.Label(root, 
	text = "Red text in times font",
	fg = "red",
	font = "Times")
label_2.pack()

label_3 = tk.Label(root,
	text = "este es el label 2",
	fg = "light blue",
	bg = "dark green",
	font = "Helvetica 21 bold italic underline")
label_3.pack()

whatever_text = "Este es un texto cualquiera que se adecua al widget"
message_1 = tk.Message(root, text = whatever_text)
message_1.config(
	bg = 'darkblue',
	fg = 'white',
	font = ('verdana', 24, 'italic', 'bold'),
	borderwidth = 100,
	relief = 'raised', #Other options: sunken, groove, ridge
	bd = 30,
	cursor = '',
	anchor = 'e'
	)
message_1.pack()

def write_something():
	print("Texto aleatorio impreso!")

frame_1 = tk.Frame(root)
frame_1.pack()

button_2 = tk.Button(frame_1, 
	text = "Imprima Mensaje",
	fg = "red",
	command = write_something )

button_2.pack(side = tk.LEFT)

button_3 = tk.Button(frame_1,
	text = "otro boton",
	fg = "green",
	command = write_something )
button_3.pack()

select_1 = tk.IntVar()
select_1.set(1)

languagesList = [
	("python", 1),
	("perl", 2),
	("java", 3),
	("cpp", 4),
	("c", 5)
]

def showSelect():
	print(select_1.get())

def showSelect2():
	print(select_2.get())

label_4 = tk.Label(root,
	text = "eliga su lenguaje de programacion",
	justify = tk.LEFT,
	padx = 20
	)
label_4.pack()

for val, language in enumerate(languagesList):
	tk.Radiobutton(root,
		text = language,
		padx = 20,
		variable = select_1,
		command = showSelect,
		value = val).pack(anchor = tk.W)

select_2 = tk.IntVar()
select_2.set(1)

for val, language in enumerate(languagesList):
	tk.Radiobutton(root,
		text = language,
		indicatoron = 0,
		width = 30,
		padx = 20,
		variable = select_2,
		command = showSelect2,
		value = val).pack(anchor = tk.W)

### Creacion de un nuevo Frame, que se llama frame_2
frame_2 = tk.Frame(root)
frame_2.pack()

def var_states():
	print(" masculino: %d, \n femenino: %d" % (var1.get(), var2.get()))

label_5 = tk.Label(frame_2,
	text = "Your sex: ",
	)
var1 = IntVar()
label_5.grid(row = 0, sticky = W)


checkbutton_1 = tk.Checkbutton(frame_2,
	text = "masculino",
	variable = var1
	)
var2 = IntVar()
checkbutton_1.grid(row = 1, sticky = W)

checkbutton_2 = Checkbutton(frame_2,
	text = "femenino",
	variable = var2
	)
checkbutton_2.grid(row = 2, sticky = W)

button_4 = Button(frame_2,
	text = "QUIT",
	bg = "red",
	fg = "light grey",
	command = frame_2.quit
	)
button_4.grid(row = 3, sticky = W, pady = 4)

button_5 = Button(frame_2,
	text = "SHOW",
	bg = "green",
	fg = "light grey",
	command = var_states
	)
button_5.grid(row = 4, sticky = W, pady = 4)

frame_3 = tk.Frame(root, bd=1, relief=SUNKEN, width=768, height=576, bg="light grey", colormap="new")
frame_3.pack(fill=X, padx=5, pady=5)

label_6 = Label(frame_3, text = "user")
label_6.grid(row = 0, column = 0, sticky = W)

label_7 = Label(frame_3, text = "password")
label_7.grid(row = 1, column = 0, sticky = W)

entry_1 = Entry(frame_3)
entry_1.grid(row = 0, column = 1)

entry_2 = Entry(frame_3)
entry_2.grid(row = 1, column = 1)

button_6 = Button(frame_3, text = "Cerrar", fg = "light grey", bg = "dark red", command = frame_3.quit)
button_6.grid(row = 1, column = 2, sticky = E)

button_7 = Button(frame_3, text = "ENVIAR", fg = "dark green", bg = "light green", command = frame_3.quit)
button_7.grid(row = 0, column = 2, sticky = E)

#### Definicion y uso de frame_4
frame_4 = tk.Frame(root)
frame_4.pack()

scale_1 = Scale(frame_4, from_= 0, to = 50)
scale_1.set(19)
scale_1.pack()

scale_2 = Scale(frame_4, from_= 0, to = 100, orient = HORIZONTAL)
scale_2.set(67)
scale_2.pack()

scale_3 = Scale(frame_4, from_ = 0, to = 200, tickinterval = 8, orient = HORIZONTAL, length = 600)
scale_3.pack()

def getValues_1():
	print(scale_1.get(), scale_2.get(), scale_3.get())

button_8 = Button(frame_4, text="Obtener valores", command = getValues_1)
button_8.pack()


root.mainloop()