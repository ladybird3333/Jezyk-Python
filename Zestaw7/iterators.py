import itertools
import random


#  a
def example_a():
    count = 0
    for i in itertools.cycle('01'):
        if count > 7:
            break
        else:
            print(i, end=" ")
            count += 1


# b
def example_b():
    arr = ("N", "E", "S", "W")
    print(random.choice(arr))


# c
def example_c():
    count = 0
    for i in itertools.cycle(range(0, 7)):
        if count > 48:
            break
        else:
            print(i, end=" ")
            count += 1

example_a()
print("\t")
example_b()
example_c()
