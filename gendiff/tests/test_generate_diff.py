from gendiff import generate_diff


def test_generate_diff_json():
    file1 = 'gendiff/tests/fixtures/file1.json'
    file2 = 'gendiff/tests/fixtures/file2.json'
    result = generate_diff(file1, file2)
    assert result == open('gendiff/tests/fixtures/expected.txt').read()


def test_generate_diff_yaml():
    file1 = 'gendiff/tests/fixtures/file1.yml'
    file2 = 'gendiff/tests/fixtures/file2.yml'
    result = generate_diff(file1, file2)
    assert result == open('gendiff/tests/fixtures/expected.txt').read()


def test_generate_diff_stylish():
    file1 = 'gendiff/tests/fixtures/file3.json'
    file2 = 'gendiff/tests/fixtures/file4.json'
    result = generate_diff(file1, file2)
    assert result == open('gendiff/tests/fixtures/expected2.txt').read()


def test_generate_diff_plane():
    file1 = 'gendiff/tests/fixtures/file3.json'
    file2 = 'gendiff/tests/fixtures/file4.json'
    result = generate_diff(file1, file2, 'plane')
    assert result == open('gendiff/tests/fixtures/expected3.txt').read()
