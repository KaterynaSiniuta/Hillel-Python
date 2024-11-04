numbers = [9, 0, 7, 31, 0, 45, 0, 0, 96, 0]

index = 0

for num in numbers:
    if num != 0:
        numbers[index] = num
        index += 1

while index < len(numbers):
    numbers[index] = 0
    index += 1

print(numbers)
