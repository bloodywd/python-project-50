import json
import yaml


def file_to_string(file_path):
    if ('.yml' in file_path) or ('.yaml' in file_path):
        file = yaml.safe_load(open(file_path))
    elif ('.json' in file_path):
        file = json.load(open(file_path))
    return file


def check_values(file1, file2, key):
    value1 = file1.get(key)
    value2 = file2.get(key)
    if key not in file1:
        return value2, 'second_only'
    elif key not in file2:
        return value1, 'first_only'
    elif value1 == value2:
        return value1, 'similar'
    elif isinstance(value1, dict) and isinstance(value2, dict):
        return parse(value1, value2), 'children'
    else:
        return (
            (value1, value2),
            'two_values'
        )
    #  функция check_values выполяет следующие вещи:
    #  сравнивает два значения, и выдает по итогу сравнения тип:
    #      first_only - значение ключа есть только в первом объекте
    #      second_only - значение ключа есть только во втором объекте
    #      similar - значения ключа в первом и втором объекте одинаковые
    #      children - значение ключа в первом и втором объекте - составные
    #      two_values - значения существует, но не равны друг другу
    #  функция возвращает кортеж,
    #      где первый элемент - итоговое значение (или оба в случае two_values)
    #      второй элемент - тип значения


def parse(file1, file2):
    difference = {}
    keys1 = list(file1.keys())
    keys2 = list(file2.keys())
    difference_keys = list(set(keys1 + keys2))
    for key in difference_keys:
        value, type = check_values(file1, file2, key)
        difference[key] = {'value': value, 'type': type}
    return difference
