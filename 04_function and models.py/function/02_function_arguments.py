'''Function takes parameters and retrurn value'''
def add(a, b, plus=0):

    x = a + b + plus
    return x
c = add(3, 4, 5)
print(c)

c1 = add(b=4, a=3)
print(c1)