class Employee:
    def __init__(self, salary, name, bond):
        self.salary = salary # Create an instence atribute of name salary and assign it with salary
        self.name = name 
        self.bond = bond

    def get_info(self):
        print(f"The name of employee is {self.name}. The salary is {self.salary}. The bond is {self.bond} years.")

e1 = Employee(350000, "John Doe" ,5)
e1.get_info()

