# UML

## Grille v1

```
Grille
--------------------------------------
matrice
--------------------------------------
Grille(nombre_lignes, nombre_colonnes)
afficher()
tirer(x, y)
```

## Grille v2

```
Grille
--------------------------------------
matrice: liste
nombre_colonnes: int
--------------------------------------
Grille(nombre_lignes, nombre_colonnes)
afficher()
tirer(x, y)
```

## Grille v3

```
Grille
--------------------------------------
matrice: liste de caractères
nombre_colonnes: int
vide: str = "∿"
--------------------------------------
Grille(nombre_lignes, nombre_colonnes)
afficher()
tirer(ligne, colonne)
```

afficher() = `__str__` en python

## Grille v4 (avec bateaux)

```
Grille
--------------------------------------
matrice: liste de caractères
nombre_colonnes: int
vide: str = "∿"
--------------------------------------
Grille(nombre_lignes, nombre_colonnes)
afficher()
tirer(ligne, colonne, touche="x")
rentre(bateau: Bateau): bool
ajoute(bateau: Bateau)
```

(rentre ajouté à l'étape F pour le placement aléatoire)

## Bateau

```
Bateau
--------------------------------------
marque: str = "⛵"
ligne: int
colonne: int
longueur: int = 1
vertical: bool = False
--------------------------------------
Bateau(ligne, colonne, longueur=1, vertical=False)
positions(): liste de (ligne, colonne)
chevauche(autre: Bateau): bool
coulé(grille: Grille): bool
```

## Types de bateaux

Les 4 classes héritent de Bateau (flèche vers Bateau).

```
           Bateau
             ^
             |
 +-----------+-----------+-------------+
 |           |           |             |
PorteAvion  Croiseur   Torpilleur   SousMarin
```

```
PorteAvion                       (longueur 4)
--------------------------------------
marque = "🚢"
--------------------------------------
PorteAvion(ligne, colonne, vertical=False)
```

Pareil pour les autres :
- Croiseur : longueur 3, marque "⛴"
- Torpilleur : longueur 2, marque "🚣"
- SousMarin : longueur 2, marque "🐟"
