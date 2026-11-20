class Grille:
    vide = "∿"

    def __init__(self, nombre_lignes, nombre_colonnes):
        self.nombre_colonnes = nombre_colonnes
        self.matrice = [Grille.vide] * (nombre_lignes * nombre_colonnes)

    def tirer(self, ligne, colonne, touche="x"):
        self.matrice[ligne * self.nombre_colonnes + colonne] = touche

    def rentre(self, bateau):
        nombre_lignes = len(self.matrice) // self.nombre_colonnes
        for (l, c) in bateau.positions():
            if l < 0 or l >= nombre_lignes or c < 0 or c >= self.nombre_colonnes:
                return False
        return True

    def ajoute(self, bateau):
        if not self.rentre(bateau):
            return
        for (l, c) in bateau.positions():
            self.matrice[l * self.nombre_colonnes + c] = bateau.marque

    def __str__(self):
        lignes = []
        for i in range(0, len(self.matrice), self.nombre_colonnes):
            lignes.append("".join(self.matrice[i:i + self.nombre_colonnes]))
        return "\n".join(lignes)
