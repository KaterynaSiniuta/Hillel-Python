fournum = int(input("Введіть 4-х значне число: "))

tysyacha = fournum // 1000
sotnya = (fournum // 100) % 10
desyatok = (fournum // 10) % 10
odyn = fournum % 10

print(tysyacha)
print(sotnya)
print(desyatok)
print(odyn)

