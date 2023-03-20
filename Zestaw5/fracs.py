import math


def reduction(frac):
    result = math.gcd(frac[0], frac[1])
    if frac[0] == 0:
        return [0, 0]
    else:
        return [frac[0] / result, frac[1] / result]


def add_frac(frac1, frac2):
    if frac1[1] != frac2[1]:
        return reduction([frac1[0] * frac2[1] + frac2[0] * frac1[1], frac1[1] * frac2[1]])
    else:
        return [frac1[0] + frac2[0], frac1[0]]


def sub_frac(frac1, frac2):
    if frac1[1] != frac2[1]:
        return reduction([frac1[0] * frac2[1] - frac2[0] * frac1[1], frac1[1] * frac2[1]])
    else:
        return reduction([frac1[0] - frac2[0], frac1[0]])


def mul_frac(frac1, frac2):
    return reduction([frac1[0] * frac2[0], frac1[1] * frac2[1]])


def div_frac(frac1, frac2):
    return reduction([frac1[0] * frac2[1], frac1[1] * frac2[0]])


def is_positive(frac):
    return frac[0] * frac[1] > 0


def is_zero(frac):
    return frac[0] == 0


def cmp_frac(frac1, frac2):
    tmp1 = reduction([frac1[0], frac1[1]])
    tmp2 = reduction([frac2[0], frac2[1]])
    if tmp1[0] == 0 and tmp2[0] == 0:
        return 0
    elif tmp1[0] / tmp1[1] > tmp2[0] / tmp2[1]:
        return -1
    elif tmp1[0] == tmp2[0] and tmp1[1] == tmp2[1]:
        return 0
    else:
        return 1


def frac2float(frac):
    return float(frac[0]) / float(frac[1])


# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)

import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_add_frac2(self):
        self.assertEqual(add_frac([-1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [0, 3]), [1, 2])

    def test_sub_frac2(self):
        self.assertEqual(sub_frac([1, 2], [0, 3]), [0, 0])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 3], [1, 2]), [1, 6])

    def test_mul_frac2(self):
        self.assertEqual(mul_frac([-2, 3], [0, 3]), [-2, 9])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 3], [4, 3]), [1, 4])

    def test_div_frac2(self):
        self.assertEqual(div_frac([2, 3], [1, 2]), [2, 3])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]), True)

    def test_is_positive2(self):
        self.assertFalse(is_positive([0, 2]), False)

    def test_is_positive3(self):
        self.assertFalse(is_positive([-1, 2]), False)

    def test_is_zero(self):
        self.assertFalse(is_zero([1, 2]), False)

    def test_is_zero2(self):
        self.assertTrue(is_zero([0, 2]), True)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [3, 4]), 1)

    def test_cmp_frac2(self):
        self.assertEqual(cmp_frac([1, 2], [1, 2]), 0)

    def test_cmp_frac3(self):
        self.assertEqual(cmp_frac([3, 2], [1, 2]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)

    def test_frac2float2(self):
        self.assertEqual(frac2float([1, 4]), 0.2)


if __name__ == '__main__':
    unittest.main()
