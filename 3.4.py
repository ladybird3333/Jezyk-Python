# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x.
while True:
    x = input("Prosze podać liczbe : ")
    if x != "stop":
        if x.isdigit():
            power = (float(x) ** 3)
            print(str(float(x)) + "  " + str(power))
        else:
            print("Niepoprawne dane na wejściu!")
    else:
        break
