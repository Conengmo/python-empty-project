import os
import sys
import subprocess

import pytest


project_name = 'myproject'


def test_mypy():
    """Run mypy if on Windows and fail test if there are typing errors.

    We don't want to run this test on the CI server, because there it is already included.
    A crude check skips this test if it is ran on Linux.
    """
    if sys.platform in ('linux', 'linux2'):
        pytest.skip("mypy pytest only runs on Windows to disable it on the CI server.")
    path = os.path.normpath(os.path.join(os.path.dirname(__file__), os.pardir))
    os.chdir(path)
    command = ['mypy', project_name, '--config-file', 'tox.ini']
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if process.stderr:
        raise RuntimeError('Error while running mypy: {}'.format(process.stderr.decode('utf-8')))
    out = process.stdout.decode('utf8').lower()
    if len(out) != 0:
        pytest.fail('mypy found typing errors:\n{}'.format(out))
