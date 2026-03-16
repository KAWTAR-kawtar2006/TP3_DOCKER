from app.calculator import add, multiply

def test_add() -> None:
    assert add(2, 4) == 6


def test_multiply() -> None:
    assert multiply(2, 3) == 6

