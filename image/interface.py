# -*- coding: utf-8 -*-
"""
Created on Sat May 30 00:46:00 2020

@author: donny
"""

from tkinter import *
from new_user import *
#créer une première fenêtre 

window_accueil = Tk()

#action après le clic sur le bouton "new account"
def action_new():
    print("bienvenu")

#personnaliser la fenêtre
window_accueil.title("Afriland Bank")
window_accueil.geometry("720x580")
window_accueil.minsize(500, 500)
window_accueil.config(background='#0F9DB0')
window_accueil.iconbitmap("download.ico")

#créer un frame
frame = Frame(window_accueil, bg='#0F9DB0')

#ajout image
lageur = 250
hauteur = 250
logo = PhotoImage(file="images.png").zoom(30).subsample(25)
canvas = Canvas(frame, width=lageur, height=hauteur, bg='#0F9DB0', bd=0, highlightthickness=0 )
canvas.create_image(lageur/2, hauteur/2, image=logo)
canvas.grid(row=0, column=0, sticky=W)

#ajout de texte  
titre = Label(frame, text="Mobile Banking", font=("Arial", 40), bg='#0F9DB0', fg='white')
titre.grid(row=0, column=1, sticky=W)

#ajout boutton
#connect = Button(frame, text="Se connecter", font=("Arial", 30), bg='white', fg='#0F9DB0' )
#connect.grid(row=2, column=1, sticky=W)

#seconde frame
second_frame = Frame(frame, bg='#0F9DB0')

num = Label(second_frame, text="Phone number", font=("Arial", 20), bg='#0F9DB0', fg='white')
num.pack()

num_input = Entry(second_frame, font=("Arial", 20), bg='#CCD6D3', fg='black')
num_input.pack()
print(num_input.get())


password = Label(second_frame, text="Password", font=("Arial", 20), bg='#0F9DB0', fg='white')
password.pack()

password_input = Entry(second_frame, show="*", font=("Arial", 20), bg='#CCD6D3', fg='black')
password_input.pack()

connect = Button(second_frame, text="Login", font=("Arial", 20), bg='white', fg='#0F9DB0' )
connect.pack(pady=25, fill=X)

second_frame.grid(row=1, column=1, sticky=W)

create = Button(window_accueil, text="New account", font=("Arial", 20), bg='white', fg='#0C8FD5', COMMAND= new_user.new_user)
create.pack(side=BOTTOM)

#afficher
frame.pack(expand=YES)
window_accueil.mainloop()