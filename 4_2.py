lst = [1, 3, 5]

if len(lst) == 0:
    result = 0
else:
    total_sum = 0
    index = 0

    while index < len(lst):
        total_sum = total_sum + lst[index]
        index = index + 2

    result = total_sum * lst[-1]

print(result)
