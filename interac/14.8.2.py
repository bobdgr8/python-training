from tkinter import messagebox

answer = messagebox.askyesnocancel("Question", "Do you wanna open this file?")
print(answer)
print(dir(messagebox))
