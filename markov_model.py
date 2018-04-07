"""Markov chain implementation."""
import random
import pickle


class Vertex(dict):
    """Contains frequency with which words occur after given word tuple.
    Each Vertex corresponds to a specific word tuple in the Model.
    """
    def __init__(self):
        super().__init__()
        self.__keys_number = 0

    def add_key(self, key):
        """Adds word.

        :param key: str
            Word to add.
        """
        if key in self:
            self[key] += 1
        else:
            self[key] = 1
        self.__keys_number += 1

    def get_random_word(self):
        """Returns next word, based on the frequencies,
         with which words occur.
         """
        rand = random.randint(0, self.__keys_number - 1)
        current_sum = 0
        keys_list = self.keys()
        for key in keys_list:
            current_sum += self[key]
            if current_sum > rand:
                return key


class Model(dict):
    """Markov chain model."""
    def __init__(self, order):
        """Model initialization.

        :param order: int
            Order of n-gram that will be used in model.
        """
        super().__init__()
        self.order = order

    def learn(self, sentence):
        """Adds new sentence to model.

        :param sentence: List
            List of words.
        """
        for i in range(len(sentence) - self.order):
            window = tuple(sentence[i: i + self.order])
            if window not in self:
                self[window] = Vertex()
            self[window].add_key(sentence[i + self.order])

    def make_sentence(self, beginning=None, length=20):
        """Creates sentence, based on model.

        :param beginning: Tuple
            Contains first words of the sentence or None.
        :param length: int
            Length of the sentence to create.
        :return: str
            Sentence.
        """
        if beginning is None:
            beginning = random.choice(list(self.keys()))
        sentence = list(beginning)
        previous_window = beginning
        while len(sentence) < length:
            if previous_window in self:
                next_word = self[previous_window].get_random_word()
            else:
                next_word = self[random.choice(list(self.keys()))].\
                    get_random_word()
            sentence.append(next_word)
            previous_window = previous_window[1:] + (next_word, )
        return ' '.join(sentence)

    def save_model(self, path):
        """Saves model to the file using pickle.

        :param path: str
            Path to the file to save model.
        """
        with open(path, 'wb') as f:
            pickle.dump(self, f)
