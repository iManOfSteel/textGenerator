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
    word_pattern = r'[a-zA-Zа-яА-Я]+'
    sentences = re.split(r'[.!?]+', line)
    result = []
    for sentence in sentences:
        result.append(re.findall(word_pattern, sentence))
    return result
