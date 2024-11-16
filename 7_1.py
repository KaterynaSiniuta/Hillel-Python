def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"


# Тест 1
result1 = say_hi("Alex", 32)
assert result1 == "Hi. My name is Alex and I'm 32 years old", 'Test1'

# Тест 2
result2 = say_hi("Frank", 68)
assert result2 == "Hi. My name is Frank and I'm 68 years old", 'Test2'

print(result1)
print(result2)
print('ОК')
