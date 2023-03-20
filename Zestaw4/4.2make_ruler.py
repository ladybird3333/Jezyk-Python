import sys


def make_ruler(number):
    i = 0
    dots = ""
    numbers = ""
    while i <= number:
        if (i == number):
            dots += ("|")
            if (len(str(i))) > 1:
                numbers += (str(i) + "   ")
            else:
                numbers += (str(i) + "    ")
            i = i + 1
        else:
            dots += ("|....")
            if ((len(str(i))) > 1 or (i == 9)):
                numbers += (str(i) + "   ")
            else:
                numbers += (str(i) + "    ")
            i = i + 1

    result = dots + "\n" + numbers
    return result


n = len(sys.argv)
if (n != 2):
    raise ValueError("Nieprawidłowa liczba argumentów!")
print(make_ruler(int(sys.argv[1])))
