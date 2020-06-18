# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:56:08 2020

@author: donny
"""

from tkinter import *
from interface import *

#créer une première fenêtre 

new_user = Tk()

#personnaliser la fenêtre
new_user.title("Afriland Bank : Create new account")
new_user.geometry("800x680")
new_user.minsize(580, 580)
new_user.config(background='#0F9DB0')
new_user.iconbitmap("download.ico")

welcome = Label(new_user, text="Create your new account", font=("Arial", 20), bg='#0F9DB0', fg='white')
welcome.pack()

#créer un frame
frame = Frame(new_user, bg='#0F9DB0')

name = Label(frame, text="Name", font=("Arial", 20), bg='#0F9DB0', fg='white')
name.pack()

name_input = Entry(frame, font=("Arial", 20), bg='#CCD6D3', fg='white')
name_input.pack()

surname = Label(frame, text="Surname", font=("Arial", 20), bg='#0F9DB0', fg='white')
surname.pack()

surname_input = Entry(frame, font=("Arial", 20), bg='#CCD6D3', fg='white')
surname_input.pack()

age = Label(frame, text="Age", font=("Arial", 20), bg='#0F9DB0', fg='white')
age.pack()

age_input = Entry(frame, font=("Arial", 20), bg='#CCD6D3', fg='white')
age_input.pack()

mail = Label(frame, text="Email", font=("Arial", 20), bg='#0F9DB0', fg='white')
mail.pack()

mail_input = Entry(frame, font=("Arial", 20), bg='#CCD6D3', fg='white')
mail_input.pack()

address = Label(frame, text="Address", font=("Arial", 20), bg='#0F9DB0', fg='white')
address.pack()

address_input = Entry(frame, font=("Arial", 20), bg='#CCD6D3', fg='white')
address_input.pack()

code = Label(frame, text="Postal Code", font=("Arial", 20), bg='#0F9DB0', fg='white')
code.pack()

code_input = Entry(frame, font=("Arial", 20), bg='#CCD6D3', fg='white')
code_input.pack()

city = Label(frame, text="City", font=("Arial", 20), bg='#0F9DB0', fg='white')
city.pack()

city_input = Entry(frame, font=("Arial", 20), bg='#CCD6D3', fg='white')
city_input.pack()


nex = Button(new_user, text="Next", font=("Arial", 20), bg='white', fg='#0C8FD5' )
nex.pack(side=BOTTOM)

frame.pack(expand=YES)
new_user.mainloop()