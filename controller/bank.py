
from tkinter import  Tk
from model.account import Account
from vue.bankView import BankView
from vue.tellerView import TellerView


class Bank(Tk):  # The Controller
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.withdraw()

        self.account = Account()
        self.account.transaction.add_callback(self.update_account)

        self.bank_view = BankView(self)
        self.bank_view.title('Banque')

        self.teller_view = TellerView(self.bank_view)
        self.teller_view.title('Client')

        self.teller_view.btn_deposit.config(command=self.make_deposit)
        self.teller_view.btn_withdrawal.config(command=self.make_withdrawal)

        self.update_account(self.account.transaction.get())

    def make_deposit(self):
        self.account.deposit(int(self.teller_view.amount.get()))

    def make_withdrawal(self):
        self.account.withdrawal(int(self.teller_view.amount.get()))

    def update_account(self, amount):
        self.bank_view.set_balance(amount)



