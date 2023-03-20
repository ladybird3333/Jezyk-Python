# x = 2;
# y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;
# Podany kod nie jest poprawny ponieważ w Pythonie nie stosujemy na końcu instrukcji znaku ';'

# for i in "axby": if ord(i) < 100: print (i)
# Podany kod nie jest poprawny, ponieważ warunek w pętli powinniśmy napisać w nowej linii, po znaku tabulacji.
# Poprawny kod:
for i in "axby":
    if ord(i) < 100: print(i)

# Podany kod jest poprawny
for i in "axby": print(ord(i) if ord(i) < 100 else i)
