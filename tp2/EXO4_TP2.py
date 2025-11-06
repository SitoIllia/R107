base=4
fromage=800.0
eau=2
ail=2
pain=400
nbConvives= int(input("Entrez le nombre de personne(s) conviées à la fondue:"))
nouvelleQuantite_f= fromage * nbConvives / base
nouvelleQuantite_e= eau * nbConvives / base
nouvelleQuantite_a= ail * nbConvives / base
nouvelleQuantite_p= pain * nbConvives / base
print("Pour faire une fondue fribourgeoise pour", nbConvives," personnes, il vous faut :")
print("-", nouvelleQuantite_f, "gr de fromage")
print("-", nouvelleQuantite_e, "dcl d'eau")
print("-", nouvelleQuantite_a, "gousse(s) d'ail")
print("-", nouvelleQuantite_p, "gr de pain")





