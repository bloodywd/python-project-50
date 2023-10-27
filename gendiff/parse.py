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


def parse(file_path1, file_path2):
    file1, file2 = file_to_string(file_path1, file_path2)
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
