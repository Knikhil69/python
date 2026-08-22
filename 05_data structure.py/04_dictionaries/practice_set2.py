'''Create a dictionary of three friends and their phone numbers. Use:

keys() to get all names
values() to get all numbers
items() to loop over key-value pairs and print them'''

friends = {"Nik":9438762334, "maru":963874715, "giggi":7658943246}
print(friends.keys())

print(friends.values())

# print(friends.items())
for name, number in friends.items(): # This is called tuple unpacking
    print(f"{name} : {number}") 

