'''Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.'''
def multiply(a,b):
    '''
    Multiply two numbers.
    perimeters:
       a(int or float): The first number.
       b(int or float): The second number.
       return:
          int or float: The products of a and b.

    '''
    if b == 0:
        return 0
    return a*b

print(multiply(4,5))
print(multiply(3,0))
help(multiply)

   