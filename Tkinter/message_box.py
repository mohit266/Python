from tkinter import *
import tkinter.messagebox as tmsg

def resize():
    root.geometry(f"{width_val.get()}x{height_val.get()}")

def func():
    pass

def help():
    tmsg.showinfo("Help", "We will help you with this gui")

def rate_us():
    ans = tmsg.askquestion("Feedback", " Was your expierence good ?")
    if ans == "yes":
        msg = "Great...Rate us on appstore please"
    else:
        msg = tmsg.showwarning("Danger", "How dare you..Be in your limit.")
        # msg = "Tell us what went wrong.We will help you as soon as possible."
    tmsg.showinfo("Expierence", msg)

root = Tk()

root.title("Menu & Submenu")
root.geometry("330x150")

Label(root, text="Window resizer", pady="10", font="Italic 14 bold").grid(row=0, column=1)

width = Label(root, text="Width  : ", padx="10", pady="1", font="Italic 14").grid(row=1, column=0)
width_val = StringVar()
width_entry = Entry(root, textvariable=width_val)
width_entry.grid(row=1, column=1)

height = Label(root, text="Height : ", font="Italic 14").grid(row=2, column=0)
height_val= StringVar()
height_entry = Entry(root, textvariable=height_val)
height_entry.grid(row=2, column=1)

Button(text="Apply", command=resize).grid(column=1)

mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New Project", command=func)
m1.add_command(label="Save", command=func)
m1.add_command(label="Open", command=func)
m1.add_separator()
m1.add_command(label="Setting", command=func)
m1.add_command(label="File Properties", command=func)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=func)
m2.add_command(label="Copy", command=func)
m2.add_command(label="Paste", command=func)
m2.add_command(label="Delete", command=func)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

m3=Menu(mainmenu, tearoff=0)

m3.add_command(label="Tool Windows", command=func)
m3.add_command(label="Appearance", command=func)
m3.add_command(label="Quick Definitions", command=func)
m3.add_command(label="Recent Files", command=func)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="View", menu=m3)

m4=Menu(mainmenu, tearoff=0)

m4.add_command(label="Help", command=help)
m4.add_command(label="Rate Us", command=rate_us)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="Other", menu=m4)

root.mainloop()