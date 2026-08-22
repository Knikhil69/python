'''Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.'''
# def fib(n):
#     if n == 0 or n == 1:
#         return 1
#     return fib(n-2) + fib(n-1)
# print(fib(6))

def fibonacci(n):
    def fib(k):
        if k <= 1:
            return k
        return fib(k-2) + fib(k-1)
    for i in range(n):
        print(fib(i), end=" ")

fibonacci(10)


'''Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.'''
def safe_divide(a,b):
    if b == 0:
        return "Can't Devide"
    return a/b
print(safe_divide(12,4))
print(safe_divide(12,0))




'''Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.'''

import my_utils
print(my_utils.is_even(34))

result = (my_utils.is_even(13))
print(result)
