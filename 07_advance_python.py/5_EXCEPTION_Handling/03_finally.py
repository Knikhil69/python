# using finally
def divide(a, b):
    try:
        c = a/b
        print(c)
        return c

    except Exception as e:
        print(e)
        return None

    # This is always executed no matter if try completey executed or not
    finally:
        print("This is always Executed")

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
divide(a,b)


