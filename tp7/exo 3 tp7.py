
import os
import sys

def recherche(dossier):
    listeFichiers = []
    listeDossiers = []

    listeDossiers.append(dossier)

    for d in listeDossiers:
        try:
            contenu = os.listdir(d)
        except PermissionError:
            continue

        for elt in contenu:
            chemin_complet = os.path.join(d, elt)

            if os.path.isfile(chemin_complet):
                listeFichiers.append(chemin_complet)

            elif os.path.isdir(chemin_complet):
                listeDossiers.append(chemin_complet)

    return listeFichiers, listeDossiers


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python3 find2.py <nom_dossier>")
        sys.exit(1)

    dossier = sys.argv[1]

    if not os.path.isdir(dossier):
        print("Erreur : ce n'est pas un répertoire valide.")
        sys.exit(1)

    files, dirs = recherche(dossier)

    print("\n=== DOSSIERS TROUVÉS ===")
    for d in dirs:
        print(d)

    print("\n=== FICHIERS TROUVÉS ===")
    for f in files:
        print(f)
