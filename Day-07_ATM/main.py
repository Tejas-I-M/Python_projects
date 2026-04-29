class ATM:
    def __init__(self,balance,pin):
        self.__balance = balance
        self.__pin = pin
    def password(self,check):
        return self.__pin == check
    def deposit(self,amount):
        if amount<=0:
            print("invalid amount!")
            return
        self.__balance+= amount
        print("deposted amount: ",amount)
    def withdraw(self,amount):
        if amount>self.__balance:
            print("insufficient balance")
            return
        self.__balance-=amount
        print("amount withdrawn: ",amount)
    def show_balance(self):
        print("balance: ",self.__balance)
atm = ATM(5000,1234)

pin_check = int(input("enter the pin: "))
if atm.password(pin_check):
    while True:
        print("\n1. deposit \n2.withdraw \n3.show balance \n4.exit")
        selected = input("enter the option: ")
        if selected=="1":
            amt = int(input("enter the amount:"))       
            atm.deposit(amt)
        elif selected=="2":
            amt = int(input("enter the amount: "))
            atm.withdraw(amt)
        elif selected =="3":
            atm.show_balance()
        elif selected =="4":
            break
        else:
            print("invalid option!!")
else:
    print("wrong pin!")
        