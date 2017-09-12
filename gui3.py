import tkinter as tk
from tkinter import simpledialog

app_window = tk.Tk()

answer = simpledialog.askstring("Input", "What is your first name?", parent = app_window)

if answer is not None:
	print("Your first name is " + answer)
else:
	print("""You dont have a first name???""")

answer = simpledialog.askinteger("Input", "What is your age?", parent = app_window, minvalue = 0, maxvalue = 100)

if answer is not None:
	print("Your age is", answer)
else:
	print("No age?")

answer = simpledialog.askfloat("Input", "What is your salary", parent = app_window, minvalue = 0.00, maxvalue = 100000.0)

if answer is not None:
	print("Your salary is", answer)
else:
	print("No salary????")


