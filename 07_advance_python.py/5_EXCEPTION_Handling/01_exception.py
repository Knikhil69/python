# while True:
#     try:
#         a = int(input("Enter number 1: "))
#         b = int(input("Enter number 2: "))
#         print(f"The divsion is {a/b}")

#     except ValueError:
#         print("Please don't perform bad typecasts. ")    

#     except ZeroDivisionError:
#         print("Hey don't divide by zero")

#     except Exception as e:
#         print("Unknown error accured!", e)

# Raising Exception 
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
if b == 0:
    raise ValueError("Please don't divide by 0")
print(f"The division is {a/b}")


         
