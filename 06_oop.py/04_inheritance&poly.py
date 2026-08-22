class Animal:
    location = "Australia"
    def __init__(self, name): # Parent class (Super class)
        self.name = name

    def speak(self):
        print("Speaking now.....!")

class Dog(Animal): # This is how inheritance is done in python "Child class"
    def speak(self):
        super().speak() # we are using speak function of the parent class
        print("Woof!")


# a = Animal("Dog") # 
# a.speak()
d = Dog(Animal("Bruno"))
d.speak()
# print(d.location)        