import os
import sys
import argparse

def recherche(dossier, fichier_recherche):
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
                if elt == fichier_recherche:
                    listeFichiers.append(chemin_complet)
            elif os.path.isdir(chemin_complet):
                listeDossiers.append(chemin_complet)

    return listeFichiers, listeDossiers


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recherche récursive d'un fichier dans un dossier")
    parser.add_argument("-d", "--dossier", required=True, help="Dossier de départ")
    parser.add_argument("-f", "--fichier", required=True, help="Nom du fichier à rechercher")
    args = parser.parse_args()

    dossier = args.dossier
    fichier_recherche = args.fichier

    if not os.path.isdir(dossier):
        print("Erreur : ce n'est pas un répertoire valide.")
        sys.exit(1)

    files, dirs = recherche(dossier, fichier_recherche)

    print("\n=== DOSSIERS TROUVÉS ===")
    for d in dirs:
        print(d)

    print("\n=== FICHIERS TROUVÉS ===")
    for f in files:
        print(f)
