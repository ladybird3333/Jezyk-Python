def Fibonacci(n):
    a = 0
    b = 1
    if (n < 0):
        print("Niepoprawne dane!")
    if (n == 0):
        return a
    if (n == 1):
        return b

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b


x = int(input("Podaj który wyraz ciągu Fibonacciego chcesz obliczyć: "))
print(Fibonacci(x))
