# Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.
i = 0
while i <= 30:
    if i % 3 != 0 or i == 0:
        print(i, end=' ')
    i = i + 1
