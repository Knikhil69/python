'''Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".'''

def full_name(first, last):
    # return first +" "+ last
    return f"{first} {last}"

print(full_name("Nikhil","Saket")) # function calling





'''Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

Both length and width
Only length (use default width)
'''
def calculate_area(length, width=10):
    return length * width
print(calculate_area(12,8))
print(calculate_area(15)) # default width 


print(calculate_area(2,20))
print(calculate_area(width=8, length=2))  # arguments 

