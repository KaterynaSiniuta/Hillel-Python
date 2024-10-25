fivenum = int(input("Введіть п'ятизначне число: "))

print((fivenum % 10) * 10000
      + (fivenum // 10 % 10) * 1000
      + (fivenum // 100 % 10) * 100
      + (fivenum // 1000 % 10) * 10
      + (fivenum // 10000))
