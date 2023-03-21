# Program służący do kompresji danych z wykorzystaniem algorytmu Huffmana

# Do zliczenia wystapien znakow w slowie
from collections import Counter
# Do implementacji kolejki priorytetowej w postaci kopca
import heapq


class Node:
    # Konstruktor klasy Node
    def __init__(self, prob, value, left=None, right=None):
        # liczba wystąpień symbolu
        self.prob = prob

        # wartosc symbolu
        self.value = value

        # lewy wezel
        self.left = left

        # prawy wezel
        self.right = right

        # wartosc w kodowaniu Huffmanna (jesli bedzie dzieckiem lewym: wartosc 0)
        # wartosc w kodowaniu Huffmanna (jesli bedzie dzieckiem prawym: wartosc 1)
        self.code_huff = ''

    def __lt__(self, nxt):
        return self.prob < nxt.prob


# Funkcja zliczajaca ilosc wystapien znakow w slowie
def Calc_Prob(data):
    chars = Counter(data)
    return chars


# Funkcja wypisujaca slownik zwrócony przez funkcje Calc_Prob od znaku z najmniejsza iloscia wystapien.
def Print_Freq(data):
    # znaki wraz z ich liczba wystapien
    data_with_prob = Calc_Prob(data)
    print("Wystapienia symboli:")

    # Sortuje wartości w słowniku (od najmniejszej liczby wystąpień do największej)
    sorted_data_with_prob = sorted(data_with_prob.items(), key=lambda x: x[1])
    print(sorted_data_with_prob)


# Funkcja realizujaca algorytm Huffmana
def Huffman_coding(data):
    # slownik ze znakami oraz ich liczba wystapien
    data_with_prob = Calc_Prob(data)
    # wyciagam do pomocniczej tablicy chars wszystkie znaki (wszystkie klucze)
    chars = data_with_prob.keys()

    # pomocnicza tablica, w ktorej przechowywane beda wezly
    nodes_arr = []

    for char in chars:
        # tworze wezly i dodaje je do kopca
        heapq.heappush(nodes_arr, Node(data_with_prob.get(char), char))

    while len(nodes_arr) > 1:
        # biore dwa wezly z najmniejsza liczba wystapien
        left = heapq.heappop(nodes_arr)
        right = heapq.heappop(nodes_arr)

        # przypisuje im wartosci 0 (dla lewego) oraz 1 (dla prawego)
        left.code_huff = 0
        right.code_huff = 1

        # tworze nowy wezel utworzony z dwoch powyższych wezlow
        # wartosc nowego wezla jest suma dwoch powyższych
        combined_Node = Node(left.prob + right.prob, left.value + right.value, left, right)

        # dodaje do kopca nowo utworzony wezel
        heapq.heappush(nodes_arr, combined_Node)

    print("Zakodowane symbole:")
    # Wywolanie funkcji, ktora wypisuje symbole z wartoscia po zakodowaniu
    CalculateCode(nodes_arr[0])


codes = dict()


# Funkcja wypisujaca symbol wraz z jego wartoscia po zakodowaniu
def CalculateCode(node, val=''):
    new_val = val + str(node.code_huff)

    # rekurencyjnie przechodze po wszystkich lewych dzieciach
    if node.left:
        CalculateCode(node.left, new_val)

    # rekurencyjnie przechodze po wszystkich prawych dzieciach
    if node.right:
        CalculateCode(node.right, new_val)

    # jesli wezel jest lisciem to wypisuje jego zakodowana wartosc
    if not node.left and not node.right:
        # do pomocnicze slownika zapisuje znaki z ich zakodowana wartoscia
        codes[node.value] = new_val
        # wypisuje znaki z zakodowana wartoscia
        print(f"{node.value} -> {new_val}")


# Funkcja zwracajaca cale zakodowane slowo
def Encoded_full_word(data):
    temp_arr = []
    for char in data:
        # wyciagam ze slownika codes zakodowane wartosci symboli
        # i umieszczam je w tablicy arr
        symbol = codes.get(char)
        temp_arr.append(symbol)
    join_word = ''.join(temp_arr)
    return join_word


def Presentation(data, encoded_word):
    print("Slowo przed kodowaniem: " + str(data))
    print("Slowo przed kodowaniem zajmuje: " + str(len(data) * 8) + " b")

    print("Slowo po zakodowaniu: " + str(encoded_word))
    print("Slowo po zakodowaniu zajmuje: " + str(len(encoded_word)) + " b")


if __name__ == "__main__":
    print("*** Przyklad pierwszy ***")
    word1 = 'AAAABBBBBBBBBBCCCCCDDDDDDDDEEEEEEEEEFFFFFFFFFFFGHH'
    print("Slowo: " + word1)
    Print_Freq(word1)
    Huffman_coding(word1)
    encoded_word1 = Encoded_full_word(word1)
    Presentation(word1, encoded_word1)

    print("\n*** Przyklad drugi ***")
    word2 = 'matematyka'
    print("Slowo: " + word2)
    Print_Freq(word2)
    Huffman_coding(word2)
    encoded_word2 = Encoded_full_word(word2)
    Presentation(word2, encoded_word2)
