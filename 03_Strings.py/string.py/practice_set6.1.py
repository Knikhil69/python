'''Write a program that counts how many vowels are in a given string.
.'''


name = "Nikhil Kumar Saket"
vowels = "aeiouAEIOU"
count = 0

for chr in name:
    if(chr in vowels):
        count += 1
print(f"There are {count} vowels in this name.")        
