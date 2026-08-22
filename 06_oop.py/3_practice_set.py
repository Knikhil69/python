'''
2. Constructor and Attributes
Create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes.
Create an object and print the person’s name and age.'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self): # this is not ask in question but I do my self for better understanding. 
        print(f"The person's name is {self.name} and their age is {self.age}.") 

p1 = Person("John" ,32)
print(p1.name)
print(p1.age)


p1.get_info()