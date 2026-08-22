class Employee:
    company = "Asus" # This is class attribute

    def __init__(self, salary, name, bond, company):
        self.salary = salary # Create an instence atribute of name salary and assign it with salary
        self.name = name 
        self.bond = bond
        self.company = company

e1 = Employee(30000, "Jhon", 4, "Tesla")
print(e1.company) # will always print instance attribute whenever present.
print(Employee.company) # This wil always print the class attribute.

# object introspection
print(dir(e1))
