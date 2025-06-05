import pytest

from src.calc import add


def test_add():
    assert add(2, 3) == 5


@pytest.mark.parametrize(
    "a,b,expected",
    [(-1, -2, -3), (-1, 1, 0), (0, 0, 0)],
)
def test_add_negative(a: int, b: int, expected: int) -> None:
    assert add(a, b) == expected
