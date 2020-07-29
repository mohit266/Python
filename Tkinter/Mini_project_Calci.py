from tkinter import *
import math


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("490x720")
        self.maxsize(490, 800)

    def label(self, inp):
        Label(self, text=inp, pady="10", bg="grey", font="Italic 14 bold").pack(fill="x")

    def calculation_window(self):
        # win variable is the screen value
        self.win = StringVar()
        self.win.set("0")
        self.screen = Entry(textvariable=self.win, font="Italic 40 bold", relief=SUNKEN, justify="right", bd=3)
        self.screen.pack(side="top", anchor="nw", ipady="21")

    def getvals(self, event):
        global win
        text = event.widget.cget("text")
        # print(text)
        if text == "=":
            if self.win.get().isdigit():
                value = int(self.win.get())
            else:
                try:
                    if '√' in self.win.get():
                        val = self.win.get()
                        ans = math.sqrt(int(val[1:]))
                        ans = round(ans, 6)
                        self.win.set(ans)
                        self.screen.update()

                    elif 'sin' in self.win.get():
                        val = self.win.get()
                        val = [i for i in val if i.isdigit()]
                        self.win.set(math.sin(math.radians(int("".join(val)))))
                        self.screen.update()
                        val.clear()

                    elif 'cos' in self.win.get():
                        val = self.win.get()
                        val = [i for i in val if i.isdigit()]
                        self.win.set(math.cos(math.radians(int("".join(val)))))
                        self.screen.update()
                        val.clear()

                    elif 'tan' in self.win.get():
                        val = self.win.get()
                        val = [i for i in val if i.isdigit()]
                        self.win.set(math.tan(math.radians(int("".join(val)))))
                        self.screen.update()
                        val.clear()

                    value = eval(self.screen.get())
                    value = round(value, 6)
                    self.win.set(value)
                    self.screen.update()

                except Exception as e:
                    self.win.set("Error")
                    self.screen.update()

        elif text == "√":
            self.win.set(text)
            self.screen.update()

        elif text == "C":
            self.win.set("0")
            self.screen.update()

        else:
            if self.win.get() == "0":
                self.win.set("")
                self.screen.update()
            self.win.set(self.win.get() + str(text))
            self.screen.update()

    def f1(self, first, second, third, symbol):

        self.frame = Frame(self)

        self.button_1 = Button(self.frame, text=first, padx="40", pady="20", font="Italic 40 bold", bd=2)
        self.button_1.bind('<Button-1>', self.getvals)
        self.button_1.pack(side="left", anchor="nw")

        self.button_1 = Button(self.frame, text=second, padx="40", pady="20", font="Italic 40 bold", bd=2)
        self.button_1.bind('<Button-1>', self.getvals)
        self.button_1.pack(side="left", anchor="nw")

        self.button_1 = Button(self.frame, text=third, padx="40", pady="20", font="Italic 40 bold", bd=2)
        self.button_1.bind('<Button-1>', self.getvals)
        self.button_1.pack(side="left", anchor="nw", ipadx=2)

        self.button_1 = Button(self.frame, text=symbol, padx="40", pady="20", font="Italic 40 bold", bd=2)
        self.button_1.bind('<Button-1>', self.getvals)
        self.button_1.pack(side="left", anchor="nw", ipadx=3)

        self.frame.pack(side="top", anchor="nw")

    def equal(self):
        self.frame_2 = Frame(self)

        self.button_1 = Button(self.frame_2, text=".", padx="60", pady="10", font="Italic 40 bold", bd=2)
        self.button_1.bind('<Button-1>', self.getvals)
        self.button_1.pack(side="left", anchor="nw")

        self.button_1 = Button(self.frame_2, text="=", padx="145", pady="10", font="Italic 40 bold", bd=2)
        self.button_1.bind('<Button-1>', self.getvals)
        self.button_1.pack()

        self.frame_2.pack(side="top", anchor="nw")

    def SCT(self):
        self.frame_3 = Frame(self)

        self.button_1 = Button(self.frame_3, text="sin", padx="32", pady="10", font="Italic 35 bold", bd=2)
        self.button_1.bind('<Button-1>', self.getvals)
        self.button_1.pack(side="left", anchor="nw")

        self.button_1 = Button(self.frame_3, text="cos", padx="38", pady="10", font="Italic 35 bold", bd=2)
        self.button_1.bind('<Button-1>', self.getvals)
        self.button_1.pack(side="left", anchor="nw")

        self.button_1 = Button(self.frame_3, text="tan", padx="38", pady="10", font="Italic 35 bold", bd=2)
        self.button_1.bind('<Button-1>', self.getvals)
        self.button_1.pack(side="top", anchor="nw")

        self.frame_3.pack(side="top", anchor="nw")


if __name__ == '__main__':
    root = GUI()
    root.title("Calculator")
    # root.wm_iconbitmap("calculator.ico")
    # root.label("Calculator")
    root.calculation_window()
    root.f1(7, 8, 9, "*")
    root.f1(4, 5, 6, "+")
    root.f1(1, 2, 3, "-")
    root.f1(0, "C", "/ ", "√")
    root.SCT()
    root.equal()
    root.mainloop()