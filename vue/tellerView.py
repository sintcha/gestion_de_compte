

from tkinter import  Toplevel, Label, Entry, Button

class TellerView(Toplevel):  # View 2
    def __init__(self, master):
        Toplevel.__init__(self, master)

        Label(self, text='Montant').pack(side='left')
        self.amount = Entry(self, width=8)
        self.amount.pack(side='left')

        self.btn_deposit = Button(self, text='Depot', width=8)
        self.btn_deposit.pack(side='left')

        self.btn_withdrawal = Button(self, text='Retrait', width=8)
        self.btn_withdrawal.pack(side='left')
