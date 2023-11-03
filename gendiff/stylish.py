def check_type(value):
    if type(value) is bool:
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def print_nested(level, depth):
    temp = []
    for key, value in level.items():
        is_nested = type(value) is dict
        temp.extend(add_value(key, value, depth + 4, is_nested, type='similar'))
    return temp


def add_value(key, value, depth, is_nested, type):
    temp = []
    if type == 'similar':
        diff = " " * (depth)
    elif type == 'first_only':
        diff = f'{" " * (depth - 2)}- '
    elif type == 'second_only':
        diff = f'{" " * (depth - 2)}+ '
    if is_nested:
        temp.append(f'{diff}{key}: {{')
        temp.extend(print_nested(value, depth))
        temp.append(f'{" " * (depth)}}}')
    else:
        temp.append(f'{diff}{key}: {check_type(value)}')
    return temp


def add_diff_values(key, value, depth, is_nested, _):
    temp = []
    value1, value2 = value
    is_nested1, is_nested2 = is_nested
    temp.extend(add_value(key, value1, depth, is_nested1, type='first_only'))
    temp.extend(add_value(key, value2, depth, is_nested2, type='second_only'))
    return temp


def add_children(key, value, depth, *_):
    temp = []
    temp.append(f'{" " * (depth)}{key}: {{')
    temp.extend(stylish_level(value, depth + 4))
    temp.append(f'{" " * (depth)}}}')
    return temp


FUNCS = {
    'children': add_children,
    'two_values': add_diff_values,
    'second_only': add_value,
    'first_only': add_value,
    'similar': add_value,
}


def stylish_level(level, depth):
    temp = []
    for key in sorted(level.keys()):
        value = level[key]['value']
        type = level[key]['type']
        is_nested = level[key]['is_nested']
        temp.extend(FUNCS[type](
            key,
            value,
            depth,
            is_nested,
            type
        ))
    return temp


def stylish(difference):
    answer = ['{']
    answer.extend(stylish_level(difference, 4))
    answer.append('}')
    return '\n'.join(answer)
