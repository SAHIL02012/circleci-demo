# test_add.py
from add import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test_add()