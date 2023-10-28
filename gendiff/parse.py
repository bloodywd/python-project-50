import json
import yaml


def file_to_string(file_path):
    if ('.yml' in file_path) or ('.yaml' in file_path):
        file = yaml.safe_load(open(file_path))
    elif ('.json' in file_path):
        file = json.load(open(file_path))
    return file


def create_difference():
    return {
        'similar': [],
        'different_values': [],
        'first_only_keys': [],
        'second_only_keys': [],
        'children': []
    }


def add_one_value(difference, key, value, index):
    difference[index].append(key)
    difference[key] = value


def add_children(difference, key):
    difference['children'].append(key)


def add_different_values(difference, key, value1, value2):
    difference['different_values'].append(key)
    difference[key] = value1, value2


def operate_same_key(diff, key, value1, value2):
    if value1 == value2:
        add_one_value(diff, key, value1, 'similar')
    elif isinstance(value1, dict) and isinstance(value2, dict):
        add_children(diff, key)
        diff[key] = parse(value1, value2)
    else:
        add_different_values(diff, key, value1, value2)


def parse(file1, file2):
    difference = create_difference()
    for key, value in file1.items():
        if key in file2:
            operate_same_key(difference, key, value, file2[key])
        else:
            add_one_value(difference, key, value, 'first_only_keys')
    for key, value in file2.items():
        if key not in file1:
            add_one_value(difference, key, value, 'second_only_keys')
    return difference
