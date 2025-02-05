"decor.py implémente une classe Decor qui permet de créer un décor pour le jeu"
import pygame # Importer pygame
pygame.init()


class Decor:
    """Classe représentant le décor du jeu"""
    def __init__(self, image="assets/images/ocean.jpg", largeur_image=600, hauteur_image=800):
        """Initialise le décor du jeu.
        - image: chemin de l'image représentant le décor du jeu.
        - largeur_image: largeur de l'image.
        - hauteur_image: hauteur de l'image."""

        