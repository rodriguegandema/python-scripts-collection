# Coding: utf-8

"""
	Projet n* 3 : To-Do List Application
"""

def toDoList():
	print("===== TO-DO LIST APPLICATION =====")
	lancerApp = input("-- Voulez-vous ouvrir une nouvelle session ? [O/n] : ").upper()
	if lancerApp != 'O':
		raise SystemExit("\n-- FIN DU PROGRAMME")
	user_to_do_list = []
	while True:
		print("----- Todo List Menu : -----")
		print("1. Voir les tâches\n2. Ajouter une tâche\n3. Supprimer une tâche\n4. Fermer la session")
		userChoice = input("\n-- Entrez votre choix (de 1 à 4) : ")
		try:
			userChoice = int(userChoice)
			match userChoice:
				case 1:
					print(f"-!- Voici vos tâches en attente : \n{user_to_do_list}\n")
				case 2:
					addTask = input("-!- Saisissez une nouvelle tâche : ")
					user_to_do_list.append(addTask)
				case 3:
					deleteTask = input("-!- Saisissez la tâche à supprimer : ")
					if len(user_to_do_list) == 0:
						print("-- Attention : Liste vide...")
					user_to_do_list.remove(deleteTask)
				case 4:
					print("\n-- FIN DE LA SESSION")
					break
				case default:
					print("-- Choix invalide. Réessaie !")
		except ValueError:
			print("\n-!- Erreur : Choix invalide. Réessaie -!-\n")
			
	
if __name__ == "__main__":
	toDoList()
