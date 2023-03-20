from points import Point


class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        if x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) == 0:
            raise ValueError("Punkty sa wspolliniowe")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):  # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "[({}, {}), ({}, {}), ({}, {})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x,
                                                       self.pt3.y)

    def __repr__(self):  # "Triangle(x1, y1, x2, y2, x3, y3)"
        return "%s(%s,%s,%s,%s,%s,%s)" % (
            self.__class__.__name__, self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x,
            self.pt3.y)

    def __eq__(self, other):  # obsługa tr1 == tr2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2 and self.pt3 == other.pt3

    def __ne__(self, other):  # obsługa tr1 != tr2
        return not self == other

    def center(self):  # zwraca środek trójkąta
        return Point((self.pt1.x + self.pt2.x + self.pt3.x) / 3, (self.pt1.y + self.pt2.y + self.pt3.y) / 3)

    def area(self):  # pole powierzchni
        return 0.5 * abs((self.pt2.x - self.pt1.x) * (self.pt3.y - self.pt1.y) - (self.pt2.y - self.pt1.y) * (
                self.pt3.x - self.pt1.x))

    def move(self, x, y):  # przesunięcie o (x, y)
        return Triangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y, self.pt3.x + x, self.pt3.y + y)

    def make4(self):  # zwraca krotkę czterech mniejszych
        temp1 = Point((self.pt1.x + self.pt3.x) / 2, (self.pt1.y + self.pt3.y) / 2)
        temp2 = Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)
        temp3 = Point((self.pt2.x + self.pt3.x) / 2, (self.pt2.y + self.pt3.y) / 2)
        t1 = Triangle(self.pt1.x, self.pt1.y, temp1.x, temp1.y, temp2.x, temp2.y)
        t2 = Triangle(temp1.x, temp1.y, temp2.x, temp2.y, temp3.x, temp3.y)
        t3 = Triangle(temp1.x, temp1.y, self.pt3.x, self.pt3.y, temp3.x, temp3.y)
        t4 = Triangle(temp3.x, temp3.y, temp2.x, temp2.y, self.pt2.x, self.pt2.y)
        return t1, t2, t3, t4


# Kod testujący moduł.

import unittest


class TestTriangle(unittest.TestCase):

    def test_str(self):
        t1 = str(Triangle(1, 1, 4, 1, 2, 5))
        t2 = "[(1, 1), (4, 1), (2, 5)]"

        if (t1 != t2):
            raise ValueError('Triangles are diffirent')

    def test_str2(self):
        t1 = str(Triangle(1, 1, 4, 1, 2, 5))
        t2 = "[(1, 1), (4, 1), (2, 6)]"

        if (t1 != t2):
            raise ValueError('Triangles are diffirent')

    def test_repr1(self):
        t1 = repr(Triangle(1, 1, 4, 1, 2, 5))
        t2 = "Triangle(1,1,4,1,2,5)"

        if (t1 != t2):
            raise ValueError('Triangles are diffirent')

    def test_repr2(self):
        t1 = repr(Triangle(1, 1, 4, 1, 2, 6))
        t2 = "Triangle(1,1,4,1,2,5)"

        if (t1 != t2):
            raise ValueError('Triangles are diffirent')

    def test_ne1(self):
        t1 = Triangle(1, 1, 4, 1, 2, 6)
        t2 = Triangle(1, 1, 4, 1, 2, 7)

        if (t1.__ne__(t2)) == True:
            raise ValueError('Triangles are diffirent')

    def test_ne2(self):
        t1 = Triangle(1, 1, 4, 1, 2, 7)
        t2 = Triangle(1, 1, 4, 1, 2, 7)

        if (t1.__ne__(t2)) == True:
            raise ValueError('Triangles are diffirent')

    def test_eq(self):
        t1 = Triangle(1, 1, 4, 1, 2, 7)
        t2 = Triangle(1, 1, 4, 1, 2, 7)

        if (t1.__eq__(t2)) != True:
            raise ValueError('Triangles are diffirent')

    def test_eq2(self):
        t1 = Triangle(1, 1, 4, 1, 2, 7)
        t2 = Triangle(0, 1, 4, 1, 2, 7)

        if (t1.__eq__(t2)) != True:
            raise ValueError('Triangles are diffirent')

    def test_move1(self):
        t1 = Triangle(1, 1, 4, 1, 2, 7)
        t2 = Triangle(2, 2, 5, 2, 3, 8)

        if (t1.move(1, 1) != t2):
            raise ValueError('Triangles are diffirent')

    def test_move2(self):
        t1 = Triangle(1, 1, 4, 1, 2, 7)
        t2 = Triangle(2, 2, 5, 2, 3, 7)

        if (t1.move(1, 1) != t2):
            raise ValueError('Triangles are diffirent')

    def test_center(self):
        t1 = Triangle(1, 1, 4, 1, 2, 7)
        t2 = Triangle(1, 1, 3, 1, 2, 7)

        if (t1.center() != Point(2.3333333333333335, 3)):
            raise ValueError('Points are diffirent')

        if (t2.center() != Point(2, 3)):
            raise ValueError('Points are diffirent ')

    def test_area(self):

        t1 = Triangle(1, 1, 3, 1, 2, 4)
        t2 = Triangle(1, 1, 3, 1, 2, 7)

        if (t1.area() != 3):
            raise ValueError('Value error')

        if (t2.area() != 6):
            raise ValueError('Value error')

    def test_make4(self):
        t1 = Triangle(1, 1, 3, 1, 2, 4)

        if (t1.make4() != ((
        Triangle(1, 1, 1.5, 2.5, 2, 1), Triangle(1.5, 2.5, 2, 1, 2.5, 2.5), Triangle(1.5, 2.5, 2, 4, 2.5, 2.5),
        Triangle(2.5, 2.5, 2, 1, 3, 1)))):
            raise ValueError('Value error!')


if __name__ == '__main__':
    unittest.main()
