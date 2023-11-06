def compare_values(dict1, dict2, key):
    value1 = dict1.get(key)
    value2 = dict2.get(key)
    if key not in dict1:
        return {
            "type": "added",
            "key": key,
            "value": value2
        }
    elif key not in dict2:
        return {
            "type": "deleted",
            "key": key,
            "value": value1
        }
    elif value1 == value2:
        return {
            "type": "unchanged",
            "key": key,
            "value": value1
        }
    elif isinstance(value1, dict) and isinstance(value2, dict):
        return {
            "type": "has_children",
            "key": key,
            "children": get_children(value1, value2),
        }
    else:
        return {
            "type": "changed",
            "key": key,
            "value1": value1,
            "value2": value2
        }


def get_tree(dict1, dict2):
    result = {}
    result['type'] = 'root'
    result['children'] = get_children(dict1, dict2)
    return result


def get_children(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())
    return [compare_values(dict1, dict2, key) for key in keys]
