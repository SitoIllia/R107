def most_frequent(L):
    max_count = 0
    premier_max = None
    for n in L:
        count = L.count(n)
        if count > max_count:
            max_count = count
            premier_max = n
    return premier_max, max_count

L = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7]

nb_freq, freq = most_frequent(L)
print("Le nombre le plus frequent dans la liste est le :", nb_freq, f"({freq} x)")