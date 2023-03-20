import pytest
from points import Point
from rectangles import Rectangle


# Kod testujący moduł rectangle

def test_center():
    assert Rectangle(1, 2, 4, 6).center, Point(2.5, 4)


def test_center2():
    assert Rectangle(2, -2, 5, 3).center, Point(3.5, 0.5)


def test_from_points():
    point1 = Point(1, 2)
    point2 = Point(4, 6)

    list = [point1, point2]
    rec = Rectangle.from_points(list)
    assert str(rec) == "[(1,2), (4,6)]"


def test_width():
    rec = Rectangle(1, 2, 4, 6)
    assert rec.width == 3


def test_height():
    rec = Rectangle(1, 2, 4, 6)
    assert rec.height == 4


def test_top():
    rec = Rectangle(1, 2, 4, 6)
    assert rec.top == 6


def test_bottom():
    rec = Rectangle(1, 2, 4, 6)
    assert rec.bottom == 2


def test_left():
    rec = Rectangle(1, 2, 4, 6)
    assert rec.left == 1


def test_right():
    rec = Rectangle(1, 2, 4, 6)
    assert rec.right == 4


def test_Points():
    point1 = Point(1, 2)
    point2 = Point(4, 6)
    list = [point1, point2]
    rec = Rectangle.from_points(list)
    assert rec.bottomleft == point1
    assert rec.topright == point2
    p3 = Point(point1.x, point2.y)
    p4 = Point(point2.x, point1.y)
    assert rec.topleft == p3
    assert rec.bottomright == p4


if __name__ == "__main__":
    pytest.main()
