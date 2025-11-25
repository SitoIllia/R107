nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
notes = []
somme_notes = 0.0

for i in range(nombreEtudiants):
    note_valide = False
    while not note_valide:
        note = float(input(f"Note etudiant {i} : "))
        if 0 <= note <= 20:
            notes.append(note)
            somme_notes += note
            note_valide = True
        else:
            print("Erreur : La note doit être comprise entre 0 et 20.")

moyenne = somme_notes / nombreEtudiants
print(f"Moyenne de classe : {moyenne}")

print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range(nombreEtudiants):
    ecart = notes[i] - moyenne
    print(f"{i} | {notes[i]} | {ecart}")