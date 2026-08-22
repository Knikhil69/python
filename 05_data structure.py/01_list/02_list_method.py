marks = [4, 3, 5, 8, 21, 34, 56]
extra_marks = [87, 89, 90]
print(marks)
marks.append(69) # This will change the original list.
marks.extend(extra_marks)
marks.pop()
print(marks)