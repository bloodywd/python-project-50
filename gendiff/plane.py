def complex_or_not(value):
    value_type = type(value)
    if value_type in (list, tuple, range, dict, set, frozenset):
        return '[complex value]'
    else:
        return f"'{value}'"


def add_first_only(key, level, path):
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
    for new_level in level['children']:
        answer += lower_level(level[new_level], new_path)
    return answer


FUNCS = {
    'children': add_children,
    'different_values': add_diff_values,
    'second_only_keys': add_second_only,
    'first_only_keys': add_first_only,
}


def lower_level(level, path):
    level_answer = ''
    for key in level:
        for names in FUNCS:
            if key in level[names]:
                level_answer += FUNCS[names](key, level, path)
    return level_answer


def plane(difference):
    answer = ''
    path = ''
    answer += lower_level(difference, path)
    return answer[:-1]
