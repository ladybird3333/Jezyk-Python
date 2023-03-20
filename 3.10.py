# słownik tłumaczący liczby zapisane w systemie rzymskim

# def dictionary(x):
#     roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     print(roman_num[x])

# kod tłumaczący całą liczbę
def roman2int(z):
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(z)):
        if i > 0 and roman_num[z[i]] > roman_num[z[i - 1]]:
            result += roman_num[z[i]] - 2 * roman_num[z[i - 1]]
        else:
            result += roman_num[z[i]]
    return result


x = input("Podaj liczbę w systemie rzymskim: ")

print("Po konwersji na system arabski: " + str(roman2int(x)))
