import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
import pymysql
import os
import shutil
#import db_config

form = tk.Tk()
form.title("asd")
form.geometry("500x280")

tab_parent = ttk.Notebook(form)

tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)

tab_parent.add(tab1, text = "All records")
tab_parent.add(tab2, text = "New Record")

tab_parent.pack(expand = 1, fill = 'both')

form.mainloop()


