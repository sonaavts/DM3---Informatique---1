import random
import unicodedata

from termcolor import colored

from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

NB_LIGNES = 8
NB_COLONNES = 10

MESSAGES = {
    PorteAvion: "Le porte-avion a coulé !",
    Croiseur: "Le croiseur a coulé !",
    Torpilleur: "Le torpilleur a coulé !",
    SousMarin: "Le sous-marin a coulé !",
}


def placer_bateaux(grille, types):
    # on place les bateaux un par un, sans chevauchement
    bateaux = []
    for Type in types:
        possibles = []
        for l in range(NB_LIGNES):
            for c in range(NB_COLONNES):
                for vertical in [False, True]:
                    b = Type(l, c, vertical)
                    if not grille.rentre(b):
                        continue
                    ok = True
                    for autre in bateaux:
                        if b.chevauche(autre):
                            ok = False
                    if ok:
                        possibles.append(b)
        bateaux.append(random.choice(possibles))
    return bateaux


def afficher(grille):
    # comme print(grille) mais avec des couleurs, des numéros, et chaque case sur 2 caractères
    print("   " + " ".join(str(c) for c in range(NB_COLONNES)))
    for l in range(NB_LIGNES):
        texte = str(l) + "  "
        for c in range(NB_COLONNES):
            car = grille.matrice[l * NB_COLONNES + c]
            # les emojis prennent déjà 2 caractères de large, les autres non
            if unicodedata.east_asian_width(car) != "W":
                car = car + " "
            if car[0] == Grille.vide:
                car = colored(car, "blue")
            elif car[0] == "x":
                car = colored(car, "white", attrs=["bold"])
            texte += car
        print(texte)


def demander(texte, maximum):
    while True:
        rep = input(texte)
        if rep.isdigit() and int(rep) < maximum:
            return int(rep)
        print(colored(f"il faut un nombre entre 0 et {maximum - 1}", "magenta"))


if __name__ == "__main__":
    mer = Grille(NB_LIGNES, NB_COLONNES)        # grille cachée, sert à savoir si c'est coulé
    affichage = Grille(NB_LIGNES, NB_COLONNES)  # grille que voit le joueur

    bateaux = placer_bateaux(mer, [PorteAvion, Croiseur, Torpilleur, SousMarin])
    restants = list(bateaux)
    coups = 0

    while len(restants) > 0:
        afficher(affichage)
        ligne = demander("ligne : ", NB_LIGNES)
        colonne = demander("colonne : ", NB_COLONNES)

        if mer.matrice[ligne * NB_COLONNES + colonne] == "x":
            print(colored("Déjà tiré ici", "magenta"))
            continue
        coups += 1

        mer.tirer(ligne, colonne)

        touche = None
        for b in bateaux:
            if (ligne, colonne) in b.positions():
                touche = b

        if touche is None:
            print(colored("Plouf !", "cyan"))
            affichage.tirer(ligne, colonne)
        else:
            print(colored("Touché !", "red", attrs=["bold"]))
            affichage.tirer(ligne, colonne, "💣")
            if touche in restants and touche.coulé(mer):
                print(colored(MESSAGES[type(touche)], "yellow", attrs=["bold"]))
                affichage.ajoute(touche)
                restants.remove(touche)

    afficher(affichage)
    print(colored(f"Bravo, tous les bateaux sont coulés en {coups} coups", "green", attrs=["bold"]))
