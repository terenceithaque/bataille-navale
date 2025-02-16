"grille.py permet de générer une grille de jeu."
import pygame
pygame.init
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
    
    def afficher(self, surface:pygame.Surface, pos_x:int, pos_y:int, max_x:int, max_y:int, taille:int) -> None:
        """Affiche la grille sur une surface pygame.
        - surface: Element d'affichage cible pygame.Surface
        - pos_x: position x de départ
        - pos_y: position y de départ
        - max_x: position x maximale
        - max_y: position y maximale
        - taille: taille des lignes de la grille"""

        largeur_surface = surface.get_width()
        hauteur_surface = surface.get_height()
        hauteur_max = hauteur_surface // 2
        # Dessiner les lignes verticales
        
        #print("Largeur de la surface:", largeur_surface)
        for x in range(pos_x, max_x, taille):
            pygame.draw.line(surface, (200, 200, 200), (x, pos_y), (x, max_y), 1)


        # Dessiner les lignes horizontales
        hauteur_surface = surface.get_height()
        #print("Hauteur de la surface:", hauteur_surface)
        for y in range(pos_y, max_y, taille):
            pygame.draw.line(surface, (200, 200, 200), (pos_x, y), (min(max_x, largeur_surface), y), 1)


    def position_absolue(self, pos_relative="A1") -> tuple:
        """Traduit une position relative (par exemple, 'A1') en position absolue (par exemple, (0, 0)). Renvoie un tuple.
        - pos_relative: chaîne de caractères contenant la position relative à traduire."""


        # Assertions
        assert (len(pos_relative) >= 2), "La position relative doit contenir au moins deux éléments."
        assert (type(pos_relative).__name__ == "str"), "La position relative doit être une chaîne de caractères."
        assert (int("".join(pos_relative[1:]))), "Les éléments après l'indice zéro doivent être traitables comme des entiers."

        pos_relative = pos_relative.upper() # Convertir la position relative en majuscule.s
        pos_absolue = () # Tuple contenant la position absolue calculée.
        
        # Positions numériques correspondantes aux lettres, compte à partir de zéro.
        pos_lettres = {"A": 0,
                       "B":1,
                       "C":2,
                       "D":3,
                       "E":4,
                       "F":5,
                       "G":6,
                       "H":7,
                       "I":8,
                       "J":9,
                       "K":10}
        
        # Positions numériques, converties en chaînes de caractères
        pos_numeriques = [str(i) for i in range(len(self.contenu))]

        # Convertir la position relative en position absolue à l'aide des données.
        ligne = 0
        colonne = 0
        for valeur in pos_relative:
            # Si la valeur actuelle est une lettre
            if valeur in pos_lettres.keys():
                ligne = pos_lettres[valeur] # La ligne correspond à la position absolue de la lettre

            # Si la valeur est une position numériques
            elif valeur in pos_numeriques:
                 colonne = int("".join(pos_relative[1:])) - 1  # La colonne correspond à la position absolue de la valeur numérique


        pos_absolue = (ligne, colonne)
        return pos_absolue


        

        


    def est_vide(self, colonne=0, ligne=0) -> bool:
        "Vérifie si la case aux coordonées (ligne, colonne) est vide dans la ligne est vide. Si aucune ligne ou colonne n'est spécifiée, vérifie la première ligne entièremment. Renvoie un booléen."
        # Assertions
        assert (type(colonne).__name__ in ["int", "NoneType"]), "case doit être de type int ou NoneType."

        if colonne: # Si une colonne est spécifiée
            if self.contenu[ligne][colonne] > 0:
                return False
            
            return True
        
        else: # Sinon, vérifier la ligne entière
            return all(case <= 0 for case in self.contenu[ligne])   








