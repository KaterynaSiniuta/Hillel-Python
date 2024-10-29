lst = [1, 2, 3, 4, 5, 6]

if lst is []:
    result = [[], []]
else:
    mid = (len(lst) + 1) // 2
    result = [lst[:mid], lst[mid:]]
print(result)
