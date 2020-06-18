

from tkinter import  Toplevel, Label, Entry

class BankView(Toplevel):  # View 1
    def __init__(self, master):
        Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)

        Label(self, text='Solde').pack(side='left')
        self.balance = Entry(self, width=8)
        self.balance.pack(side='left')

    def set_balance(self, amount):
        self.balance.delete(0, 'end')
        self.balance.insert('end', str(amount))


