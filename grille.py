"grille.py permet de générer une grille de jeu."

from typing import Any


class Grille:
    "Grille de jeu"
    def __init__(self, n_lignes:int, n_colonnes:int) -> None:
        """Initialise la grille
        -n_lignes: nombre de lignes de la grille
        - n_colonnes: nombre de colonnes de la grille"""

        self.contenu = self.generer(n_lignes, n_colonnes, 0) # Contenu de la grille (liste de listes)
        print(self.contenu)

    def generer(self, n_lignes:int, n_colonnes:int, element:int|str) -> list:
        """Génère une liste représentant la grille.
        - n_lignes: nombre de lignes à générer.
        - n_colonnes: nombre de colonnes à générer
        - element: élément à insérer dans chaque case, par exemple 0 ou 1 ->  0 pour rien, 1 pour un élément du jeu quelconque""" 

        self.contenu = [] # Initaliser ou réinitialiser le contenu de la grille

        # Générer les lignes et les colonnes
        for i in range(n_lignes):
            colonne =  []
            for n in range(n_colonnes):
                colonne.append(element)

            self.contenu.append(colonne)


        return self.contenu





