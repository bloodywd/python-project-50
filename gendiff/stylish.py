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
            answer += f'{" " * (depth + 4)}{check_nested(k, val, depth + 4)}\n'
        answer += f'{" " * (depth)}}}'
        return answer
    else:
        return f'{key}: {check_type(value)}'


def add_similar(key, level, depth, answer):
    key_to_string = check_nested(key, level[key], depth)
    answer.append(f'{" " * depth}{key_to_string}')


def add_first_only(key, level, depth, answer):
    key_to_string = check_nested(key, level[key], depth)
    answer.append(f'{" " * (depth - 2)}- {key_to_string}')


def add_second_only(key, level, depth, answer):
    key_to_string = check_nested(key, level[key], depth)
    answer.append(f'{" " * (depth - 2)}+ {key_to_string}')


def add_diff_values(key, level, depth, answer):
    key_to_string1 = check_nested(key, level[key][0], depth)
    key_to_string2 = check_nested(key, level[key][1], depth)
    answer.append(f'{" " * (depth - 2)}- {key_to_string1}')
    answer.append(f'{" " * (depth - 2)}+ {key_to_string2}')


def add_children(key, level, depth, answer):
    answer.append(f'{" " * (depth)}{key}: {{')
    lower_level(level[key], depth + 4, answer)
    answer.append(f'{" " * (depth)}}}')


FUNCS = {
    'children': add_children,
    'different_values': add_diff_values,
    'second_only_keys': add_second_only,
    'first_only_keys': add_first_only,
    'similar': add_similar,
}


def lower_level(level, depth, answer):
    [
        FUNCS[names](key, level, depth, answer)
        for key in sorted(level.keys())
        for names in FUNCS
        if key in level[names]
    ]


def stylish(difference):
    answer = ['{',]
    depth = 0
    lower_level(difference, depth + 4, answer)
    answer.append('}')
    return '\n'.join(answer)
