from tkinter import messagebox

answer = messagebox.askokcancel("Question", "Do you wanna open this file?")
print(type(answer))
answer = messagebox.askyesnocancel("Question", "Continue playing???")
print(answer)
