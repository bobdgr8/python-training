from tkinter import *

root = Tk()


def show_event_details(event):
    event_name = {"2": "KeyPress", "4": "ButtonPress", "6": "Motion", "9": "FocusIn"}
    print('=' * 50)
    print("EventName=" + event_name[str(event.type)])
    print("EventKeySymbol=" + str(event.keysym))
    print("EventType=" + str(event.type))
    print("EventWidgetId=" + str(event.widget))
    print("EventCoordinate (x,y)=(" + str(event.x) + "," + str(event.y) + ")")
    print("Time:", str(event.time))


def button_press(event):
    print(dir(event))
    print("Pressed button 1")


button1 = Button(root, text="Button Bound to \n Keyboard Enter & Mouse Click")
button1.bind("<Button-1>", button_press)
button1.bind("<Return>", button_press)
button1.pack()

label1 = Label(root, text="Entry is bound to mouse-click\nFocusIn and Keypress Event").pack()
# entry1 = Entry(root, )

root.mainloop()
