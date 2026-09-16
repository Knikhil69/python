# combined of args and kwargs

def func1(*args , **kwargs): # alwayes write args first and the kwargs
    print(args)
    print(kwargs)

func1(3,5,67,8,989,78,9,0, Jack = 35, Jill = 38, Marie = 43)
