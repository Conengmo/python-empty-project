
from myproject.mymod import do_something


def test_do_something():
    return_obj = do_something()
    assert return_obj is None
