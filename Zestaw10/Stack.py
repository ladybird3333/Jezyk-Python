class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):  # podglądamy stos
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):  # nigdy nie jest pełny
        return False

    def push(self, item):
        if self.is_full():
            raise Exception('Stos jest przepelniony')
        self.items.append(item)  # dodajemy na koniec

    def pop(self):  # zwraca element
        if self.is_empty():
            raise Exception('Stos jest pusty')
        return self.items.pop()  # zabieram od końca
