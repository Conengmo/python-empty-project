"""Configuration file for pytest."""
import os
from typing import Callable

import pytest

import myproject


@pytest.fixture(scope='session')
def path_tests() -> str:
    """Return the full path of the test dir.

    In a test function you can add this as an argument, Pytest will make it available.

    Examples
    --------
    >>> def my_test_function(path_tests: str):
    ...     os.listdir(path_tests)
    """
    return os.path.join(myproject.settings.root_dir, 'tests')


@pytest.fixture(scope='session')
def create_data_function() -> Callable:
    """Return a function to create test data.

    Examples
    --------
    >>> def my_test_function(create_test_data_function: Callable):
    ...     data = create_data_function('argument1')
    """
    def func(arg):
        return arg

    return func
