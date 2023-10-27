import json
import yaml


def file_to_string(file_path1, file_path2):
    if ('.yml' in file_path1) or ('.yaml' in file_path1):
        file1 = yaml.safe_load(open(file_path1))
        file2 = yaml.safe_load(open(file_path2))
    elif ('.json' in file_path1):
        file1 = json.load(open(file_path1))
        file2 = json.load(open(file_path2))
    return (file1, file2)


def create_difference():
    return {
        'simular': [],
        'different_values': [],
        'first_only_keys': [],
        'second_only_keys': [],
        'children': []
    }


def add_simular(difference, key, value):
    difference['simular'].append(key)
    difference[key] = value


def add_children(difference, key):
    difference['children'].append(key)


def add_different_values(difference, key, value1, value2):
    difference['different_values'].append(key)
    difference[key] = value1, value2


def add_first_only(difference, key, value):
    difference['first_only_keys'].append(key)
    difference[key] = value


def add_second_only(difference, key, value):
    difference['second_only_keys'].append(key)
    difference[key] = value


def operate_same_key(diff, key, value1, value2):
    if value1 == value2:
        add_simular(diff, key, value1)
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
            add_first_only(difference, key, value)
    for key, value in file2.items():
        if key not in file1:
            add_second_only(difference, key, value)
    return difference