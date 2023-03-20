from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return "[(%s,%s), (%s,%s)]" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return "%s(%s,%s,%s,%s)" % (self.__class__.__name__, self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):  # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def center(self):  # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):  # pole powierzchni
        return abs((self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y))

    def move(self, x, y):  # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)


# Kod testujący moduł.

import unittest


class TestRectangle(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(Rectangle(1, 2, 4, 6)), "[(1,2), (4,6)]")
        self.assertEqual(str(Rectangle(2, -2, 5, 3)), "[(2,-2), (5,3)]")

    def test_repr(self):
        self.assertEqual(repr(Rectangle(1, 2, 4, 6)), "Rectangle(1,2,4,6)")
        self.assertEqual(repr(Rectangle(2, -2, 5, 3)), "Rectangle(2,-2,5,3)")

    def test_ne(self):
        self.assertTrue(Rectangle(1, 2, 4, 6).__ne__(Rectangle(1, 2, 1, 5)))
        self.assertFalse(Rectangle(1, 2, 4, 6).__ne__(Rectangle(1, 2, 4, 6)))

    def test_eq(self):
        self.assertTrue(Rectangle(1, 2, 4, 6).__eq__(Rectangle(1, 2, 4, 6)))
        self.assertFalse(Rectangle(1, 2, 1, 4).__eq__(Rectangle(0, 2, 1, 4)))

    def test_move(self):
        self.assertEqual(Rectangle(1, 2, 4, 6).move(1, 1), Rectangle(2, 3, 5, 7))
        self.assertEqual(Rectangle(1, 2, 4, 6).move(-1, 1), Rectangle(0, 3, 3, 7))

    def test_center(self):
        self.assertEqual(Rectangle(1, 2, 4, 6).center(), Point(2.5, 4))
        self.assertEqual(Rectangle(2, -2, 5, 3).center(), Point(3.5, 0.5))

    def test_area(self):
        self.assertEqual(Rectangle(1, 2, 4, 6).area(), 12)
        self.assertEqual(Rectangle(2, -2, 5, 3).area(), 15)


if __name__ == '__main__':
    unittest.main()
