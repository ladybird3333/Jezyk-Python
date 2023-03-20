# Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby.
# Znaleźć listę zawierającą sumy liczb z tych sekwencji.
L = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
temp = []

for item in L:
    result = 0
    for x in item:
        result +=x
    temp.append(result)
print("Sekwencja: "+str(L))
print("Wynik: "+str(temp))
