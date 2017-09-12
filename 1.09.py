from tkinter import *
root = Tk()
Label(root, text="Click at different\n locations in the frame below").pack()


def callback(event):
    print(dir(event))
    print("You clicked at", event.x, event.y)


def b_event(event):
    print(dir(event))
    print("hello")

frame = Frame(root, bg='khaki', width=130, height=80)
frame.bind("<Double-Button-1>", callback)
frame.bind("<Leave>", b_event)
frame.pack()
root.mainloop()
