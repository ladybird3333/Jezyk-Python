L1 = [9, 3, 1, 5, 4, 6]
L2 = [9, 3, 1, 5, 4, 6]


def partial_reverse(list, left, right):
    while (left < right):
        temp = list[left]
        list[left] = list[right]
        list[right] = temp
        left += 1
        right -= 1
    return list


def partial_reverse_recursion(list, left, right):
    list[left], list[right] = list[right], list[left]
    if (right - left) > 1:
        partial_reverse_recursion(list, left + 1, right - 1)
    return list


print("Przed zamianą miejscami (wersja iteracyjna): "+str(L1)+", po zamianie : "+ str(partial_reverse(L1, 1, 4)))
print("Przed zamianą miejscami (wersja rekurencyjna): "+str(L2)+", po zamianie : "+ str(partial_reverse_recursion(L2, 1, 4)))
