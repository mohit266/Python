from tkinter import *

root = Tk()

root.geometry("600x380")

root.title("Exercise 2")


def button1():
    print("Button 1 is pressed")


def button2():
    print("Button 2 is pressed")


def button3():
    print("Button 3 is pressed")


def button4():
    print("Button 4 is pressed")


def button5():
    print("Button 5 is pressed")


label = Label(text="Welcome to tkinter", bg="grey", fg="white")
label.pack(side=TOP, fill="x")

frame = Frame(root, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw", fill="x")

b1 = Button(frame, text="1", bg="white", fg="black", padx=25, pady=25, command=button1)
b1.pack(fill="x")

b2 = Button(frame, text="2", bg="white", fg="black", padx=25, pady=25, command=button2)
b2.pack(fill="x")

b3 = Button(frame, text="3", bg="white", fg="black", padx=25, pady=25, command=button3)
b3.pack(fill="x")

b4 = Button(frame, text="4", bg="white", fg="black", padx=25, pady=25, command=button4)
b4.pack(fill="x")

b5 = Button(frame, text="5", bg="white", fg="black", padx=25, pady=25, command=button5)
b5.pack(fill="x")


root.mainloop()