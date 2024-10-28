number1 = float(input("Введіть перше число: "))
operation = input("Введіть операцію (+, -, *, /): ")
number2 = float(input("Введіть друге число: "))

if operation == '+':
    print("Результат: ", number1 + number2)
elif operation == '-':
    print("Результат: ", number1 - number2)
elif operation == '*':
    print("Результат: ", number1 * number2)
elif operation == '/':
    if number2 == 0:
        print("Помилка: Дільник не може дорівнювати нулю")
    else:
        print("Результат: ", number1 / number2)
else:
    print("Невідома операція")
