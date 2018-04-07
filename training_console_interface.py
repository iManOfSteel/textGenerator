import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir',
                        help='Path do directory with documents')
    parser.add_argument('--model', required=True,
                        help='Model saving destination')
    parser.add_argument('--lc', action='store_true',
                        help='Converts text to lowercase')
    parser.add_argument('--order', type=int, default=2,
                        help='Order of n-gram than will be used in model')
    return parser.parse_args()
