import itertools


def stringify(data, depth):
    if type(data) is bool:
        return str(data).lower()
    elif data is None:
        return 'null'
    if type(data) is not dict:
        return data
    lines = []
    for key, value in data.items():
        child = stringify(value, depth + 1)
        indent = get_indent(depth + 1)
        lines.append(f'{indent}{key}: {child}')
    result = itertools.chain("{", lines, [get_indent(depth) + "}"])
    return '\n'.join(result)


def get_indent(depth, type_char=' '):
    if depth == 0:
        return ''
    else:
        return ' ' * (depth * 4 - 2) + f'{type_char} '


def stylish(tree, depth=0):
    lines = []
    for child in tree['children']:
        type = child.get('type')
        key = child.get('key')
        value = child.get('value')
        match type:
            case 'has_children':
                indent = get_indent(depth + 1)
                lines.append(f'{indent}{key}: {stylish(child, depth + 1)}')
            case 'added':
                indent = get_indent(depth + 1, type_char='+')
                lines.append(f'{indent}{key}: {stringify(value, depth + 1)}')
            case 'deleted':
                indent = get_indent(depth + 1, type_char='-')
                lines.append(f'{indent}{key}: {stringify(value, depth + 1)}')
            case 'unchanged':
                indent = get_indent(depth + 1)
                lines.append(f'{indent}{key}: {stringify(value, depth + 1)}')
            case 'changed':
                indent1 = get_indent(depth + 1, type_char='-')
                indent2 = get_indent(depth + 1, type_char='+')
                value1, value2 = child.get('value1'), child.get('value2')
                lines.append(f'{indent1}{key}: {stringify(value1, depth + 1)}')
                lines.append(f'{indent2}{key}: {stringify(value2, depth + 1)}')
            case _:
                raise Exception("Unknown type of node")
    result = itertools.chain("{", lines, [get_indent(depth) + "}"])
    return '\n'.join(result)
