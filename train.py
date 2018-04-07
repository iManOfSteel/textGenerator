"""Module that creates model from set of texts."""
import os
import sys
import markov_model
import training_console_interface
from parser import parse


def learn_from_text(model, lc, file=sys.stdin):
    """Adds text from file to model

    :param model: Model
        Model, that will be updated.
    :param lc: Boolean
        if True, all text will be converted to lowercase.
    :param file: File or sys.stdin
        Text source
    """
    for line in file:
        if lc:
            line = line.lower()
        line = parse(line)
        for sentence in line:
            model.learn(sentence)


def main():
    """Trains the model on files from the set"""
    args = training_console_interface.get_args()
    model = markov_model.Model(args.order - 1)
    if args.input_dir is None:
        learn_from_text(model, args.lc)
    else:
        for name in os.listdir(args.input_dir):
            with open(os.path.join(args.input_dir, name),
                      encoding='utf-8') as file:
                learn_from_text(model, args.lc, file)
    model.save_model(args.model)


if __name__ == "__main__":
    main()
