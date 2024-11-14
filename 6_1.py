import string

input_string = input("Введіть дві літери через дефіс: ")

letter1, letter2 = input_string.split('-')

letters = string.ascii_letters

start_index = letters.index(letter1)
end_index = letters.index(letter2)

if start_index > end_index:
    start_index, end_index = end_index, start_index

print(letters[start_index:end_index + 1])
