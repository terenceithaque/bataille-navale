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

        # Dessiner les lignes verticales
        largeur_surface = surface.get_width()
        print("Largeur de la surface:", largeur_surface)
        for x in range(pos_x, max_x, taille):
            pygame.draw.line(surface, (200, 200, 200), (x, 0), (x, largeur_surface), 1)


        # Dessiner les lignes horizontales
        hauteur_surface = surface.get_height()
        print("Hauteur de la surface:", hauteur_surface)
        for y in range(pos_y, max_y, taille):
            pygame.draw.line(surface, (200, 200, 200), (0, y), (largeur_surface, y), 1)    





