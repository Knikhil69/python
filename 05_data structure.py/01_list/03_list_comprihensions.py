# Create a list  containing the tabel of 5.

# a = 5
# table =[]
# for i in range(1, 11):
#     table.append(5*i)
# print(table)   

table = [5*i for i in range(1, 11)]# list comprihensions
print(table)



my_list = [1, 2, 3, 4, 5]
my_list.append(4)
my_list.insert(1, 99) 
my_list.remove(2)
my_list.pop() 
my_list.reverse() 
my_list.sort() 
print(my_list)
