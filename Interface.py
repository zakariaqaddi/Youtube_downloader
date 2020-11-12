from tkinter import *
top = Tk(className=' GUI YOUTUBE DOWNLOADER')
# top['background'] = '#856ff8'
top.geometry("450x250")

Choix = ['video', 'audio', 'playlist_video', 'playlist_audio']
radio = IntVar()

title = Label(
    top, text="Bienvenue, Ce petit programme vous permet de télécharger video, audio ou playlist")
title.grid(row=1, column=2)

url = Label(top, text=" Enter le lien Youtube ")
url.grid(row=3, column=2)

e1 = Entry(top)
e1.grid(row=4, column=2)

R1 = Radiobutton(top, text=Choix[0], variable=radio, value=1)
R1.grid(row=6, column=2)

R2 = Radiobutton(top, text=Choix[1], variable=radio, value=2)
R2.grid(row=7, column=2)

R3 = Radiobutton(top, text=Choix[2], variable=radio, value=3)
R3.grid(row=8, column=2)

R4 = Radiobutton(top, text=Choix[3], variable=radio, value=4)
R4.grid(row=9, column=2)

b = Button(top, text="Lancer")
vide1 = Label(top, text='')
vide2 = Label(top, text='')
vide1.grid(row=10, column=2)
vide2.grid(row=5, column=2)
b.grid(row=11, column=2)
top.mainloop()
