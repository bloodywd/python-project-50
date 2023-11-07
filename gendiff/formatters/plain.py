def check_type(value):
    value_type = type(value)
    if value_type in (list, tuple, range, dict, set, frozenset):
        return '[complex value]'
    elif value_type is bool:
        return str(value).lower()
    elif value is None:
        return 'null'
    elif value_type is str:
        return f"'{value}'"
    else:
        return f"{value}"


def plain(tree, path=''):
    result = []
    for child in tree['children']:
        value = child.get('value')
        type = child.get('type')
        key = child.get('key')
        if type == 'has_children':
            result.append(plain(child, path + key + '.'))
        elif type == 'added':
            result.append(f'Property \'{path}{key}\' was added '
                          f'with value: {check_type(value)}')
        elif type == 'deleted':
            result.append(f'Property \'{path}{key}\' was removed')
        elif type == 'changed':
            value1 = child.get('value1')
            value2 = child.get('value2')
            result.append(f'Property \'{path}{key}\' was updated. From '
                          f'{check_type(value1)} to '
                          f'{check_type(value2)}')
    return "\n".join(result)
