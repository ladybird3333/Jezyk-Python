# Napisać program rysujący "miarkę" o zadanej długości.
def ruler(number):
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


x = int(input("Podaj długość miarki : "))
print(ruler(x))
