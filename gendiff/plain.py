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
    return f'Property \'{path}{key}\' was removed\n'


def add_second_only(key, level, path):
    value = complex_or_not(level[key])
    return f'Property \'{path}{key}\' was added with value: {value}\n'


def add_diff_values(key, level, path):
    value1 = complex_or_not(level[key][0])
    value2 = complex_or_not(level[key][1])
    return f'Property \'{path}{key}\' was updated. From {value1} to {value2}\n'


def add_children(key, level, path):
    answer = ''
    new_path = f'{path}{key}.'
    answer += lower_level(level[key], new_path)
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
        if key == 'props':
            continue
        props = level['props']
        if props[key] == 'similar':
            continue
        key_func_name = props[key]
        level_answer += FUNCS[key_func_name](key, level, path)
    return level_answer


def plain(difference):
    answer = ''
    path = ''
    answer += lower_level(difference, path)
    return answer[:-1]
