from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    file1 = 'gendiff/tests/fixtures/file1.json'
    file2 = 'gendiff/tests/fixtures/file2.json'
    result = generate_diff(file1, file2)
    assert result == open('gendiff/tests/fixtures/expected.txt').read()
