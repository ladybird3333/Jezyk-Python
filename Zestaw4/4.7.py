def flatten(sequence):
    if isinstance(sequence, (list, tuple)):
        if len(sequence) == 0:
            return []
        first_item, rest_item = sequence[0], sequence[1:]
        return flatten(first_item) + flatten(rest_item)
    else:
        return [sequence]


L = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(L))
