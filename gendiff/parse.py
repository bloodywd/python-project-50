import json
import yaml


def file_to_string(file_path):
    if ('.yml' in file_path) or ('.yaml' in file_path):
        file = yaml.safe_load(open(file_path))
    elif ('.json' in file_path):
        file = json.load(open(file_path))
    return file


def check_values(file1, file2, key):
    if key not in file1:
        return file2[key], 'second_only'
    if key not in file2:
        return file1[key], 'first_only'
    if file1[key] == file2[key]:
        return file1[key], 'similar'
    if isinstance(file1[key], dict) and isinstance(file2[key], dict):
        return parse(file1[key], file2[key]), 'children'
    if file1[key] != file2[key]:
        return (file1[key], file2[key]), 'two_values'


def parse(file1, file2):
    difference = {
        'props': {}
    }
    keys1 = list(file1.keys())
    keys2 = list(file2.keys())
    difference_keys = list(set(keys1 + keys2))
    for key in difference_keys:
        value, props = check_values(file1, file2, key)
        difference[key] = value
        difference['props'][key] = props
    print(difference['props'])
    return difference
