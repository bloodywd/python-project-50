def check_type(value):
    if type(value) is bool:
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def print_nested(level, depth):
    temp = []
    for key in level.keys():
        value = level[key]['value']
        is_nested = level[key]['is_nested']
        if is_nested:
            temp.extend([
                f'{" " * (depth)}{key}: {{',
                print_nested(value, depth),
                f'{" " * (depth)}}}'
            ])
        else:
            temp.append(f'{" " * (depth)}{key}: {check_type(value)}')
    return temp


def add_similar(key, value, is_nested, depth):
    if is_nested:
        return print_nested(key, value, depth)
    else:
        return [
            f'{" " * depth}{key}: {check_type(value)}'
        ]


def add_first_only(key, value, is_nested, depth):
    if is_nested:
        return print_nested(key, value, depth)
    else:
        return [
            f'{" " * (depth - 2)}- {key}: {check_type(value)}'
        ]


def add_second_only(key, value, is_nested, depth):
    if is_nested:
        return [
            f'{" " * (depth - 2)}+ {key}: {{',
            print_nested(value, depth),
            f'{" " * (depth)}}}'
        ]
    else:
        return [
            f'{" " * (depth - 2)}+ {key}: {check_type(value)}'
        ]


def add_diff_values(key, value, is_nested, depth):
    temp = []
    value1, value2 = value
    is_nested1, is_nested2 = is_nested
    if is_nested1:
        temp.extend(print_nested(key, value1, depth))
    else:
        temp.append(f'{" " * (depth - 2)}- {key}: {check_type(value1)}')
    if is_nested2:
        temp.extend(print_nested(key, value2, depth))
    else:
        temp.append(f'{" " * (depth - 2)}+ {key}: {check_type(value2)}')
    return temp


def add_children(key, value, _, depth):
    temp = []
    temp.append(f'{" " * (depth)}{key}: {{')
    temp.extend(stylish_level(value, depth + 4))
    temp.append(f'{" " * (depth)}}}')
    return temp


FUNCS = {
    'children': add_children,
    'two_values': add_diff_values,
    'second_only': add_second_only,
    'first_only': add_first_only,
    'similar': add_similar,
}


def stylish_level(level, depth):
    temp = []
    for key in sorted(level.keys()):
        value = level[key]['value']
        type = level[key]['type']
        is_nested = level[key]['is_nested']
        temp.extend(FUNCS[type](key, value, is_nested, depth))
    return temp


def stylish(difference):
    answer = ['{']
    answer.extend(stylish_level(difference, 4))
    answer.append('}')
    return '\n'.join(answer)
