# Napisać program rysujący prostokąt zbudowany z małych kratek.
def rectangle(height, depth):
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


x = int(input("Podaj wysokosc: "))
y = int(input("Podaj szerokosc: "))
print(rectangle(x, y))
