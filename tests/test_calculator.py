import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.calculator import add, multiply

def test_add() -> None:
    assert add(2, 4) == 6


def test_multiply() -> None:
    assert multiply(2, 3) == 6

