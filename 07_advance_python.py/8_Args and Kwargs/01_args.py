# *args: allow you to pass a varialbe number of positional arguments.

def sum(*args):
    # args will be a tuple of all the value pasasd to sum.
    total = 0
    for item in args:
        total += item
    return total
print(sum(345,567,898,56,4))

