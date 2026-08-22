'''You can apply multiple decorators to a single function. Decorators are applied from bottom to top (or, equivalently, from the innermost to the outermost).'''
def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper
 
def exclaim(func):
    def wrapper():
        return func() + "!!!"
    return wrapper
 
@uppercase
@exclaim
def greet():
    return "hello"
 
print(greet())