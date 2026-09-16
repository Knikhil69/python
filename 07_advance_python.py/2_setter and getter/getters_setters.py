class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self): # getter 
        l = self.name.split(" ")
        return l[0]

    @first_name.setter
    def first_name(self, first): # setter
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name


e = Employee("NIKHIL Kr.", 85732)
# print(e.first_name())
# e.set_first_name("John")
# print(e.name)

print(e.first_name) # getter
e.first_name = "John" # setter
print(e.name) 



      