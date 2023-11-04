def complex_or_not(value):
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


def get_value(node, key):
    return node[key]['value'], node[key]['description']


def plain_node(node, path):
    result = []
    for key in sorted(node.keys()):
        value, description = get_value(node, key)
        if description == 'has_children':
            result.extend(plain_node(value, path + key + '.'))
        elif description == 'added':
            result.append(f'Property \'{path}{key}\' was added '
                          f'with value: {complex_or_not(value)}')
        elif description == 'deleted':
            result.append(f'Property \'{path}{key}\' was removed')
        elif description == 'changed':
            value1, value2 = value
            result.append(f'Property \'{path}{key}\' was updated. From '
                          f'{complex_or_not(value1)} to '
                          f'{complex_or_not(value2)}')
    return result


def plain(difference):
    return "\n".join(plain_node(difference, path=''))
