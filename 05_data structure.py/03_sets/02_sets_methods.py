s = {34, 23, 1, 3, 22}

print(s)
s.add(56)
s.add(990)
s.remove(23)
#s.remove(5768) # showing error because this element is not present in the sets.
s.discard(4999) # not showing error
s.pop()

print(s)