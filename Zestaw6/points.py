import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return "(%s,%s)" % (self.x, self.y)

    def __repr__(self):  # zwraca string "Point(x, y)"
        return "%s(%r,%r)" % (self.__class__.__name__, self.x, self.y)

    def __eq__(self, other):  # obsługa point1 == point2
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):  # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points


# Kod testujący moduł.


import unittest


class TestPoint(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(Point(1, 3)), "(1,3)")
        self.assertEqual(str(Point(-1, 3)), "(-1,3)")

    def test_repr(self):
        self.assertEqual(repr(Point(1, 3)), "Point(1,3)")
        self.assertEqual(repr(Point(-1, 3)), "Point(-1,3)")

    def test_eq(self):
        self.assertTrue(Point(1, 2).__eq__(Point(1, 2)))
        self.assertFalse(Point(1, 2).__eq__(Point(1, 3)))

    def test_ne(self):
        self.assertTrue(Point(1, 3).__ne__(Point(1, 2)))
        self.assertFalse(Point(1, 2).__ne__(Point(1, 2)))

    def test_add(self):
        self.assertEqual(Point(1, 2).__add__(Point(1, 3)), Point(2, 5))
        self.assertEqual(Point(-1, 2).__add__(Point(1, 3)), Point(0, 5))


    def test_sub(self):
        self.assertEqual(Point(1, 2).__sub__(Point(1, 3)), Point(0, -1))
        self.assertEqual(Point(-1, 2).__sub__(Point(1, 3)), Point(-2, -1))


    def test_mul(self):
        self.assertEqual(Point(1, 3).__mul__(Point(1, 3)), 10)
        self.assertEqual(Point(-1, 3).__mul__(Point(1, 3)), 8)


    def test_cross(self):
        self.assertEqual(Point(1, 3).cross(Point(1, 3)), 0)
        self.assertEqual(Point(-1, 3).cross(Point(1, 3)), -6)


    def test_lenght(self):
        self.assertEqual(Point(-4, 0).length(), 4)
        self.assertEqual(Point(0, 0).length(), 0)


    def test_hash(self):
        self.p1 = Point(3, 4)
        self.assertEqual(hash(self.p1), hash((self.p1.x, self.p1.y)))


if __name__ == '__main__':
    unittest.main()
