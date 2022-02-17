import pytest

from introduction import add

@pytest.mark.parametrize("a, b, expected", [(2,3,5),
                                            (2, -3, -1),
                                            (2, 3.5, 5.5),
                                            (2, -3.5, -1.5),
                                            (2, 0, 2),
                                            (2, -0, 2),
                                            (2, 0.0, 2),
                                            (2, -0.0, 2),
                                            (2, 0.5, 2.5),
                                            (2, -0.5, 1.5)])
def test_add(a, b, expected):
    assert add(a, b) == expected