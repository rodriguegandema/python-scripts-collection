# Coding: utf-8
from random import randint
# Simulateur de lancer de paires de dés
def jeu():
    while True:
        choix_du_joueur = input("Lancer le dé ? (oui/non): ").lower()
        if choix_du_joueur == 'oui':
            lancers = (randint(1, 6), randint(1, 6))
            print(lancers)
        elif choix_du_joueur == 'non':
            print("Fin du jeu")
            break
        else:
            print("Saisi Invalide !")
            continue

jeu()