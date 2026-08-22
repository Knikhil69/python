def sum(a , b):
    # a and b are local variable
    c = a + b
    z = 1 # it create a local varialbe called  z which is destroyed after this  function returns
    return c


def greet():
    z = 32 # Local variable
    print("hello")

z = 8 # z is a global variable
print(z)
print(sum(4,6))
print(z)