"main.py exécute le jeu"
import pygame # Importer pygame
pygame.init() # Initialiser pygame
from jeu import * # Importer le contenu du fichier jeu.py
from tkinter import messagebox # Importer le module messagebox de tkinter


# Exécuter une première partie
jeu = Jeu(titre="Bataille navale !", largeur=800, hauteur=600)
jeu.executer()
del jeu
pygame.quit()
# Demander au joueur s'il souhaite rejouer, si c'est le cas entrer dans une boucle
while True:
    rejouer = messagebox.askyesno("Rejouer ?", "Voulez-vous rejouer ?") # Demander au joueur s'il souhaite rejouer et enregistrer la réponse
    if rejouer: # Si le joueur veut rejouer
        # Réinitialiser le jeu
        pygame.init()
        jeu = Jeu(titre="Bataille navale !", largeur=800, hauteur=600)
        jeu.executer()

    else:
        break    