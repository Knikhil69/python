'''Take a user input string and check if it is a palindrome (same forwards and backwards).'''

string = input("Enter the word: ") 

if (string == string[::-1]):
    print("The string is a palindrome. ")
else:
    print("The string is not a palindome. ")    