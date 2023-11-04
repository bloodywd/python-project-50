import argparse
from gendiff.parse import parse, open_file
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.format_to_json import json_formatter


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


def run_differ():
    args = parse_arguments()
    first_file = args.first_file
    second_file = args.second_file
    formatter = 'stylish' if not args.format else args.format
    print(generate_diff(first_file, second_file, formatter))


def generate_diff(file_path1, file_path2, formatter='stylish'):
    file1 = open_file(file_path1)
    file2 = open_file(file_path2)
    diff = parse(file1, file2)
    if formatter == 'stylish':
        return stylish(diff)
    if formatter == 'plain':
        return plain(diff)
    if formatter == 'json':
        return json_formatter(diff)
