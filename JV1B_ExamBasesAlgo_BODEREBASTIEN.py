

myTable = [25,265,4,48972,3,12,5,36,1]

# ------------ Partie I : Tri à bulle ---------------

# Question 1

stockage = myTable[0]
myTable[0] = myTable [1]
myTable[1] = stockage
print(len(myTable))

# Question 2


for i in range (0, len(myTable)) :
    #fonction if rajoutée pour éviter de vérifier le tableau à i+1 quand il est déjà au bout du tableau
    if (i<len(myTable)-1):
        if(myTable[i]>myTable[i+1]):
            stockage = myTable[i]
            myTable[i] = myTable [i+1]
            myTable[i+1] = stockage


# Question 3

for j in range (0, len(myTable)):
    for i in range (0, len(myTable)) :
        if (i<len(myTable)-1):
            if(myTable[i]>myTable[i+1]):
                stockage = myTable[i]
                myTable[i] = myTable [i+1]
                myTable[i+1] = stockage


print(myTable)


# Question 4

# Le tri à bulle est considéré lent car il doit parcourir de nombreuses fois le tableau afin de correctement se trier.
# Là où les autres algorithmes de tri font leur tri au fur et à mesure, ici le programme aura besoin de repasser i*i fois 
# sur le tableau, où i est la longueur du tableau


# ------------ Partie II : Tic Tac Toe ---------------

# Question 1

ligne1=[".",".","."]
ligne2=[".",".","."]
ligne3=[".",".","."]
tableDeJeu=[ligne1,ligne2,ligne3]
print(ligne1)
print(ligne2)
print(ligne3) 

# Question 2

#récupération de la colonne
print("Veuillez selectionner une colone où jouer")
print("Les options sont 1, 2 ou 3")
positionColonneJouee = input()

#vérification de la validité du coup
while((positionColonneJouee != "1") and (positionColonneJouee != "2") and (positionColonneJouee != "3")): 
    print("Veuillez choisir une bonne option")
    print("Les options sont 1, 2 ou 3")
    positionColonneJouee = input()

#récupération de la ligne
print("Veuillez selectionner une ligne où jouer")
print("Les options sont 1, 2 ou 3")
positionLigneJouee = input()

#vérification de la validité du coup
while((positionLigneJouee != "1") and (positionLigneJouee != "2") and (positionLigneJouee != "3")): 
    print("Veuillez choisir une bonne option")
    print("Les options sont 1, 2 ou 3")
    positionLigneJouee = input()

#transformation des inputs en entiers
positionColonneJouee=int(positionColonneJouee)-1
positionLigneJouee=int(positionLigneJouee)-1


tableDeJeu[positionLigneJouee][positionColonneJouee]="X"

print(tableDeJeu)


# Question 3

#clairement y a un moyen plus simple que ça, mais je vois pas pour le moment
if ((ligne1[0] == "X" and ligne1[1] == "X" and ligne1[2] == "X") 
    or (ligne2[0] == "X" and ligne2[1] == "X" and ligne2[2] == "X") 
    or (ligne3[0] == "X" and ligne3[1] == "X" and ligne3[2] == "X")
    or (ligne1[0] == "X" and ligne2[0] == "X" and ligne3[0] == "X")
    or (ligne1[1] == "X" and ligne2[1] == "X" and ligne3[1] == "X")
    or (ligne1[2] == "X" and ligne2[2] == "X" and ligne3[2] == "X")
    or (ligne1[0] == "X" and ligne2[1] == "X" and ligne3[2] == "X")
    or (ligne1[2] == "X" and ligne2[1] == "X" and ligne3[0] == "X")):
        print("joueur 1 à gagné !")

if ((ligne1[0] == "O" and ligne1[1] == "O" and ligne1[2] == "O") 
    or (ligne2[0] == "O" and ligne2[1] == "O" and ligne2[2] == "O") 
    or (ligne3[0] == "O" and ligne3[1] == "O" and ligne3[2] == "O")
    or (ligne1[0] == "O" and ligne2[0] == "O" and ligne3[0] == "O")
    or (ligne1[1] == "O" and ligne2[1] == "O" and ligne3[1] == "O")
    or (ligne1[2] == "O" and ligne2[2] == "O" and ligne3[2] == "O")
    or (ligne1[0] == "O" and ligne2[1] == "O" and ligne3[2] == "O")
    or (ligne1[2] == "O" and ligne2[1] == "O" and ligne3[0] == "O")):
        print("joueur 2 à gagné !")


# Question 4

if (ligne1.__contains__(".") and ligne2.__contains__(".") and ligne3.__contains__(".")):
    print("La partie n'est pas finie !")

else :
    print("fin de la partie")


#le code du tic tac toe complet sera fait sur le document JV1B_ExamBasesAlgo_BODEREBASTIEN_2, pour ne pas être géné par les autres exercices

