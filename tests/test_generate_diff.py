from gendiff import generate_diff
import json
import os


PATH = os.path.dirname(__file__) + '/fixtures'
# os.path.join не работает, так как file_to_string в модуле parse
# недополучает папку tests


def test_generate_diff_stylish_json():
    file1, file2 = PATH + '/file1.json', PATH + '/file2.json'
    result = generate_diff(file1, file2)
    assert result == open(PATH + '/expected1.txt').read()


def test_generate_diff_stylish_yml():
    file1, file2 = PATH + '/file1.yml', PATH + '/file2.yml'
    result = generate_diff(file1, file2)
    assert result == open(PATH + '/expected1.txt').read()


def test_generate_diff_plane_json():
    file1, file2 = PATH + '/file1.json', PATH + '/file2.json'
    result = generate_diff(file1, file2, 'plain')
    assert result == open(PATH + '/expected2.txt').read()


def test_generate_diff_plane_yml():
    file1, file2 = PATH + '/file1.yml', PATH + '/file2.yml'
    result = generate_diff(file1, file2, 'plain')
    assert result == open(PATH + '/expected2.txt').read()


def test_generate_diff_json():
    file1, file2 = PATH + '/file1.json', PATH + '/file2.json'
    result = json.loads((generate_diff(file1, file2, 'json')))
    expected = json.load(open(PATH + '/expected3.json'))
    assert result == expected
