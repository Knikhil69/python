# the filter() function constructs an iterator from elements of an iterable for which a function returns True.
def is_greater_then_9(x):
    if x > 9:
        return True
    else:
        return False

a = [1,3,5,234,67,89,9,8,7,45,78,59,34]
new = list(filter(is_greater_then_9, a))
print(new)

# by using lambda() function
a = [2,3,56,7,89,90,54,73,21,5,7,8,9]
new = list(filter(lambda x: x>9, a))
print(new)