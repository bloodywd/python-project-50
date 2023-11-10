import json
import yaml


def parse(file_path):
    if '.yml' in file_path or '.yaml' in file_path:
        return yaml.safe_load(open(file_path))
    elif '.json' in file_path:
        return json.load(open(file_path))
    else:
        raise Exception("Unknown file type")
