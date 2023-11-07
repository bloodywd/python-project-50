import itertools


def stringify(data, indent_count):
    if type(data) is bool:
        return str(data).lower()
    elif data is None:
        return 'null'
    if type(data) is not dict:
        return data
    lines = []
    for key, value in data.items():
        child = stringify(value, indent_count + 4)
        lines.append(f'{(indent_count + 4) * " "}{key}: {child}')
    result = itertools.chain("{", lines, [get_indent(indent_count) + "}"])
    return '\n'.join(result)


def get_indent(indent_count, type='unchanged'):
    if type == 'changed':
        return (' ' * (indent_count - 2) + '- ',
                ' ' * (indent_count - 2) + '+ ')
    if type in ('unchanged', 'has_children'):
        return ' ' * indent_count
    elif type == 'deleted':
        return ' ' * (indent_count - 2) + '- '
    elif type == 'added':
        return ' ' * (indent_count - 2) + '+ '


def check_value(child, indent_count):
    result = []
    type = child.get('type')
    key = child.get('key')
    value = child.get('value')
    indent = get_indent(indent_count, type)
    if type == 'has_children':
        result.append(f'{indent}{key}: {stylish(child, indent_count)}')
    if type in ('added', 'deleted', 'unchanged'):
        result.append(
            f'{indent}{key}: {stringify(value, indent_count)}'
        )
    if type == 'changed':
        indent1, indent2 = get_indent(indent_count, type)
        value1, value2 = child.get('value1'), child.get('value2')
        result.append(f'{indent1}{key}: {stringify(value1, indent_count)}')
        result.append(f'{indent2}{key}: {stringify(value2, indent_count)}')
    return '\n'.join(result)


def stylish(tree, indent_count=0):
    lines = []
    for child in tree['children']:
        lines.append(check_value(child, indent_count + 4))
    result = itertools.chain("{", lines, [get_indent(indent_count) + "}"])
    return '\n'.join(result)
