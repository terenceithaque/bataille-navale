"decor.py implémente une classe Decor qui permet de créer un décor pour le jeu"
import pygame # Importer pygame
pygame.init()


class Decor:
    """Classe représentant le décor du jeu"""
    def __init__(self, image="assets/images/ocean.jpg", largeur_image=600, hauteur_image=800, largeur_ecran=600, hauteur_ecran=800) -> None:
        """Initialise le décor du jeu.
        - image: chemin de l'image représentant le décor du jeu.
        - largeur_image: largeur de l'image.
        - hauteur_image: hauteur de l'image.
        - largeur_ecran: largeur de la fenêtre de jeu.
        - hauteur_ecran: hauteur de la fenêtre de jeu."""

        # Charger et redimensionner l'image du décor
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (largeur_image, hauteur_image))

        # Obtenir le rectangle de l'image
        self.rect = self.image.get_rect()
        self.rect.centerx = largeur_image
        self.rect.centery = hauteur_image

    def afficher(self, ecran:pygame.Surface) -> None:
        "Affiche le décor à l'écran."
        ecran.blit(self.image, self.rect)    