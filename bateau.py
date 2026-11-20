class Bateau:
    marque = "⛵"

    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    def positions(self):
        pos = []
        for i in range(self.longueur):
            if self.vertical:
                pos.append((self.ligne + i, self.colonne))
            else:
                pos.append((self.ligne, self.colonne + i))
        return pos

    def coulé(self, grille):
        for (l, c) in self.positions():
            if grille.matrice[l * grille.nombre_colonnes + c] != "x":
                return False
        return True

    def chevauche(self, autre):
        for p in self.positions():
            if p in autre.positions():
                return True
        return False


class PorteAvion(Bateau):
    marque = "🚢"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 4, vertical)


class Croiseur(Bateau):
    marque = "⛴"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 3, vertical)


class Torpilleur(Bateau):
    marque = "🚣"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)


class SousMarin(Bateau):
    marque = "🐟"

    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)
