class Employee:

    def __init__(self, name, salary):
        self.nameTag = name
        self.salaryTag = salary

    def printName(self):
        print(f"The name of employee is:{self.nameTag}")

    def printSal(self):
        print(f"Salary of {self.nameTag} is {self.salaryTag}")


emp_Praveen = Employee("Praveen", 30000)
emp_Praveen.printName()
emp_Praveen.printSal()
