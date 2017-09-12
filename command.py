
from tkinter import *

square = lambda x: x * x


def my_callback():
    my_callback.i += 1
    print(my_callback.i)
my_callback.i = 0
root = Tk()
root.Title = "Title"
print(dir(my_callback))
Button(root, text="Click me", command=my_callback).pack()
root.mainloop()
