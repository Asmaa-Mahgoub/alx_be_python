
class BankAccount:
    def __init__(self, account_balance:float):
        self.account_balance = account_balance
        self.initial_balance = 0

    def deposit(self, amount):
        self.account_balance += amount
        #print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            #print(f"Withdraw: ${amount}")
            return True
            
        else:
            #print("Insufficient funds")
            return False

    def display_balance(self):
        print(f"Current Balance: ${float(self.account_balance)}")

#CIB= BankAccount(43000)
#CIB.deposit(67)
#CIB.withdraw(50)
#CIB.withdraw(100000) 
#CIB.display_balance()





   

