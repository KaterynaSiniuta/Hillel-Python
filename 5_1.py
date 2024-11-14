name = input("Введіть ім'я змінної: ")

is_valid = True

keywords = [
    "False", "None", "True", "and", "as", "assert", "async", "await",
    "break", "class", "continue", "def", "del", "elif", "else", "except",
    "finally", "for", "from", "global", "if", "import", "in", "is", "lambda",
    "nonlocal", "not", "or", "pass", "raise", "return",
    "try", "while", "with", "yield"
]

if name in keywords:
    is_valid = False
elif name == "_":
    is_valid = True
elif name.count("_") == len(name) and len(name) > 1:
    is_valid = False
elif name[0] in "0123456789":
    is_valid = False
else:
    for char in name:
        if char not in "abcdefghijklmnopqrstuvwxyz_0123456789":
            is_valid = False

print(is_valid)
