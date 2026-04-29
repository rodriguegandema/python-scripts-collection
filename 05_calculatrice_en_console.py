# Coding: utf-8

def addition(nbre1, nbre2):
	return nbre1 + nbre2
	
def soustraction(nbre1, nbre2):
	return nbre1 - nbre2
	
def multiplier(nbre1, nbre2):
	return nbre1 * nbre2
	
def division(nbre1, nbre2):
	return nbre1 / nbre2
	
def calculator():
	print("============================")
	print("======= CALCULATRICE =======")
	print("============================")
	while True:
		newProgram = input("\n-- Effectuez un nouveau calcul [O/n] : ").upper()
		if newProgram != 'O':
			print("\n-- Fin du programme...")
			break
		while True:
			nbre1 = input("-- Entrez un nombre : ").replace(',','.')
			nbre2 = input("-- Entrez un second nombre : ").replace(',','.')
			try:
				nbre1 = float(nbre1)
				nbre2 = float(nbre2)
				choixOperateur = input("-- Choisissez un opérateur [+, -, *, /] : ")
				match choixOperateur:
					case '+':
						resultat = addition(nbre1, nbre2)
						break
					case '-':
						resultat = soustraction(nbre1, nbre2)
						break
					case '*':
						resultat = multiplier(nbre1, nbre2)
						break
					case '/':
						try:
							resultat = round(division(nbre1, nbre2), 3)
							break
						except ZeroDivisionError:
							print("\n-- Erreur : division impossible")
					case default:
						print("\n-- Erreur: opérateur indisponible !")
			except ValueError:
				print("\n-- Veuillez entrer des nombres\n")
		
		print(f"\n-- Le résultat est : {resultat}") # Afficher les résultats des opérations
	
if __name__ == "__main__":
	calculator()
