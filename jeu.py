"jeu.py contient une classe Jeu qui renferme la logique principale du gameplay."
import pygame # Importer pygame
pygame.init() # Initialiser pygame


class Jeu:
    """Classe représentant une partie de bataille navale."""
    def __init__(self, titre:str, largeur:int, hauteur:int) -> None:
        """Initilisation du jeu.
        - titre: titre de la fenêtre de jeu
        - largeur: largeur de la fenêtre de jeu
        - hauteur: hauteur de la fenêtre de jeu"""

        # Fenêtre du jeu
        self.fenetre = pygame.display.set_mode((largeur, hauteur))
        # Titre de la fenêtre
        pygame.display.set_caption(titre)

        # Reste du code du gameplay

    def executer(self):
        """Exécute la boucle de jeu."""
        self.execution = True # Variable pour marquer l'état du jeu (en exécution ou non)

        # Boucle de jeu
        while self.execution:
            # Détecter les événements de jeu et réagir en conséquence
            for evenement in pygame.event.get():
                # Si le joueur veut quitter le jeu
                if evenement.type == pygame.QUIT:
                    # Mettre la variable d'exécution à False 
                    self.execution = False

            # Mettre à jour l'affichage
            pygame.display.flip()              
        