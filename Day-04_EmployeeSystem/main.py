class Employee:
    total_employees=0
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        if salary<10000:
            print("Salary must be at least 10000")
            self.salary=10000
        else:            
            self.salary=salary

        Employee.total_employees+=1
    def update_salary(self,new_salary):
        if new_salary<10000:
            print("Salary must be at least 10000")
            return
        self.salary=new_salary
        print(f"Salary updated to {self.salary}")

    def apply_bonus(self,percent):
        if percent<0:
            print("bonus cannot be negative")
            return
        bonus = self.salary*percent/100
        self.salary +=bonus
        print(f"Bonus: {bonus},New salary: {self.salary}")
    def display(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}") 
        print(f"Salary: {self.salary}")
    @staticmethod
    def company_policy():
        print("Must work 8 hrs")

emp1 = Employee('tejas',1,10000)
emp2 = Employee("jett",1,1000000)
emp1.display()
emp1.apply_bonus(10)
emp1.display()

print()

emp2.display()

print()
print('Total Employees:',Employee.total_employees)
Employee.company_policy()
           