import pytest
from RandomQueue import RandomQueue


def test_insert():
    r = RandomQueue()
    r.insert(1)
    r.insert(2)
    assert r.is_empty() != True


def test_is_empty():
    r = RandomQueue()
    assert r.is_empty() == True


def test_is_full():
    r = RandomQueue()
    assert r.is_full() == False


def test_remove():
    r = RandomQueue()
    r.insert(1)
    r.insert(2)

    r.remove()
    r.remove()

    assert r.is_empty() == True


def test_clear():
    r = RandomQueue()
    r.insert(1)
    r.insert(2)
    r.insert(3)
    r.clear()
    assert r.is_empty() == True


if __name__ == "__main__":
    pytest.main()
