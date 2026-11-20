from main import placer_bateaux, NB_LIGNES, NB_COLONNES
from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin


def test_placer_bateaux():
    # on le fait plusieurs fois vu que c'est aléatoire
    for _ in range(50):
        g = Grille(NB_LIGNES, NB_COLONNES)
        bateaux = placer_bateaux(g, [PorteAvion, Croiseur, Torpilleur, SousMarin])

        assert len(bateaux) == 4
        assert type(bateaux[0]) == PorteAvion
        assert type(bateaux[3]) == SousMarin

        for b in bateaux:
            assert g.rentre(b)
            for autre in bateaux:
                if b != autre:
                    assert not b.chevauche(autre)
