from vue.transaction import Transaction


class Account:  # The Model
    def __init__(self):
        self.transaction = Transaction()

    def deposit(self, value):
        self.transaction.set(self.transaction.get() + value)

    def withdrawal(self, value):
        self.transaction.set(self.transaction.get() - value)