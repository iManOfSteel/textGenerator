"""Console interface for generate.py"""
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', required=True,
                        help='Path to model')
    parser.add_argument('--length', required=True, type=int,
                        help='Length of the text')
    parser.add_argument('--seed',
                        help='Beginning of the text')
    parser.add_argument('--output',
                        help='Path to output file')
    parser.add_argument('--max-output-len', type=int, default=100,
                        help='Max line length in output')
    return parser.parse_args()
