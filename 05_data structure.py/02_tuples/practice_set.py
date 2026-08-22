'''3. Tuples and Operations on Tuples
Create a tuple coordinates = (10, 20) and print both elements.
Try to modify the tuple by setting coordinates[0] = 50 — note what happens.
Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.
'''
coordinates = (10, 20)
print(coordinates[0])
print(coordinates[1])

# coordinates[0] = 50  # tuple, object does not support item assignment
# print(coordinates)

num = list(coordinates)
num[0] = 50
coordinates = tuple(num)
print(coordinates)
