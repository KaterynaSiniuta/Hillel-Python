input_string = input("Введіть рядок: ")

punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~'''
hashtag = '#' + input_string.title().replace(' ', '').replace(punctuation, '')

hashtag = hashtag[:140]

print(hashtag)
