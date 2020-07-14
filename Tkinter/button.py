from tkinter import *

root = Tk()

root.geometry("700x350")

def clickhere():
    print("Hii Mohit here")

def youranswer():
    print("I m doing well")

def lst_msg():
    print("Good bye!!")

# f1 --> frame
f1 = Frame(root, borderwidth=4, relief=SUNKEN)
f1.pack(side=TOP, anchor="nw", fill="x")

# b1 --> button
b1 = Button(f1, bg="grey", fg="black", text="Enter Here to check the message", command=clickhere)
b1.pack(side=LEFT, padx=2, fill="x")

b2 = Button(f1, bg="grey", fg="black", text="How you doing ", command=youranswer)
b2.pack(side=LEFT, padx=2, fill="x")

b3 = Button(f1, bg="grey", fg="black", text="Enter to say goodbye", command=lst_msg)
b3.pack(side=LEFT, padx=2, fill="x")

root.mainloop()
