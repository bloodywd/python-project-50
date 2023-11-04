import json
import yaml


def open_file(file_path):
    if '.yml' in file_path or '.yaml' in file_path:
        return yaml.safe_load(open(file_path))
    elif '.json' in file_path:
        return json.load(open(file_path))


def compare_values(file1, file2, key):
    value1 = file1.get(key)
    value2 = file2.get(key)
    if key not in file1:
        return value2, 'added'
    elif key not in file2:
        return value1, 'deleted'
    elif value1 == value2:
        return value1, 'unchanged'
    elif isinstance(value1, dict) and isinstance(value2, dict):
        return parse(value1, value2), 'has_children'
    else:
        return (
            (value1, value2),
            'changed'
        )


def set_value(result, key, value, description):
    result[key] = {'value': value, 'description': description}


def parse(file1, file2):
    result = {}
    keys1 = list(file1.keys())
    keys2 = list(file2.keys())
    result_keys = list(set(keys1 + keys2))
    for key in result_keys:
        value, description = compare_values(file1, file2, key)
        set_value(result, key, value, description)
    return result
