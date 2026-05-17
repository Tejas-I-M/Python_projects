import os
import json

class ExpenseTracker:
    def __init__(self,file_name = "expenses.json"):
        self.file_name = file_name
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if not os.path.exists(self.file_name):
            print("no file found")
            return []
        with open(self.file_name,'r') as f:
            return json.load(f)
    def save_expenses(self):
        with open(self.file_name,'w') as f:
            json.dump(self.expenses,f,indent=4)
    def add_expense(self,title,amount):
        if amount <0:
            print("amount cannot be negative")
            return
        exp = {"title":title,"amount":amount}
        self.expenses.append(exp)
        self.save_expenses()
        print("expense added")
    def view_expenses(self):
        if not self.expenses:
            print("no expenses found")
            return
        for exp in self.expenses:
            print(f"-{exp['title']}: {exp['amount']}")
    def total_expense(self):
        total = sum(exp['amount'] for exp in self.expenses)
        print("total expense: ",total)
tracker = ExpenseTracker()
while True:
    print("\n1.add 2.view 3.total 4.exit")
    choice = input("choose: ")
    if choice =="1":
        title = input("enter title: ")
        amount = int(input("enter the amount: "))
        tracker.add_expense(title,amount)
    elif choice=="2":
        tracker.view_expenses()
    elif choice =="3":
        tracker.total_expense()
    elif choice=="4":
        break
    else:
        print("invalid choice")
