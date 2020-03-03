#import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Menu
import mysql.connector as mysql
from tkinter import StringVar, IntVar
from tkinter import scrolledtext


window = Tk()
window.title("Data Base App, using TK")
window.geometry("900x680")

class gui1:
    def __init__(self, master, f_name1="", f_number1="", f_kw1=""):
        self.master = master
        self.f_name1 = f_name1
        self.f_number1 = f_number1
        self.f_kw1 = f_kw1
        #master.title = "basic gui 1 using tkinter"
        self.tabControl1 = ttk.Notebook(self.master)
        self.FrameTab1 = Frame(self.tabControl1)
        self.FrameTab2 = Frame(self.tabControl1)
        self.FrameTab3 = Frame(self.tabControl1)
        self.tabControl1.add(self.FrameTab1, text = "Input Data")
        self.tabControl1.add(self.FrameTab2, text = "Show Record")
        self.tabControl1.add(self.FrameTab3, text = "Comments")
        self.tabControl1.grid(columnspan = 10, rowspan = 10, padx = 10, pady = 10, sticky=W+E+N+S)
        #some variables
        self.f_name1 = StringVar()
        self.f_number1 = StringVar()
        self.f_kw1 = IntVar()
        self.f_result1 = StringVar()
        self.consult_parameter = StringVar()
        #self.button_1 = Button(self.FrameTab1, text = "button_1", bg = "green", fg = "yellow", command=self.saludo).grid() #fg = "red" is the fontColor, bg is background color
        # Entries 1
        #self.frame_entries_1 = Frame(self.FrameTab1).grid(columnspan = 5, rowspan = 5, sticky = W + E + N + S, padx = 5, pady = 5, column = 2, row = 9, ipadx = 5, ipady = 5)
        self.name_entry_1 = Entry(self.FrameTab1, textvariable = self.f_name1, width = 40).grid(row = 4, column = 1)
        self.name_label_1 = Label(self.FrameTab1, text = "Name: ", fg = "white").grid(row = 4, column = 0, sticky = E)
        # Entries 2
        #self.frame_entries_2 = Frame(self.FrameTab1).grid()
        self.name_entry_2 = Entry(self.FrameTab1, textvariable = self.f_number1, width = 40).grid(row = 5, column = 1)
        self.name_label_2 = Label(self.FrameTab1, text = "Number: ", fg = "white").grid(row = 5, column = 0, sticky = E)
        # Entries 3
        #self.frame_entries_3 = Frame(self.FrameTab1).grid()
        self.name_entry_3 = Entry(self.FrameTab1, textvariable = self.f_kw1, width = 40).grid(row = 6, column = 1)
        self.name_label_3 = Label(self.FrameTab1, text = "Keyword: ", fg = "white").grid(row = 6, column = 0, sticky = E)
        # Button submit
        self.button_submit = Button(self.FrameTab1, text = "Submit", width = 20, bg = "green", fg = "white", command = self.query2).grid(column = 3, row = 9)
        self.button_exit = Button(self.FrameTab1, text = "Exit", width = 20, bg = "red", fg = "light grey", command = master.quit).grid(column = 2, row = 9)
        self.button_test = Button(self.FrameTab1, text = "test1", bg = "blue", fg = "white", command = self.saludo).grid(column = 0, row = 19)
        # Tab Show Record
        # Tab 2 Section, search for an id
        self.entry_search_1 = Entry(self.FrameTab2, textvariable = self.consult_parameter, width = 20).grid(row = 4, column = 1)
        self.label_search_1 = Label(self.FrameTab2, text = "Name: ", fg = "white").grid(row = 4, column = 0, sticky = E)
        self.button_search_1 = Button(self.FrameTab2, text = "Pull", bg = "blue", fg = "white", command = self.showallrecords).grid(column = 3, row = 4)
        # Menu creation
        #file menu
        self.menubar1 = Menu(self.master)
        self.menu_item_file = Menu(self.menubar1, tearoff = 0)
        self.menu_item_file.add_command(label = "Saludo", command = self.saludo)
        self.menu_item_file.add_separator()
        self.menu_item_file.add_command(label = "Exit", command = master.quit)
        self.menubar1.add_cascade(label = "File", menu = self.menu_item_file)
        # Edit Menu
        self.menu_item_edit = Menu(self.menubar1, tearoff = 0)
        self.menu_item_edit.add_command(label = "Saludo", command = self.saludo)
        self.menu_item_edit.add_separator()
        self.menu_item_edit.add_command(label = "Exit", command = master.quit)
        self.menubar1.add_cascade(label = "Edit", menu = self.menu_item_edit)
        self.master.config(menu = self.menubar1)
        # Help Menu
        self.menu_item_help = Menu(self.menubar1, tearoff = 0)
        self.menu_item_help.add_command(label = "About", command = self.saludo)
        self.menu_item_help.add_separator()
        self.menu_item_help.add_command(label = "Exit", command = master.quit)
        self.menubar1.add_cascade(label = "Help", menu = self.menu_item_help)
        self.master.config(menu = self.menubar1)
        # LabelBox grouping
        self.group1 = LabelFrame(self.FrameTab2, text="Text Box", padx=5, pady=5)
        self.group1.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.group1.rowconfigure(0, weight=1)
        self.group1.columnconfigure(0, weight=1)
        self.txtbox = scrolledtext.ScrolledText(self.group1, width=40, height=10)
        self.txtbox.grid(row=0, column=0, sticky=E+W+N+S)


    def saludo(self):
        print("Enviado!", self.f_name1)

    def query2(self):
        name1 = self.f_name1.get()
        number1 = self.f_number1.get()
        kw1 = self.f_kw1.get()
        db = mysql.connect(
        host = "localhost",
        user = "admin",
        passwd = "123qwe",
        database = "ss1",
        )
        #First test
        cursor = db.cursor()
        sql1 = "INSERT INTO Employee (name1, number1, kw1) VALUES ('ppyyg','245a','778')"
        cursor.execute(sql1)
        db.commit()
        print(cursor.rowcount, "record(s) affected")
        #second test
        cursor = db.cursor()
        sql1 = """INSERT INTO Employee (name1, number1, kw1) VALUES (%s, %s, %s)"""
        data1 = ('tturk', '88w', 445)
        cursor.execute(sql1, data1)
        db.commit()
        print(cursor.rowcount, "record(s) affected")
        #third test
        cursor = db.cursor()
        cursor.execute("INSERT INTO Employee (name1, number1, kw1) VALUES (%s, %s, %s)", (name1, number1, kw1))
        db.commit()
        print(cursor.rowcount, "record(s) affected")

    def showallrecords(self):
        Data = self.readfromdatabase()
        for index, dat in enumerate(Data):
            self.kk1 = Label(self.FrameTab2, text=dat[0]).grid(row=index+10, column=0)
            self.kk2 = Label(self.FrameTab2, text=dat[1]).grid(row=index+10, column=1)
            self.kk3 = Label(self.FrameTab2, text=dat[2]).grid(row=index+10, column=2)

    def readfromdatabase(self):
        consult_parameter1 = self.consult_parameter.get()
        db = mysql.connect(host = "localhost", user = "admin", passwd = "123qwe", database = "ss1",)
        cursor = db.cursor()
        sql1 = "SELECT * FROM Employee WHERE idq = %s"
        data1 = (consult_parameter1,)
        cursor.execute(sql1, data1)
        return cursor.fetchall()


mydb = mysql.connect(
host="localhost",
user="admin",
passwd="123qwe"
)

cursor = mydb.cursor()
cursor.execute("SHOW DATABASES")
databases = cursor.fetchall()
print(databases)

dbapp1 = gui1(window)
# menu1 = Menu(window)
# window.config(menu = menu1)
window.mainloop()

# root = Tk()
# my_gui = gui1(root)
# root.mainloop()

###########################################
# Database structure:
# id, autoincrement, int
# name1, varchar(20)
# number1, int(5)
# kw1, varchar(10)
#