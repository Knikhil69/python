'''Write a function greet() that prints "Hello, Python Learner!" when called'''
# def greet():
#     return f"Hello, Python Learner!"
# print(greet())

'''OR'''
def greet():
    print("Hello, Python Learner!")

greet() # function calling



''''Write a function square(num) that returns the square of a given number. Test it with different numbers.'''

# def square(num):
#     d = num**2
#     return d
# num_1 = square(12)
# num_2 = square(32)
# num_3 = square(40)
# num_4 = square(10)

# print(num_1)
# print(num_2)
# print(num_3)
# print(num_4)

''' this is the clean version of the code and (d) is not neccessary '''
def square(num):
    return num ** 2

print(square(12))
print(square(32))
print(square(40))
print(square(10))