from tkinter import *

root = Tk()

root.geometry("450x300")

scrollbar = Scrollbar(root)

label = Label(root, text="You are going great man!!", yscrollcommand=scrollbar.set)
label.pack(fill=BOTH)

scrollbar.pack(side="right", fill=Y)

scrollbar.config()

root.mainloop()