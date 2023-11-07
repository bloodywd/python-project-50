def stringify(data, indent_count):
    if type(data) is bool:
        return str(data).lower()
    elif data is None:
        return 'null'
    if type(data) is not dict:
        return data
    result = ["{"]
    for key, value in data.items():
        child = stringify(value, indent_count + 4)
        result.append(f'{(indent_count + 4) * " "}{key}: {child}')
    result.append(f'{indent_count * " "}}}')
    return '\n'.join(result)


def get_indent(type, indent_count):
    if type == 'changed':
        return ' ' * (indent_count - 2) + '- ', ' ' * (indent_count - 2) + '+ '
    if type == 'unchanged' or type == 'has_children':
        return ' ' * indent_count
    elif type == 'deleted':
        return ' ' * (indent_count - 2) + '- '
    elif type == 'added':
        return ' ' * (indent_count - 2) + '+ '


def check_value(tree, indent_count):
    result = []
    type = tree.get('type')
    key = tree.get('key')
    value = tree.get('value')
    indent = get_indent(type, indent_count)
    if type == 'has_children':
        result.extend(stylish_children(tree, indent_count))
    if type in ('added', 'deleted', 'unchanged'):
        result.append(
            f'{indent}{key}: {stringify(value, indent_count)}'
        )
    if type == 'changed':
        indent1, indent2 = get_indent(type, indent_count)
        result.append(f'{indent1}{key}: {stringify(tree["value1"], indent_count)}')
        result.append(f'{indent2}{key}: {stringify(tree["value2"], indent_count)}')
    return result


def stylish_children(tree, indent_count=0):
    result = []
    if tree['type'] == 'root':
        result.append("{")
    else:
        result.append(f'{indent_count * " "}{tree.get("key")}: {{')
    for child in tree['children']:
        result.extend(check_value(child, indent_count + 4))
    result.append(f'{indent_count * " "}}}')
    return result


def stylish(difference):
    result = stylish_children(difference)
    return '\n'.join(result)
