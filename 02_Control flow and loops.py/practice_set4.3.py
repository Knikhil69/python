'''Use a while loop to reverse a given number (e.g., 123 → 321).'''
# num = 87654321

# print(int(str(num)[:: -1])) #REVERSE A GIVEN NUMBER

num = 1234
reversed_number = 0

while (num != 0):
    digit = num % 10
    reversed_number = reversed_number * 10 + digit
    num = num // 10

print("Reversed Number: ",reversed_number)

'''
num = 1234
reversed_number = 0

| Iteration | `num` | `digit` | `reversed_number` |
| --------: | ----: | ------: | ----------------: |
|         1 |  1234 |       4 |                 4 |
|         2 |   123 |       3 |                43 |
|         3 |    12 |       2 |               432 |
|         4 |     1 |       1 |              4321 |

Loop stops when num becomes 0.

Output:

4321
'''