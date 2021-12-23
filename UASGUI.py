from tkinter import * //mengambil semua yang ada di library tkinter
from tkinter import messagebox // mengambil messagebox dari library tkinter
import random // mengambil libabry random

#peluang dan angka acak
peluang = 10
x = random.randint(1,100)


root = Tk() // 

root.config(background='light blue') // pengaturan background dari windows

label = Label(text="Permainan", font="Normal 30", background='light blue') //Pengaturan label terdiri dari : teks, font, dan background
label.grid(row=0, column=0, columnspan=2) // pengaturan letak label

data = Entry(font="Normal 30", bd=10) // pengaturan tempat pengetikan 
data.grid(row=1, column=0) // pengaturan letak pengetikan

def perintah(): // hasil dari pengetikan
    print(data.get()) // akan diprint
    data.delete(0, END) // akan didelete di dalam pengetikan

button = Button(text="Klik", font="Normal 20", //pengaturan button seperti text, font, background ketika diklik, dan aksi dari button tersebut
activebackground="red", command=perintah)
button.grid(row=1, column=1) // pengaturan letak button

teks = Text(width=50, height=50, bd=10, font="Normal 15") // pengaturan text seperti width, height, background, dan font
teks.grid(row=2, column=0, columnspan=2) // pengaturan letak teks
root.mainloop() // menjalankan program 
