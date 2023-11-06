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


def get_value(node, key):
    return node[key]['value'], node[key]['description']


def plain_node(node, path):
    result = []
    for key in node.keys():
        value, description = get_value(node, key)
        if description == 'has_children':
            result.extend(plain_node(value, path + key + '.'))
        elif description == 'added':
            result.append(f'Property \'{path}{key}\' was added '
                          f'with value: {check_type(value)}')
        elif description == 'deleted':
            result.append(f'Property \'{path}{key}\' was removed')
        elif description == 'changed':
            value1, value2 = value
            result.append(f'Property \'{path}{key}\' was updated. From '
                          f'{check_type(value1)} to '
                          f'{check_type(value2)}')
    return result


def plain(difference):
    print(difference)
    return "\n".join(plain_node(difference, path=''))
