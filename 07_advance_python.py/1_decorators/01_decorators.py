# Ddecorator is a function that takes a function, it creates a new function inside its body (wrappper). Then it retutns that new function.

def decorator(func):
    def wrapper():
        print("I am about to execute a function...")
        func()
        print("I have execute this function....")
    return wrapper()

@decorator
def say_hello():
    print("Hello")