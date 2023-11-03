import json
import yaml


def file_to_string(file_path):
    if ('.yml' in file_path) or ('.yaml' in file_path):
        file = yaml.safe_load(open(file_path))
    elif ('.json' in file_path):
        file = json.load(open(file_path))
    return file


def is_nested(value):
    return type(value) is dict


def check_values(file1, file2, key):
    value1 = file1.get(key)
    value2 = file2.get(key)
    if key not in file1:
        return value2, 'second_only', is_nested(value2)
    elif key not in file2:
        return value1, 'first_only', is_nested(value1)
    elif value1 == value2:
        return value1, 'similar', is_nested(value1)
    elif is_nested(value1) and is_nested(value2):
        return parse(value1, value2), 'children', True
    else:
        return (
            (value1, value2),
            'two_values',
            (is_nested(value1), is_nested(value2))
        )


def parse(file1, file2):
    difference = {}
    keys1 = list(file1.keys())
    keys2 = list(file2.keys())
    difference_keys = list(set(keys1 + keys2))
    for key in difference_keys:
        value, type, nested = check_values(file1, file2, key)
        difference[key] = {'value': value, 'type': type, 'is_nested': nested}
    return difference
