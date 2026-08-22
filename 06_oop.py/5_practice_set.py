'''3. Simple Inheritance
Create a base class Animal with a method sound() that prints "Some sound".
Create a derived class Dog that overrides sound() to print "Bark!".
Create an object of Dog and call sound()
'''

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal): # Inheriting from Animal
    def sound(self):  # Overriding the inherited method
        print("Bark!")

d = Dog() 
d.sound()