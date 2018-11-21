from typing import Callable


def test_path_tests(path_tests: str):
    assert isinstance(path_tests, str)
    assert path_tests.endswith('tests')


def test_create_data_function(create_data_function: Callable):
    data = create_data_function('hi there')
    assert data == 'hi there'
