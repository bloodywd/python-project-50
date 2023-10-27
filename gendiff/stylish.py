def check_nested(key, value, depth):
    answer = ''
    if isinstance(value, dict):
        answer += f'{key}: {{\n'
        for k, val in value.items():
            answer += f'{" " * (depth + 4)}{check_nested(k, val, depth + 4)}'
        answer += f'{" " * (depth)}}} \n'
        return answer
    else:
        return f'{key}: {value}\n'


def add_simular(level, depth):
    answer = ''
    for key in level['simular']:
        key_to_string = check_nested(key, level[key], depth)
        answer += f'{" " * depth}{key_to_string}'
    return answer


def add_first_only(level, depth):
    answer = ''
    for key in level['first_only_keys']:
        key_to_string = check_nested(key, level[key], depth)
        answer += f'{" " * (depth - 2)}- {key_to_string}'
    return answer


def add_second_only(level, depth):
    answer = ''
    for key in level['second_only_keys']:
        key_to_string = check_nested(key, level[key], depth)
        answer += f'{" " * (depth - 2)}+ {key_to_string}'
    return answer


def add_diff_values(level, depth):
    answer = ''
    for key in level['different_values']:
        key_to_string1 = check_nested(key, level[key][0], depth)
        key_to_string2 = check_nested(key, level[key][1], depth)
        answer += f'{" " * (depth - 2)}- {key_to_string1}'
        answer += f'{" " * (depth - 2)}+ {key_to_string2}'
    return answer


def add_children(level, depth):
    answer = ''
    for key in level['children']:
        answer += f'{" " * (depth)}{key}: {{ \n'
        answer += lower_level(level[key], depth + 4)
        answer += f'{" " * (depth)}}} \n'
    return answer


def lower_level(level, depth):
    level_answer = ''
    level_answer += add_simular(level, depth)
    level_answer += add_first_only(level, depth)
    level_answer += add_second_only(level, depth)
    level_answer += add_diff_values(level, depth)
    level_answer += add_children(level, depth)
    return level_answer


def stylish(difference):
    answer = '{\n'
    depth = 0
    answer += lower_level(difference, depth + 4)
    answer += '}'
    print(answer)
    return answer
