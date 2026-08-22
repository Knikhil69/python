'''Using Decorators with Arguments
Decorators themselves can also accept arguments. This requires another level of nesting: an outer function that takes the decorator's arguments and returns the actual decorator function'''

def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
             func(a)
        return wrapper
    return decorator 

@repeat(10)
def greet(name):
    print(f"Hello, {name}!")
greet("NIKHIL")
