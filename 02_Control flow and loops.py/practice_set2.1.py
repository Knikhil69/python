'''Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.'''

a = int(input("Enter your a number betbeen 1 to 7:"))
match a :
    case 1:
        print("Today is Monday.")
    case 2:
        print("Today is Tuesday.")
    case 3:
        print("Today is Wednesday.")
    case 4:
        print("Today is Thursday.")
    case 5:
        print("Today is Friday.")
    case 6:
        print("Today is Saturday.")
    case 7:
        print("Today is Sunday.")
    case _:
        print("Invalid response try  again.")
                            


