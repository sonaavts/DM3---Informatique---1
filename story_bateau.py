# User story "chevauchement"

from bateau import Bateau

# deux bateaux qui se chevauchent (en (2, 4))
b1 = Bateau(2, 3, longueur=3)
b2 = Bateau(1, 4, longueur=3, vertical=True)
print(b1.positions(), b2.positions())
print("chevauchement :", b1.chevauche(b2))

# deux bateaux qui ne se chevauchent pas
b1 = Bateau(0, 0, longueur=2)
b2 = Bateau(3, 0, longueur=4)
print(b1.positions(), b2.positions())
print("chevauchement :", b1.chevauche(b2))
