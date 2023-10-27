#!/usr/bin/env python3
import argparse
from gendiff.parse import parse, file_to_string
from gendiff.stylish import stylish


def generate_diff(file_path1, file_path2):
    file1, file2 = file_to_string(file_path1, file_path2)
    diff = parse(file1, file2)
    return stylish(diff)


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
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
