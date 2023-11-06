#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff.cli import parse_arguments


def main():
    args = parse_arguments()
    first_file = args.first_file
    second_file = args.second_file
    formatter = 'stylish' if not args.format else args.format
    print(generate_diff(first_file, second_file, formatter))


if __name__ == '__main__':
    main()
