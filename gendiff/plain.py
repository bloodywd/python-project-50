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


def add_first_only(key, _, __, path):
    return f'Property \'{path}{key}\' was removed\n'


def add_second_only(key, value, _, path):
    value = complex_or_not(value)
    return f'Property \'{path}{key}\' was added with value: {value}\n'


def add_diff_values(key, value, _, path):
    value1, value2 = value
    value1 = complex_or_not(value1)
    value2 = complex_or_not(value2)
    return f'Property \'{path}{key}\' was updated. From {value1} to {value2}\n'


def add_children(key, value, _, path):
    answer = ''
    new_path = f'{path}{key}.'
    answer += lower_level(value, new_path)
    return answer


FUNCS = {
    'children': add_children,
    'two_values': add_diff_values,
    'second_only': add_second_only,
    'first_only': add_first_only,
}


def lower_level(level, path):
    level_answer = ''
    for key in sorted(level.keys()):
        value = level[key]['value']
        type = level[key]['type']
        is_nested = level[key]['is_nested']
        if type == 'similar':
            continue
        level_answer += FUNCS[type](key, value, is_nested, path)
    return level_answer


def plain(difference):
    answer = ''
    path = ''
    answer += lower_level(difference, path)
    return answer[:-1]
