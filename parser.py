import re


def parse(line):
    delimiters = ['.', '!', '?']
    for delimiter in delimiters:
        line = line.replace(delimiter, '.')
    sentences = filter(None, line.split('.'))
    result = []
    for sentence in sentences:
        sentence = re.sub(r'[^a-zA-Zа-яА-Я]', ' ', sentence)
        result.append(sentence.split())
    return result
