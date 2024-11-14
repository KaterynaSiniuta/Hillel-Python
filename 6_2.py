seconds = int(input("Введіть кількість секунд (0 - 8640000): "))

days, remainder = divmod(seconds, 24 * 60 * 60)
hours, remainder = divmod(remainder, 60 * 60)
minutes, seconds = divmod(remainder, 60)

if days % 10 == 1 and days != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and not (12 <= days <= 14):
    day_word = "дні"
else:
    day_word = "днів"

print(f"{days} {day_word} {str(hours).zfill(2)}:{str(minutes).zfill(2)}"
      f":{str(seconds).zfill(2)}")
