'''Write a lambda function that adds two numbers and test it.'''
add = lambda x,y: x + y
print(add(4,6))

'''Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares'''
numbers = [1, 2, 3 ,4, 5] 
squares = list(map(lambda x: x**2, numbers))
print(squares)




'''challange question  and map(), filter() important for interviews.'''
numbers = [2, 4, 6]

result = list(map(lambda x: x + 5, numbers))

print(result)

'''and one more filter()'''
numbers = [1, 2, 3, 4]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)
'''Hint: Unlike map(), which transforms every element, filter() keeps only the elements for which the condition is True.'''
