def check_type(value):
    if type(value) is bool:
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return value


def is_nested(value):
    return type(value) is dict


def stylish_single_value(key, value, indent_count, description):
    result = []
    indent = ''
    nested = is_nested(value)
    if description == 'unchanged':
        indent += ' ' * indent_count
    elif description == 'deleted':
        indent += ' ' * (indent_count - 2) + '- '
    elif description == 'added':
        indent += ' ' * (indent_count - 2) + '+ '
    if nested:
        result.append(f'{indent}{key}: {{')
        for k, val in value.items():
            result.extend(stylish_single_value(
                k, val, indent_count + 4, description='unchanged')
            )
        result.append(' ' * indent_count + '}')
    else:
        result.append(f'{indent}{key}: {check_type(value)}')
    return result


def get_value(node, key):
    return node[key]['value'], node[key]['description']


def stylish_node(node, indent_count):
    result = []
    for key in sorted(node.keys()):
        value, description = get_value(node, key)
        if description == 'has_children':
            result.append(' ' * indent_count + key + ': {')
            result.extend(stylish_node(value, indent_count + 4))
            result.append(' ' * indent_count + '}')
        if description in ('added', 'deleted', 'unchanged'):
            result.extend(
                stylish_single_value(key, value, indent_count, description)
            )
        if description == 'changed':
            value1, value2 = value
            result.extend(stylish_single_value(
                key, value1, indent_count, description='deleted'
            ))
            result.extend(stylish_single_value(
                key, value2, indent_count, description='added'
            ))
    return result


def stylish(difference):
    answer = ['{']
    answer.extend(stylish_node(difference, indent_count=4))
    answer.append('}')
    return '\n'.join(answer)
