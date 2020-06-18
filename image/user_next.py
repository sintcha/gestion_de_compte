# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 16:57:19 2020

@author: donny
"""

from tkinter import *
#from interface import *
from new_user import *


#créer une première fenêtre 

user_next = Tk()

#personnaliser la fenêtre
user_next.title("Afriland Bank : Create account")
user_next.geometry("720x580")
user_next.minsize(500, 500)
user_next.config(background='#0F9DB0')
user_next.iconbitmap("download.ico")

welcome = Label(user_next, text="Create your identifiers", font=("Arial", 20), bg='#0F9DB0', fg='white')
welcome.pack()

#créer un frame
frame = Frame(user_next, bg='#0F9DB0')

phone = Label(frame, text="Phone number", font=("Arial", 20), bg='#0F9DB0', fg='white')
phone.pack()

phone_input = Entry(frame, font=("Arial", 20), bg='#CCD6D3', fg='white')
phone_input.pack()

password = Label(frame, text="Password", font=("Arial", 20), bg='#0F9DB0', fg='white')
password.pack()

password_input = Entry(frame, font=("Arial", 20), bg='#CCD6D3', fg='white')
password_input.pack()

passwordc = Label(frame, text="Confirm your password", font=("Arial", 20), bg='#0F9DB0', fg='white')
passwordc.pack()

passwordc_input = Entry(frame, font=("Arial", 20), bg='#CCD6D3', fg='white')
passwordc_input.pack()

finish = Button(user_next, text="finished", font=("Arial", 20), bg='white', fg='#0C8FD5' )
finish.pack(side=BOTTOM)

frame.pack(expand=YES)
user_next.mainloop()