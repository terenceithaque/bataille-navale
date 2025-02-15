"jeu.py contient une classe Jeu qui renferme la logique principale du gameplay."
import pygame # Importer pygame
pygame.init() # Initialiser pygame
from decor import * # Importer decor.py
from grille import * # Importer grille.py

class Jeu:
    """Classe représentant une partie de bataille navale."""
    def __init__(self, titre:str) -> None:
        """Initilisation du jeu.
        - titre: titre de la fenêtre de jeu
       """

        # Fenêtre du jeu

        self.fenetre = pygame.display.set_mode((800, 600))

     

        # Titre de la fenêtre
        pygame.display.set_caption(titre)

        self.infos_ecran = pygame.display.Info()
        self.largeur_ecran = self.infos_ecran.current_w
        self.hauteur_ecran = self.infos_ecran.current_h
        # Créer le décor du jeu
        self.decor = Decor(image="assets/images/ocean.jpg", largeur_image=self.largeur_ecran, hauteur_image=self.hauteur_ecran)

        # Grilles du joueur et de l'adversaire
        self.grille_joueur = Grille(n_lignes=11, n_colonnes=11)
        self.grille_joueur_x = self.fenetre.get_width() # Position x de la grille du joueur
        self.grille_joueur_y = self.fenetre.get_height() // 2 # Position y de la grille du joueur


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

                if evenement.type == pygame.MOUSEMOTION:
                    print("Position de la souris :", pygame.mouse.get_pos())    

            # Afficher le décor du jeu
            self.decor.afficher(self.fenetre)

            # Afficher les grilles
            self.grille_joueur.afficher(self.fenetre, 0, self.grille_joueur_y, self.grille_joueur_x, self.fenetre.get_height() , 15)
            # Mettre à jour l'affichage
            pygame.display.flip()              
        