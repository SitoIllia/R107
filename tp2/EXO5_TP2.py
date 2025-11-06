x= int(input("Entrez un nombre entier:"))
if x==0:
    print("le nombre est null")
else:
    if x >0:
        x=x%2
        if x==0:
            print("le nombre est positif est pair")
        else:
            print("le nombre est positif et impair")
    else:
        x=x%2
        if x==0:
            print("Le nombre est négatif est pair")
        else:
            print("le nombre est négatif et impair")




