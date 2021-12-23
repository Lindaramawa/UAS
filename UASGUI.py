from tkinter import *
from tkinter import messagebox
import random

#peluang dan angka acak
peluang = 10
x = random.randint(1,100)


root = Tk()

root.config(background='light blue')

label = Label(text="Permainan", font="Normal 30", background='light blue')
label.grid(row=0, column=0, columnspan=2)

data = Entry(font="Normal 30", bd=10)
data.grid(row=1, column=0)

def perintah():
    print(data.get())
    data.delete(0, END)

button = Button(text="Klik", font="Normal 20", 
activebackground="red", command=perintah)
button.grid(row=1, column=1)

teks = Text(width=50, height=50, bd=10, font="Normal 15")
teks.grid(row=2, column=0, columnspan=2)
root.mainloop()