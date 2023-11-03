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


def add_first_only(key, _, path):
    return [
        f'Property \'{path}{key}\' was removed',
    ]


def add_second_only(key, value, path):
    return [
        f'Property \'{path}{key}\' was added '
        f'with value: {complex_or_not(value)}',
    ]


def add_diff_values(key, value, path):
    value1, value2 = value
    return [
        f'Property \'{path}{key}\' was updated. '
        f'From {complex_or_not(value1)} to {complex_or_not(value2)}'
    ]


def add_children(key, value, path):
    new_path = f'{path}{key}.'
    return lower_level(value, new_path)


FUNCS = {
    'children': add_children,
    'two_values': add_diff_values,
    'second_only': add_second_only,
    'first_only': add_first_only,
}


def lower_level(level, path):
    level_answer = []
    for key in sorted(level.keys()):
        value = level[key]['value']
        type = level[key]['type']
        if type == 'similar':
            continue
        level_answer.extend(FUNCS[type](key, value, path))
    return level_answer


def plain(difference):
    path = ''
    return "\n".join(lower_level(difference, path))
