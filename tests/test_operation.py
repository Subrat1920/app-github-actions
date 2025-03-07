from src.math_operation import add, sub

def test_add():
    assert add(2,3)==5
    assert add(1,-1)==0
    assert add(3,2)==10


def test_add():
    assert sub(4,1)==3
    assert sub(1,1)==0
    assert sub(3,2)==10