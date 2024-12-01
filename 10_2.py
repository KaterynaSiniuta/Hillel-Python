import re


def first_word(text):
    """ Пошук першого слова """
    text = text.lstrip("., ")
    word = re.match(r"[a-zA-Z0-9']+", text)
    return word.group(0) if word else ""


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'

print('OK')
