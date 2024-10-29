lst = [12, 3, 4, 10]

if len(lst) > 1:
    last_element = lst[-1]
    lst = [last_element] + lst[:-1]
print(lst)

lst = [1]
if len(lst) > 1:
    last_element = lst[-1]
    lst = [last_element] + lst[:-1]
print(lst)

lst = []
if len(lst) > 1:
    last_element = lst[-1]
    lst = [last_element] + lst[:-1]
print(lst)

lst = [12, 3, 4, 10, 8]
if len(lst) > 1:
    last_element = lst[-1]
    lst = [last_element] + lst[:-1]
print(lst)
