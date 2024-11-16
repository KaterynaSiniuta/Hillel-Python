number = int(input("Введіть ціле число: "))

while number > 9:
    product = 1
    while number > 0:
        product *= number % 10
        number //= 10
    number = product

print("Результат:", number)
