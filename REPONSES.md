# Réponses aux questions

## Grille

**Proser une méthode pour simuler une matrice à C colonnes et L lignes par une liste.**

On met les lignes les unes à la suite des autres dans une seule liste de taille C * L.
La case (ligne l, colonne c) est à l'indice `l * C + c`.

Dans l'autre sens, l'indice i correspond à la ligne `i // C` et à la colonne `i % C`.

**Quels sont les attributs nécessaires pour implémenter cela dans la classe Grille ?**

`matrice` : la liste
`nombre_colonnes` : pour calculer l'indice

Pas besoin de garder le nombre de lignes, on le retrouve avec `len(matrice) // nombre_colonnes`.
UML mis à jour (version 2).

**Ajoutez ces informations au diagramme UML**

Fait (version 3) : `vide = "∿"` pour une case vierge, `"x"` pour une case tirée.

## Affichage

**Créer la méthode spéciale `__str__`**

On découpe la matrice en morceaux de `nombre_colonnes` cases et on met un retour à la ligne entre chaque.
Dans l'énoncé l'exemple affiche des `.` mais les cases vides sont des `∿`, donc chez nous ça affiche des `∿`.

**Exécutez et corrigez si nécessaire la user story "Plouf dans l'eau"**

Ça marche, il a juste fallu décommenter le `print(grille)`.

