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


def add_first_only(key, level, path, answer):
    answer.append(f'Property \'{path}{key}\' was removed')


def add_second_only(key, level, path, answer):
    value = complex_or_not(level[key])
    answer.append(f'Property \'{path}{key}\' was added with value: {value}')


def add_diff_values(key, level, path, answer):
    value1 = complex_or_not(level[key][0])
    value2 = complex_or_not(level[key][1])
    answer.append(
        f'Property \'{path}{key}\' was updated. From {value1} to {value2}'
    )


def add_children(key, level, path, answer):
    new_path = f'{path}{key}.'
    lower_level(level[key], new_path, answer)


FUNCS = {
    'children': add_children,
    'different_values': add_diff_values,
    'second_only_keys': add_second_only,
    'first_only_keys': add_first_only,
}


def lower_level(level, path, answer):
    [
        FUNCS[names](key, level, path, answer)
        for key in sorted(level.keys())
        for names in FUNCS
        if key in level[names]
    ]


def plain(difference):
    answer = []
    path = ''
    lower_level(difference, path, answer)
    return '\n'.join(answer)
