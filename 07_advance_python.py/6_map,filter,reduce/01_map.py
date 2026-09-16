# the map() function applies a given function to each item of an iterable and result an iterator that yields the result.
number = [1,2,3,45,6,21]

def Square(x):
    return x*x

new = list(map(Square, number))
print(new)

# by using lamda function 
number = [2,4,5,67,90]
new = list(map(lambda x:x*x , number))
print(new)
