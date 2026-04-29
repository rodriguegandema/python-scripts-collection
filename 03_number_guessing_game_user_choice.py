# Coding: utf-8
from random import randint

def demander_intervalle():
    while True:
        try:
            minimum = int(input("Entrez un nombre entier minimum: "))
            maximum = int(input("Entrez un nombre entier maximum: "))
            if minimum >= maximum:
                print("Le minimum doit être inférieur au maximum.")
                continue
            return minimum, maximum
        except ValueError:
            print("Saisie invalide !")

def jeu():
    print("Jeu de dévinette")
    minimum, maximum = demander_intervalle()
    tirage = randint(minimum, maximum)
    compteur = 0
    
    while True:
        choix = input(f"Dévine un nombre entre {minimum} et {maximum} (S pour quitter): ").upper()
        if choix == 'S':
            print("Fin du jeu")
            break
        if not choix.isnumeric():
            print("Saisie invalide !")
            continue
        
        choix = int(choix)
        compteur += 1
        
        if choix == tirage:
            print(f"Félicitations ! Tu as trouvé en {compteur} tentative(s).")
            break
        elif choix > tirage:
            print("Plus Bas !")
        else:
            print("Plus Haut !")
         
jeu()