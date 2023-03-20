import sys


def make_grid(height, depth):
    i = 0
    j = 0
    temp1 = "+"
    temp2 = "|"
    result = ""

    while i < depth:
        temp1 += ("---+")
        temp2 += ("   |")
        i = i + 1
    while j < height:
        result += temp1 + "\n" + temp2 + "\n"
        j = j + 1
    result += temp1
    return result


n = len(sys.argv)
if (n != 3):
    raise ValueError("Nieprawidłowa liczba argumentów!")
print(make_grid(int(sys.argv[1]), int(sys.argv[2])))
