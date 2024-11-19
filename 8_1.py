def add_one(some_list):
    if not some_list:
        raise ValueError("Вхідний список не може бути порожнім.")

    if not all(isinstance(digit, int) and 0 <= digit <= 9
               for digit in some_list):
        raise ValueError("Список має містити лише цілі числа від 0 до 9.")

    number_str = "".join(str(digit) for digit in some_list)
    number = int(number_str) + 1

    return [int(digit) for digit in str(number)]


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'

print("ОК")
