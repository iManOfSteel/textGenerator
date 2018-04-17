"""Generates text."""
import pickle
import generator_console_interface
import sys


def main():
    """Generates text with the specified length and first words."""
    args = generator_console_interface.get_args()
    if args.output is not None:
        sys.stdout = open(args.output, 'w')

    with open(args.model, 'rb') as f:
        model = pickle.load(f)

    window = None
    if args.seed is not None:
        window = tuple(args.seed.split(' '))
    for i in range(0, args.length, args.max_output_len):
        text = model.make_sentence(beginning=window,
                                   length=min(args.max_output_len, args.length - i))
        print(text)
        window = tuple(text.split()[len(text) - model.order:])
    if args.output is not None:
        sys.stdout.close()


if __name__ == '__main__':
    main()
