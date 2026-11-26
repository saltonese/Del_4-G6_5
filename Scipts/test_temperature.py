import pytest
from Task_1 import Temperature

def test_initialization():
    temp = Temperature(25)

    assert temp.value == 25.0
    assert temp.unit == "C"
