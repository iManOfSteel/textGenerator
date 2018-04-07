import re


delims = ['.', '!', '?']


def parse(line):
    for delim in delims:
        line = line.replace(delim, '.')
    sentences = filter(None, line.split('.'))
    result = []
    for sentence in sentences:
        sentence = re.sub(r'\W+', ' ', sentence)
        sentence = ''.join([i for i in sentence if not i.isdigit()])
        result.append(sentence.split())
    return result
