from tkinter import *

def evnt(event):
    print("Thank you for clicking the button")
    print(f"You clicked on the button at {event.x},{event.y}")

def evnt_scnd(event):
    print("Thank you for checking..")

root = Tk()
root.title("Events Handling in Tkinter")
root.geometry("500x400")

widget = Button(root, text="Please Click me")
widget.pack()

scnd = Button(root, text="Checking")
scnd.pack()

widget.bind('<Button-1>', evnt)
widget.bind('<Double-1>', quit)
scnd.bind('<Button-1>', evnt_scnd)

root.mainloop()
