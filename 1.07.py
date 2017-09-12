from tkinter import *
parent = Tk()
parent.title("Find and replace")

Label(parent, text="Find: ").grid(row=0, column=0, sticky=E)
Entry(parent, width=60).grid(row=0, column=1, padx=2, pady=2, sticky=EW, columnspan=9)

Label(parent, text="Replace: ").grid(row=1, column=0, sticky=E)
Entry(parent, width=60).grid(row=1, column=1, padx=2, pady=2, sticky=EW, columnspan=9)

Button(parent, text="Find").grid(row=0, column=10, sticky=EW, padx=2, pady=2)
Button(parent, text="Find all").grid(row=1, column=10, sticky=EW, padx=2, pady=2)

parent.mainloop()
