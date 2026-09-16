'''Use filter() to get only even numbers from [10, 11, 12, 13, 14].'''
even_numbers = list(filter(lambda x: x % 2 == 0, [10, 11, 12, 13, 14]))
print(even_numbers)
