from grille import Grille
from bateau import Bateau


def test_init():
    g = Grille(5, 8)
    assert g.nombre_colonnes == 8
    assert g.matrice == ["∿"] * 40


def test_tirer():
    g = Grille(5, 8)
    g.tirer(2, 3)
    assert g.matrice[19] == "x"
    assert g.matrice.count("x") == 1


def test_tirer_touche():
    g = Grille(2, 3)
    g.tirer(1, 1, touche="💣")
    assert g.matrice == ["∿", "∿", "∿", "∿", "💣", "∿"]


def test_ajoute():
    g = Grille(2, 3)
    g.ajoute(Bateau(1, 0, longueur=2, vertical=False))
    assert g.matrice == ["∿", "∿", "∿", "⛵", "⛵", "∿"]


def test_ajoute_depasse():
    g = Grille(2, 3)
    g.ajoute(Bateau(1, 0, longueur=2, vertical=True))
    g.ajoute(Bateau(1, 0, longueur=4, vertical=True))
    assert g.matrice == ["∿", "∿", "∿", "∿", "∿", "∿"]


def test_ajoute_depasse_a_droite():
    # ne doit pas déborder sur la ligne suivante
    g = Grille(2, 3)
    g.ajoute(Bateau(0, 2, longueur=2))
    assert g.matrice == ["∿", "∿", "∿", "∿", "∿", "∿"]


def test_rentre():
    g = Grille(2, 3)
    assert g.rentre(Bateau(1, 0, longueur=3))
    assert not g.rentre(Bateau(1, 0, longueur=2, vertical=True))
    assert not g.rentre(Bateau(0, 2, longueur=2))


def test_str():
    g = Grille(5, 8)
    assert str(g) == "∿∿∿∿∿∿∿∿\n∿∿∿∿∿∿∿∿\n∿∿∿∿∿∿∿∿\n∿∿∿∿∿∿∿∿\n∿∿∿∿∿∿∿∿"
    g.tirer(2, 3)
    assert str(g) == "∿∿∿∿∿∿∿∿\n∿∿∿∿∿∿∿∿\n∿∿∿x∿∿∿∿\n∿∿∿∿∿∿∿∿\n∿∿∿∿∿∿∿∿"
