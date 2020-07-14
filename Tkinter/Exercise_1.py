from tkinter import *
from PIL import Image, ImageTk
root = Tk()

def every_100(text):
    final_text = text.split()
    final = ""
    for i in range(0, len(final_text)):
        final += " "+final_text[i]
        if i % 18 == 0 and i != 0:
            final += "\n"
    return final

texts=[]
photos=[]

for i in range(0, 3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    img = Image.open(f"{i+1}.jpg")
    img = img.resize((300, 225),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(img))

root.geometry("1100x850")

root.title("Exercise 1")

Label(text="Latest News", fg="black", font="Italic 18 bold").pack(fill="x")
Label(text="July 1,2020", pady=7, font="Italic 10 bold").pack()

for i in range(0,3):
    f1 = Frame(root, pady=10)
    Label(f1, text=texts[i]).pack(side="left")
    Label(f1, image=photos[i], anchor="e").pack(side="right")
    f1.pack(anchor="w")

root.mainloop()