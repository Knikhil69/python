# **Kwargs: Allow  you to pass a variable number of keyword arguments.

def marks(**kwargs):
    # kwargs is a dictionary with all the key value pairs which were passed to marks.

    for  item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(shubham = 34, Vikas = 45, Jack=67, Rohan = 90, Marie = 89)
    

