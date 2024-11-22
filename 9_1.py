def popular_words(text: str, words: list) -> dict:
    """
    Counts the occurrences of specified words in a given text.

    Arguments:
    text (str): The text to analyze.
    words (list): A list of words to count in the text.

    Returns:
    dict: A dictionary where the keys are the words from the `words` list,
          and the values are the number of times each word appears in the text.
    """
    # Convert the text to lowercase and split it into words
    word_list = text.lower().split()

    # Create a dictionary of results
    result = {word: word_list.count(word) for word in words}

    return result


# Function test
assert popular_words(
    '''When I was One I had just begun When I was Two I was nearly new''',
    ['i', 'was', 'three', 'near']
) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'

print('OK')
