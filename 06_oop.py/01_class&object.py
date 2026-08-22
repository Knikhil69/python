# class: calss is a blueprint or a templete . Example from for an exam that contains name , age , father's name etc .
# Object: specifice instence created from the templete (class). for example from which contain the for John Doe.


class Employee:
    company = "HP"
    def get_sallary(self):# self is important here because self is a way to reference the object of the class which is being created.
        return 34000
    
e1 = Employee() # A object of class Emmployee is created here.
print(e1.get_sallary()) # Employee e's get sallary mathod is called.
print(e1.company)

e2 = Employee()
print(e2.get_sallary())
print(e2.company)



'''Interview Question

Q: Why do we use self?

Answer:

self refers to the current object.
It allows each object to store and access its own data.
Without self, all objects would not have separate attributes.
'''