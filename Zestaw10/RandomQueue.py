import random


class RandomQueue:

    def __init__(self):
        self.items = []

    def insert(self, item):  # wstawia element w czasie O(1)
        self.items.append(item)

    def remove(self):  # zwraca losowy element w czasie O(1)
        index = random.randrange(len(self.items))
        element = self.items[index]
        self.items[index] = self.items[-1]
        self.items.pop()
        return element

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False

    def clear(self):  # czyszczenie listy
        del self.items[:]

