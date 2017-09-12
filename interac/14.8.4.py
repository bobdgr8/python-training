import tkinter as tk
from tkinter import filedialog
import os

application_window = tk.Tk()

my_filetypes = [("all files", ".*"), ("text files", ".txt")]

answer = filedialog.askdirectory(parent=application_window, initialdir=os.getcwd(), title="Please select a folder:")
print(answer)
answer = filedialog.askopenfilename(parent=application_window, initialdir=os.getcwd(), title="Please select one or more files:", filetypes=my_filetypes)
print(answer)
