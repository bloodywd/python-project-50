from gendiff.parse import parse
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.format_to_json import json_formatter
from gendiff.tree import get_tree


def generate_diff(file_path1, file_path2, formatter='stylish'):
    file1 = parse(file_path1)
    file2 = parse(file_path2)
    tree = get_tree(file1, file2)
    if formatter == 'stylish':
        return stylish(tree)
    if formatter == 'plain':
        return plain(tree)
    if formatter == 'json':
        return json_formatter(tree)
