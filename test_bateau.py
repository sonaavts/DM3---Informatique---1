from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin
from grille import Grille


def test_init():
    b = Bateau(2, 3)
    assert b.ligne == 2
    assert b.colonne == 3
    assert b.longueur == 1
    assert b.vertical == False


def test_init_parametres():
    b = Bateau(2, 3, longueur=4, vertical=True)
    assert b.longueur == 4
    assert b.vertical == True


def test_positions():
    assert Bateau(2, 3, longueur=3).positions() == [(2, 3), (2, 4), (2, 5)]
    assert Bateau(2, 3, longueur=3, vertical=True).positions() == [(2, 3), (3, 3), (4, 3)]


def test_coulé():
    g = Grille(5, 8)
    b = Bateau(2, 3, longueur=2)
    g.ajoute(b)
    assert not b.coulé(g)
    g.tirer(2, 3)
    assert not b.coulé(g)
    g.tirer(2, 4)
    assert b.coulé(g)


def test_types():
    assert PorteAvion(0, 0).longueur == 4
    assert Croiseur(0, 0).longueur == 3
    assert Torpilleur(0, 0).longueur == 2
    assert SousMarin(0, 0).longueur == 2
    assert Croiseur(1, 2, True).vertical == True
    assert isinstance(SousMarin(0, 0), Bateau)


def test_types_ajout_grille():
    g = Grille(2, 4)
    g.ajoute(PorteAvion(0, 0))
    assert g.matrice == ["🚢", "🚢", "🚢", "🚢", "∿", "∿", "∿", "∿"]

    g = Grille(3, 2)
    g.ajoute(Croiseur(0, 1, True))
    g.ajoute(Torpilleur(0, 0, True))
    assert g.matrice == ["🚣", "⛴", "🚣", "⛴", "∿", "⛴"]

    g = Grille(1, 3)
    g.ajoute(SousMarin(0, 1))
    assert g.matrice == ["∿", "🐟", "🐟"]


def test_chevauche():
    b1 = Bateau(2, 3, longueur=3)
    b2 = Bateau(1, 4, longueur=3, vertical=True)
    b3 = Bateau(0, 0, longueur=2)
    assert b1.chevauche(b2)
    assert b2.chevauche(b1)
    assert not b1.chevauche(b3)
