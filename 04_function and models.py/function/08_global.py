def sum(a, b):
    print("Hey I am summing")
    c = a + b 
    global z # Please modify global z
    z = 0 # this will refer to global vairiable and not create a local vairiable
    return c



z = 3
print(sum(3, 12))
print(z)