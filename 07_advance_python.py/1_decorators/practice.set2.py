'''Write a decorator timer that calculates how long a function takes to execute. Test it with a function that sums numbers from 1 to 1,000,000.'''

from time import time # import time 

def timer(func):
    def wrapper(n):
        t1 = time() # initial time
        result = func(n)
        t2 = time() # final time
        # print(t2 - t1)
        print(f"Execution time: {t2 - t1:.6f} seconds") # The :.6f limits the output to six decimal places.
        return result
    return wrapper
@timer

def sum_1m(n):
    total = 0
    for i in range(1 , n+1):
        total += i
    return total
a = sum_1m(1000000) # output: 500000500000
print(a)  

'''don't use sum as variable because sum is already a built in function. '''


