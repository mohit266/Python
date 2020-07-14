from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("450x300")

    def label(self, inp):
        Label(self, text=inp, pady="10", bg="light blue", font="Italic 14 bold").pack(fill="x")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvariable=self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)

    def frame(self, first, second, third, fourth):
        f1 = Frame(self, pady="20")
        enroll = Label(f1, text=first, pady="5", font="Italic 12").grid(row=0, column=0)
        self.enroll_val = StringVar()
        enroll_entry = Entry(f1, textvariable=self.enroll_val)
        enroll_entry.grid(row=0, column=1)

        name = Label(f1, text=second, pady="5", font="Italic 12").grid(row=1, column=0)
        self.name_val = StringVar()
        name_entry = Entry(f1, textvariable=self.name_val)
        name_entry.grid(row=1, column=1)

        sem = Label(f1, text=third, padx=10, pady="5", font="Italic 12").grid(row=2, column=0)
        self.sem_val = StringVar()
        sem_entry = Entry(f1, textvariable=self.sem_val)
        sem_entry.grid(row=2, column=1)

        mobile = Label(f1, text=fourth, padx=10, pady="5", font="Italic 12").grid(row=3, column=0)
        self.mobile_val = StringVar()
        mobile_entry = Entry(f1, textvariable=self.mobile_val)
        mobile_entry.grid(row=3, column=1)

        f1.pack(side="top")

    def upload(self):
        self.var.set("Submitting..")
        self.statusbar.update()
        import time
        time.sleep(2)
        self.var.set("Submitted")
        self.statusbar.update()
        time.sleep(2)
        self.var.set("Ready")
        print(f" Enrollment no is : {self.enroll_val.get()}\n Name is : {self.name_val.get()}\n Semester is : {self.sem_val.get()}\n Mobile no. is {self.mobile_val.get()}")
        self.enroll_val.set("")
        self.name_val.set("")
        self.sem_val.set("")
        self.mobile_val.set("")

    def button(self):
        Button(text="Submit", command=self.upload).pack()


if __name__ == '__main__':
    root = GUI()
    root.label("Hey Classes")
    root.frame("Enrollment no : ", "Name : ", "Semester : ", "Mobile : ")
    root.button()
    root.status()
    root.mainloop()
