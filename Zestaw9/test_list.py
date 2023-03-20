import pytest
from SingleList import SingleList, Node


def test_insert():
    alist = SingleList()
    alist.insert_head(Node(1))
    alist.insert_head(Node(2))
    alist.insert_tail(Node(3))  # [2,1,3]
    head = alist.head
    tail = alist.tail
    assert head.data == 2
    assert tail.data == 3
    assert alist.count() == 3


def test_remove():
    alist = SingleList()
    alist.insert_head(Node(1))
    alist.insert_head(Node(2))
    alist.insert_tail(Node(5))
    alist.insert_tail(Node(3))  # [2,1,5,3]
    alist.remove_tail()
    alist.remove_head()  # alist=[1,5]
    assert alist.count() == 2
    head = alist.head
    tail = alist.tail
    assert head.data == 1
    assert tail.data == 5


def test_join():
    alist = SingleList()
    alist.insert_head(Node(1))
    alist.insert_head(Node(2))
    alist.insert_tail(Node(3))  # [2,1,3]

    blist = SingleList()
    blist.insert_head(Node(6))
    blist.insert_head(Node(7))
    blist.insert_head(Node(8))  # [8,7,6]

    alist.join(blist)  # alist=[2,1,3,8,7,6]
    head = alist.head
    tail = alist.tail
    assert head.data == 2
    assert tail.data == 6
    assert blist.count() == 0


def test_empty():
    alist = SingleList()
    alist.insert_head(Node(1))
    alist.remove_head()
    assert alist.is_empty() == True


def test_clear():
    alist = SingleList()
    alist.insert_head(Node(1))
    alist.insert_head(Node(2))
    alist.insert_tail(Node(3))  # [2,1,3]
    alist.clear()
    assert alist.count() == 0


if __name__ == "__main__":
    pytest.main()
