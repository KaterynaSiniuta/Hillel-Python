def common_elements():
    numbers_divisible_by_3 = {x for x in range(100) if x % 3 == 0}
    numbers_divisible_by_5 = {x for x in range(100) if x % 5 == 0}

    return numbers_divisible_by_3 & numbers_divisible_by_5


# Тест
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}

print('ОК')
