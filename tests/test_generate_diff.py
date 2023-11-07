from gendiff import generate_diff
import json
import os
import pytest
import itertools


PATH = os.path.join(os.path.dirname(__file__), 'fixtures')


@pytest.mark.parametrize(
    "file1,file2,expected,formatter",
    [
        ('file1.json', 'file2.json', 'expected1.txt', 'stylish'),
        ('file1.yml', 'file2.yml', 'expected1.txt', 'stylish'),
        ('file1.json', 'file2.json', 'expected2.txt', 'plain'),
        ('file1.yml', 'file2.yml', 'expected2.txt', 'plain'),
    ],
)
def test_generate_diff(file1, file2, expected, formatter):
    file1, file2 = os.path.join(
        PATH, file1), os.path.join(PATH, file2)
    result = generate_diff(file1, file2, formatter)
    with open(os.path.join(PATH, expected), 'r') as f:
        assert result == f.read()


def test_generate_diff_json():
    file1, file2 = os.path.join(
        PATH, 'file1.json'), os.path.join(PATH, 'file2.json')
    result = json.loads((generate_diff(file1, file2, 'json')))
    with open(os.path.join(PATH, 'expected3.json'), 'r') as f:
        assert result == json.load(f)
