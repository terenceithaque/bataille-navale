"jeu.py contient une classe Jeu qui renferme la logique principale du gameplay."
import pygame # Importer pygame
pygame.init() # Initialiser pygame
from decor import * # Importer decor.py


class Jeu:
    """Classe représentant une partie de bataille navale."""
    def __init__(self, titre:str) -> None:
        """Initilisation du jeu.
        - titre: titre de la fenêtre de jeu
       """

        # Fenêtre du jeu

        self.fenetre = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

     

        # Titre de la fenêtre
        pygame.display.set_caption(titre)

        self.infos_ecran = pygame.display.Info()
        self.largeur_ecran = self.infos_ecran.current_w
        self.hauteur_ecran = self.infos_ecran.current_h
        # Créer le décor du jeu
        self.decor = Decor(image="assets/images/ocean.jpg", largeur_image=self.largeur_ecran, hauteur_image=self.hauteur_ecran)

        # Reste du code du gameplay

    def executer(self) -> None:
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

            # Afficher le décor du jeu
            self.decor.afficher(self.fenetre)
            # Mettre à jour l'affichage
            pygame.display.flip()              
        