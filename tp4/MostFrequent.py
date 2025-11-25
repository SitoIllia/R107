# **********************
# Complétez le programme à partir d'ici.
# **********************

def most_frequent(L):
    compteur = {}
    for n in L:
        if n in compteur:
            compteur[n] += 1
        else:
            compteur[n] = 1
    max = 0
    premier_max = None
    for n in L:
        if compteur[n] > max:
            max = compteur[n]
            premier_max = n
    return premier_max, max
L = [2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7, 6,2, 55, 7, 55, 36, 7, 21, 56, 55, 3, 7]

nb_freq, freq = most_frequent(L)
print("Le nombre le plus frequent dans la liste est le :", nb_freq, f"({freq} x)")

# **********************
# Ne rien modifier après cette ligne.
# **********************
