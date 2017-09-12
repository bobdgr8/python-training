from tkinter import *
root = Tk()

frame = Frame(root)
# demo of side and fill functions

Label(frame, text="Pack demo of side and fill").pack()
Button(frame, text="A").pack(side=LEFT, fill=Y)
Button(frame, text="B").pack(side=TOP, fill=X)
Button(frame, text="C").pack(side=RIGHT, fill=NONE)
Button(frame, text="D").pack(side=TOP, fill=BOTH)
frame.pack()

Label(root, text="Pack demo of expand").pack()
Button(root, text="I dont expand").pack()
Button(root, text="I do not fill X but I expand").pack(expand=1)
Button(root, text="I fill X and expand").pack(fill=X, expand=1)

root.mainloop()
