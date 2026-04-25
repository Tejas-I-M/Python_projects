class Student:
    def __init__(self,name, roll_no):
        self.name =name
        self.roll_no = roll_no
        self.__marks =[]
    def add_marks(self,marks):
        if marks < 0 or marks > 100:
            print("Invalid marks. Marks should be between 0 and 100.")
            return
        self.__marks.append(marks)
    def calculate_average(self):
        if len(self.__marks) ==0:
            return 0
        return sum(self.__marks)/len(self.__marks)
    def get_grade(self):
        average = self.calculate_average()
        if average >=90:
            return "A"
        elif average >=80:
            return "B"
        elif average >=70:
            return "C"
        else:
            return "D"
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.__marks}")
        print(f"Average Marks: {self.calculate_average():.2f} %")
        print(f"Grade: {self.get_grade()}")
student1 = Student("Tejas",420)
student1.add_marks(-100)
student1.display()