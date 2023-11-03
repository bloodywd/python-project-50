from gendiff import generate_diff
import json
import os


PATH = os.path.join(os.path.dirname(__file__) + '/fixtures')


def test_generate_diff_stylish_json():
    file1, file2 = os.path.join(
        PATH + '/file1.json'), os.path.join(PATH + '/file2.json')
    result = generate_diff(file1, file2)
    assert result == open(os.path.join(PATH + '/expected1.txt')).read()


def test_generate_diff_stylish_yml():
    file1, file2 = os.path.join(
        PATH + '/file1.yml'), os.path.join(PATH + '/file2.yml')
    result = generate_diff(file1, file2)
    assert result == open(os.path.join(PATH + '/expected1.txt')).read()


def test_generate_diff_plane_json():
    file1, file2 = os.path.join(
        PATH + '/file1.json'), os.path.join(PATH + '/file2.json')
    result = generate_diff(file1, file2, 'plain')
    assert result == open(os.path.join(PATH + '/expected2.txt')).read()


def test_generate_diff_plane_yml():
    file1, file2 = os.path.join(
        PATH + '/file1.yml'), os.path.join(PATH + '/file2.yml')
    result = generate_diff(file1, file2, 'plain')
    assert result == open(os.path.join(PATH + '/expected2.txt')).read()


def test_generate_diff_json():
    file1, file2 = os.path.join(
        PATH + '/file1.json'), os.path.join(PATH + '/file2.json')
    result = json.loads((generate_diff(file1, file2, 'json')))
    expected = json.load(open(os.path.join(PATH + '/expected3.json')))
    assert result == expected
