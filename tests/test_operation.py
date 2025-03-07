from src.math_operation import add, sub

def test_addition():
    assert add(2, 3) == 5
    assert add(1, -1) == 0
    assert add(3, 7) == 10  

def test_subtraction():
    assert sub(4, 1) == 3
    assert sub(1, 1) == 0
    assert sub(3, 2) == 1
