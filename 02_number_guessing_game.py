# Coding: utf-8

from random import randint

"""
	Projet n*2 : Jeu de dévinette (Nombres) en console <>
	-- [Normal Version]
"""

def guessingGame():
	print("===== NUMBER GUESSING GAME [Vous avez 5 tentatives !] =====")
	while True:
		lancerJeu = input("-- Jouer une partie [O/n] ? : ").upper()
		if lancerJeu != 'O':
			print("\n-- FIN DU PROGRAMME")
			break
		tirages = randint(1, 10)
		compteur = 0
		while True:
			intervalle = '1 et 10'
			nbreAleatoire = input(f"\n-- Dévine le nombre (compris entre {intervalle}) : ")
			try: 
				nbreAleatoire = int(nbreAleatoire)
				compteur += 1
				if compteur == 5:
					print("\n-- GAME OVER | Vous avez écoulé vos cartes !")
					print(f"-- La bonne réponse était : {tirages}\n")
					break
				elif nbreAleatoire < tirages:
					print("-- Plus Haut ! Réessaie...")
				elif nbreAleatoire > tirages:
					print("-- Plus Bas ! Réessaie...")
				elif nbreAleatoire == tirages:
					print("\n-- BRAVO !!!\n")
					print(f"-- Vous avez réussi après {compteur} tentatives.\n")
					break
			except ValueError:
				print(f"\n-- Veuillez entrer un nombre entier compris entre {intervalle}")
		
if __name__ == "__main__":
	guessingGame()
