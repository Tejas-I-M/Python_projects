
class BankAccount:
    def __init__(self,account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number= account_number
        self.balance = balance
        self.transactions = []

    def deposit(self,amount):
        if amount <=0:
            print("Deposit amount must be positive.")
            return
        self.balance+=amount
        self.transactions.append(f"Deposted:{amount}")
        print('Deposited: ',amount)
        print("New Balance: ",self.balance)
    def withdraw(self,amount):
        if amount <=0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance-=amount
        self.transactions.append(f"Withdrawn: {amount}")
        print("withdrawn: ",amount)
        print("New Balance: ",self.balance)
    def display(self):
        print("Account Holder: ",self.account_holder)
        print("Account Number: ",self.account_number)
        print("Balance: ",self.balance)
    def show_transactions(self):
        for t in self.transactions:
            print("-",t)

account1= BankAccount("Tejas", 1, 1000)
print()
account1.display()
print()
account1.deposit(500000)
print()
account1.display()
print()
account1.withdraw(200000)
print()
account1.show_transactions()
