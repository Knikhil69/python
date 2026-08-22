'''Write a program that merges two dictionaries into one.'''
a = {"Name":"NIkhil", "Grade":"A+"}
b = {"Subjects":5, "Branch":"AIML"}

merge_dic = {**a, **b}
print(merge_dic)



'''second way '''
a = {"Name": "Nikhil", "Grade": "A+"}
b = {"Subjects": 5, "Branch": "AIML"}

a.update(b)

print(a) 

'''Difference:

{**a, **b} creates a new dictionary.
a.update(b) modifies the existing dictionary a.'''