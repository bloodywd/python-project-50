#!/usr/bin/env python3
import argparse
import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    diff = '{\n'
    for key, value in file1.items():
        if key in file2:
            if file1[key] == file2[key]:
                diff += f'    {key}: {value}\n'
            else:
                diff += f'  - {key}: {value}\n  + {key}: {file2[key]}\n'
        else:
            diff += f'  - {key}: {value}\n'
    for key, value in file2.items():
        if key not in file1:
            diff += f'  + {key}: {value}\n'
    diff += '}'
    return diff


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
