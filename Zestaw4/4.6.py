L = [[], 2, [4], (1, 2)]


def sum_seq(sequence):
    result_sum = 0
    for item in sequence:
        if (isinstance(item, (list, tuple))):
            result_sum += sum_seq(item)
        else:
            result_sum += item
    return result_sum


print("Suma liczb dla sekwencji : "+str(L)+ " wynosi : "+str(sum_seq(L)))
