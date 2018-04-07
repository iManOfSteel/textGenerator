import pickle
import generator_console_interface
import sys

if __name__ == '__main__':
    args = generator_console_interface.get_args()
    if args.output is not None:
        output_file = open(args.output, 'w')
        sys.stdout = output_file

    with open(args.model, 'rb') as f:
        model = pickle.load(f)

    MAX_OUTPUT_LEN = 1000
    window = None
    if args.seed is not None:
        window = tuple(args.seed.split(' '))
    for i in range(0, args.length, MAX_OUTPUT_LEN):
        text = model.make_sentence(beginning=window,
                                   length=min(MAX_OUTPUT_LEN, args.length - i))
        print(text, end=' ')
        window = tuple(text.split()[len(text) - model.order:])
    if args.output is not None:
        output_file.close()
