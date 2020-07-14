from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# To create a rectangle specify parameters in this order -- coors of left corner and coors of bottom right.
can_widget.create_rectangle(100, 300, 300, 100, fill="yellow")

can_widget.create_oval(150, 250, 250, 150,fill="white")

can_widget.create_text(200, 200, text="Hello Tkinter")

can_widget.create_line(103, 228, 228, 103)
can_widget.create_line(170, 300, 300, 170)

can_widget.create_line(150, 100, 300, 210)
can_widget.create_line(100, 190, 250, 300)

root.mainloop()