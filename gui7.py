import tkinter as tk
from tkinter import Tk, Label, Button, W, E, LEFT, RIGHT, StringVar, END, Entry, IntVar

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.but1 = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.but1["text"] = "ok"

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def say_shit(self):
        print("shit")

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="this is my first gui")
        self.label.pack()

        self.greet_button = Button(master, text="Greetings!", command = self.greet)
        self.greet_button.pack()

        self.greet_button2 = Button(master, text="SecondGreetings!", command = self.greet2)
        self.greet_button2.pack()

        self.close_button = Button(master, text = "Close now!", command = master.quit)
        self.close_button.pack()

    def greet(self):
        print("Hallo!")

    def greet2(self):
        print("this is second hallo!")

class Calculator():
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.total = 0
        self.enteredNumber = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable = self.total_label_text)

        self.label = Label(master, text = "Total: ")

        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate = "key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text = "+", command = lambda: self.update("add"))
        self.substract_button = Button(master, text = "-", command = lambda: self.update("substract"))
        self.reset_button = Button(master, text = "Reset", command = lambda: self.update("reset"))

        self.label.grid(row = 0, column = 0, sticky = W)
        self.total_label.grid(row = 0, column = 1, columnspan = 2, sticky = E)

        self.entry.grid(row = 1, column = 0, columnspan = 3, sticky = W + E)

        self.add_button.grid(row = 2, column = 0)
        self.substract_button.grid(row = 2, column = 1)
        self.reset_button.grid(row = 2, column = 2, sticky = W + E)

    def validate(self, new_text):
        if not new_text:
            self.enteredNumber = 0
            return True

        try:
            self.enteredNumber = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.enteredNumber
        elif method == "substract":
            self.total -= self.enteredNumber
        else:
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

#root = tk.Tk()
#app = Application(master=root)
root = Tk()
my_gui = Calculator(root)
root.mainloop()