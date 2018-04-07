"""Parses text."""
import re


def parse(line):
    """Removes all non-alphabetic characters form the string and
    split text on sentences.

    :param line: str
        Text to parse.
    :return: list
        List of parsed sentences. Each sentence - a word list.
    """
    delimiters = ['.', '!', '?']
    for delimiter in delimiters:
        line = line.replace(delimiter, '.')
    sentences = filter(None, line.split('.'))
    result = []
    for sentence in sentences:
        sentence = re.sub(r'[^a-zA-Zа-яА-Я]', ' ', sentence)
        result.append(sentence.split())
    return result
