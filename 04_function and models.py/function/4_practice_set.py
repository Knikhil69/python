'''Write a recursive function factorial(n) that returns the factorial of a number.'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))
print(factorial(0))

'''factorial(5)
= 5 * factorial(4)
= 5 * (4 * factorial(3))
= 5 * (4 * (3 * factorial(2)))
= 5 * (4 * (3 * (2 * factorial(1))))
= 5 * (4 * (3 * (2 * 1)))
= 5 * (4 * (3 * 2))
= 5 * (4 * 6)
= 5 * 24
= 120'''

'''Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.
'''
def sum_of_digit( n ):
    if n == 0:
        return 0
    return (n % 10 + sum_of_digit(int(n / 10)))

# Driven code to check above
num = 12345
result = sum_of_digit(num)
print(result)

'''It does two things:

n % 10 → gets the last digit of the number.
sum_of_digit(n // 10) → recursively finds the sum of the remaining digits.
Finally, it adds them together.'''



'''sum_of_digit(12345)
= 5 + sum_of_digit(1234)
= 5 + 4 + sum_of_digit(123)
= 5 + 4 + 3 + sum_of_digit(12)
= 5 + 4 + 3 + 2 + sum_of_digit(1)
= 5 + 4 + 3 + 2 + 1 + sum_of_digit(0)
= 5 + 4 + 3 + 2 + 1 + 0
= 15'''