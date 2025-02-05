"main.py exécute le jeu"
import pygame # Importer pygame
pygame.init() # Initialiser pygame
from jeu import * # Importer le contenu du fichier jeu.py


# Exécuter une première partie
jeu = Jeu(titre="Bataille navale !", largeur=800, hauteur=600)
jeu.executer()

# Demander au joueur s'il souhaite rejouer, si c'est le cas entrer dans une boucle
