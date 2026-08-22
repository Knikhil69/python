a = int(input("Enter your lucky number between 1 to 10 :"))


match a:
    case 1:
        print("Hey you are  won car")
    case 5:
        print("Hey you are won watch")
    case 9:
        print("Hey you are won I phone")
    case _:
        print("Better luck next time")   


'''
Match-case is a new feature introduced in Python 3.10 for pattern matching.
It simplifies complex conditional logic.
'''