#!/usr/bin/env python3
import os
import sys

def aide():
    print("Erreur : mauvaise utilisation du script.")
    print("Utilisation : python find1.py <nom_dossier>")
    sys.exit(1)

def affiche(dossier):
    try:
        for element in os.listdir(dossier):
            print(element)
    except PermissionError:
        print("Permission refusée pour accéder à :", dossier)

def main():
    if len(sys.argv) != 2:
        aide()

    dossier = sys.argv[1]

    if not os.path.exists(dossier):
        print(f"Erreur : le dossier '{dossier}' n'existe pas.")
        aide()
    if not os.path.isdir(dossier):
        print(f"Erreur : '{dossier}' n'est pas un dossier.")
        aide()

    affiche(dossier)

if __name__ == "__main__":
    main()
