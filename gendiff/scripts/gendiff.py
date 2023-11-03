#!/usr/bin/env python3
import argparse
from gendiff.parse import parse, file_to_string
from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.format_to_json import format_to_json


FUNCS = {
    'stylish': stylish,
    'plain': plain,
    'json': format_to_json,
}


def generate_diff(file_path1, file_path2, format='stylish'):
    file1 = file_to_string(file_path1)
    file2 = file_to_string(file_path2)
    diff = parse(file1, file2)
    return FUNCS[format](diff)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument(
        '-f', '--format', help='output format (default: "stylish") '
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    first_file = args.first_file
    second_file = args.second_file
    format = 'stylish' if not args.format else args.format
    print(generate_diff(first_file, second_file, format))


if __name__ == '__main__':
    main()
