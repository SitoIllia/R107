
nombre = float(input("Vous cherchez la table de multiplication de quel nombre ? "))

resultats = []

for i in range(10):
    produit = round(nombre * i, 1)
    resultats.append(produit)

for i in range(10):
    print(f"{nombre} * {i} = {resultats[i]}")