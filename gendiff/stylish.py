def check_type(value):
    if type(value) is bool:
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def check_nested(key, value, depth):
    answer = ''
    if isinstance(value, dict):
        answer += f'{key}: {{\n'
        for k, val in value.items():
            answer += f'{" " * (depth + 4)}{check_nested(k, val, depth + 4)}'
        answer += f'{" " * (depth)}}}\n'
        return answer
    else:
        return f'{key}: {check_type(value)}\n'


def add_similar(key, level, depth):
    answer = ''
    key_to_string = check_nested(key, level[key], depth)
    answer += f'{" " * depth}{key_to_string}'
    return answer


def add_first_only(key, level, depth):
    answer = ''
    key_to_string = check_nested(key, level[key], depth)
    answer += f'{" " * (depth - 2)}- {key_to_string}'
    return answer


def add_second_only(key, level, depth):
    answer = ''
    key_to_string = check_nested(key, level[key], depth)
    answer += f'{" " * (depth - 2)}+ {key_to_string}'
    return answer


def add_diff_values(key, level, depth):
    answer = ''
    key_to_string1 = check_nested(key, level[key][0], depth)
    key_to_string2 = check_nested(key, level[key][1], depth)
    answer += f'{" " * (depth - 2)}- {key_to_string1}'
    answer += f'{" " * (depth - 2)}+ {key_to_string2}'
    return answer


def add_children(key, level, depth):
    answer = ''
    answer += f'{" " * (depth)}{key}: {{\n'
    answer += lower_level(level[key], depth + 4)
    answer += f'{" " * (depth)}}}\n'
    return answer


FUNCS = {
    'children': add_children,
    'different_values': add_diff_values,
    'second_only_keys': add_second_only,
    'first_only_keys': add_first_only,
    'similar': add_similar,
}


def lower_level(level, depth):
    level_answer = ''
    for key in sorted(level.keys()):
        for names in FUNCS:
            if key in level[names]:
                level_answer += FUNCS[names](key, level, depth)
    return level_answer


def stylish(difference):
    answer = '{\n'
    depth = 0
    answer += lower_level(difference, depth + 4)
    answer += '}'
    return answer
