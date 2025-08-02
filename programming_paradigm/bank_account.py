
class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.initial_balance = 0

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${self.account_balance}")

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
            print(f"Withdraw: ${self.account_balance}")
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")

CIB= BankAccount(95000)
CIB.deposit(8000)
CIB.withdraw(60000)
CIB.display_balance()





   

