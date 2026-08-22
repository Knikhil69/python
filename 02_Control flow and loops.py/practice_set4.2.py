'''Write a program that keeps asking the user to enter a password until they enter the correct one.'''


password = "RKJF876HGU"
entered_pass = input(" Enter password")

while (entered_pass != password):
    entered_pass = input("Wrong password! try again, enter password:")
print("You are successful logged in:")    
    