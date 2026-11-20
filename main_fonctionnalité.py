from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

g = Grille(8, 10)
g.ajoute(PorteAvion(0, 0))
g.ajoute(Croiseur(2, 5, True))
g.ajoute(Torpilleur(6, 1))
g.ajoute(SousMarin(4, 8, True))
print(g)
