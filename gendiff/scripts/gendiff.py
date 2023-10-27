#!/usr/bin/env python3
import argparse
from gendiff.parse import parse


def generate_diff(file_path1, file_path2):
    return parse(file_path1, file_path2)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument(
        '-f', '--format', help='set format of output'
    )
    return parser.parse_args()


__all__ = (
    'generate_diff',
)


def main():
    args = parse_arguments()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
