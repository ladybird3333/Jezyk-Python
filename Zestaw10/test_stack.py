import pytest
from Stack import Stack


def test_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.is_empty() != True
    assert stack.__str__() == '[1, 2]'


def test_is_empty():
    stack = Stack()
    assert stack.is_empty() == True


def test_str():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.__str__() == '[1, 2, 3]'


def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    assert stack.__str__() == '[1, 2]'


def test_is_full():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.is_full() == False


def test_exception():
    stack = Stack()
    stack.pop()


if __name__ == "__main__":
    pytest.main()
