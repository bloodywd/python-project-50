from gendiff.parse import parse, open_file
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.format_to_json import json_formatter


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
