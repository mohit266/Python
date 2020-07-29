from tkinter import *

def func():
    pass

root = Tk()
root.title("Menu & Submenu")
root.geometry("700x450")

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

root.mainloop()