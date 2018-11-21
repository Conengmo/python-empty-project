import os
import sys
import subprocess

import pytest


project_name = 'myproject'


def test_flake8():
    """Run flake8 if on Windows and fail test if there are linter errors.

    We don't want to run this test on the CI server, because there it is already included.
    A crude check skips this test if it is ran on Linux.
    """
    if sys.platform in ('linux', 'linux2'):
        pytest.skip("flake8 pytest only runs on Windows to disable it on the CI server.")
    path = os.path.normpath(os.path.join(os.path.dirname(__file__), os.pardir))
    os.chdir(path)
    command = ['flake8', project_name]
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if process.stderr:
        raise RuntimeError('Error while running flake8: {}'.format(process.stderr.decode('utf-8')))
    out = process.stdout.decode('utf8').lower()
    assert len(out) == 0, 'flake8 found PEP8 linter errors:\n{}'.format(out)
