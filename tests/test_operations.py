from src.math_operations import subtraction, addition, division


def test_subtraction():
    assert subtraction(5, 2) == 3
    assert subtraction(10, 5) == 5
    
def test_addition():
    assert addition(5, 2) == 7
    assert addition(10, 5) == 15


def test_division():
    assert division(5, 2) == 2.5
    assert division(10, 5) == 2