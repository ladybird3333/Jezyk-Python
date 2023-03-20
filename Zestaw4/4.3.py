def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


n = int(input("Podaj liczbę: "))
print("Silnia liczby "+str(n)+" wynosi "+str(factorial(n)))
