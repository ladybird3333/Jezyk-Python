# Dla dwóch sekwencji liczb lub znaków znaleźć:
# (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń)
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

x = input("Podaj ciąg znaków/liczb dla zbioru pierwszego: ")
S1=set(x)
print("S1: "+str(S1))

y = input("Podaj ciąg znaków/liczb dla zbioru drugiego: ")
S2=set(y)
print("S2: "+str(S2))

intersection=S1.intersection(S2)
print("Część wspólna zbiorów S1 i S2: " + str(intersection))

sum=S1.union(S2)
print("Suma zbiorów S1 i S2: "+str(sum))

