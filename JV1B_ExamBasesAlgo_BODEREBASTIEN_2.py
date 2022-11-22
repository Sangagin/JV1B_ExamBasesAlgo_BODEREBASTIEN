#le code du tic tac toe complet sera fait ici, pour ne pas être géné par les autres exercices





ligne1=[".",".","."]
ligne2=[".",".","."]
ligne3=[".",".","."]
tableDeJeu=[ligne1,ligne2,ligne3]

victoire=False
tourActuel="X"

print("\n")
print("Une petite partie de Tic Tac Toe ?")
print("Le joueur aux X commence")

#début de la boucle de partie
while(victoire==False):
    print("")
    print("C'est au tour du joueur aux ",tourActuel)
    print("")
    print("Veuillez selectionner une colone où jouer")
    print("Les options sont 1, 2 ou 3")
    positionColonneJouee = input()

    #vérification de la validité du coup des colones
    while((positionColonneJouee != "1") and (positionColonneJouee != "2") and (positionColonneJouee != "3")): 
        print("")
        print("Veuillez choisir une bonne option")
        print("")
        print("Veuillez selectionner une colone où jouer")
        print("Les options sont 1, 2 ou 3")
        positionColonneJouee = input()

    #récupération de la ligne
    print("")
    print("Veuillez selectionner une ligne où jouer")
    print("Les options sont 1, 2 ou 3")
    positionLigneJouee = input()

    #vérification de la validité du coup des lignes
    while((positionLigneJouee != "1") and (positionLigneJouee != "2") and (positionLigneJouee != "3")): 
        print("")
        print("Veuillez choisir une bonne option")
        print("Veuillez selectionner une ligne où jouer")
        print("Les options sont 1, 2 ou 3")
        positionLigneJouee = input()

    #transformation des inputs en entiers
    positionColonneJouee=int(positionColonneJouee)-1
    positionLigneJouee=int(positionLigneJouee)-1


    #vérification qu'il n'y a pas déjà un pion sur cette case
    if(tableDeJeu[positionLigneJouee][positionColonneJouee]=="."):
        #placement des pions et changement de joueur
        if(tourActuel=="X"):
            tableDeJeu[positionLigneJouee][positionColonneJouee]="X"
            print("")
            print(ligne1)
            print(ligne2)
            print(ligne3)
            tourActuel="O"
        else:
            tableDeJeu[positionLigneJouee][positionColonneJouee]="O"
            print("")
            print(ligne1)
            print(ligne2)
            print(ligne3)
            tourActuel="X"

    else:
        print("")
        print("Il y a déjà un pion sur cette case !")
        print("Veuillez choisir une autre case.")

    #vérification de victoire ou non
    if ((ligne1[0] == "X" and ligne1[1] == "X" and ligne1[2] == "X") 
        or (ligne2[0] == "X" and ligne2[1] == "X" and ligne2[2] == "X") 
        or (ligne3[0] == "X" and ligne3[1] == "X" and ligne3[2] == "X")
        or (ligne1[0] == "X" and ligne2[0] == "X" and ligne3[0] == "X")
        or (ligne1[1] == "X" and ligne2[1] == "X" and ligne3[1] == "X")
        or (ligne1[2] == "X" and ligne2[2] == "X" and ligne3[2] == "X")
        or (ligne1[0] == "X" and ligne2[1] == "X" and ligne3[2] == "X")
        or (ligne1[2] == "X" and ligne2[1] == "X" and ligne3[0] == "X")):
            print("")
            print("joueur 1 à gagné !")
            victoire=True


    if ((ligne1[0] == "O" and ligne1[1] == "O" and ligne1[2] == "O") 
        or (ligne2[0] == "O" and ligne2[1] == "O" and ligne2[2] == "O") 
        or (ligne3[0] == "O" and ligne3[1] == "O" and ligne3[2] == "O")
        or (ligne1[0] == "O" and ligne2[0] == "O" and ligne3[0] == "O")
        or (ligne1[1] == "O" and ligne2[1] == "O" and ligne3[1] == "O")
        or (ligne1[2] == "O" and ligne2[2] == "O" and ligne3[2] == "O")
        or (ligne1[0] == "O" and ligne2[1] == "O" and ligne3[2] == "O")
        or (ligne1[2] == "O" and ligne2[1] == "O" and ligne3[0] == "O")):
            print("")
            print("joueur 2 à gagné !")
            victoire=True

    if (ligne1.__contains__(".") or ligne2.__contains__(".") or ligne3.__contains__(".")):
        print("")

    else :
        print("")
        print("C'est une égalité !")
        print("fin de la partie")
        victoire=True


# Question 4

# Si l'on souhaite créer un jeu de puissance 4 il faudra :
# - augmenter la taille des lignes
# - faire en sorte de forcer le placement des pions sur la position la plus basse de chaque colonne 
#       (en enlevant le choix de la ligne puis en forçant le placement en vérifiant si un pion est déjà présent, cela se fait facilement)
# - augmenter la detection de victoire à 4 pions















