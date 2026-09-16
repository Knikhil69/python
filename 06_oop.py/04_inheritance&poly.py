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




# inheritance in python 
class Animal:  # Parent class or (Super class)
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound....")

class Dog(Animal): # Dog inherit from animal 
    def speak(self): # Override  the speak method 
        super().speak() # use to call the method from the parent class and it is use inside the child class 
        print(f"{self.name} is  a dog and it is saying  Woof!")

class Cat(Animal): # this is also inherit from Animal
    def speak(self): # overrride the speak method 
        super().speak() 
        print(f"{self.name} is a cat and it is  saying Meow!")

# create an object
my_dog = Dog("Rover")
my_cat = Cat("Fluffy")

# They both have a name attribute (inherited form Animal)
print(my_dog.name)
print(my_cat.name)

# The both have speak method but the behaves differently 
my_dog.speak()
my_cat.speak()


