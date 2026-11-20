# User story "Plouf dans l'eau"

from grille import Grille

grille = Grille(5, 8)

while True:
    print(grille)
    ligne = int(input("ligne : "))
    colonne = int(input("colonne : "))
    grille.tirer(ligne, colonne)
