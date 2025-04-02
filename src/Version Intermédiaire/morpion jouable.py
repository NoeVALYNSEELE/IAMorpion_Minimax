def afficher_grille(grille):
     for index, ligne in enumerate(grille): #répète le nombre de ligne dans la liste fois (3) et établit l'élément ligne comme un élément de la liste grille(ici les sous-listes) + ajoute un index pour savoir où en est on dans la liste
        print(" | ".join(map(str, ligne))) #affiche les bars assemblé à l'élément actuel (ligne) grâce à join et vérifie que ce sont bie des caractères
        if index < len(grille)-1: #si ce n'est pas la dernière ligne
            print("-"*9) #affiche 9 trait

def demander_coup():
    ligne = int(input("Choisissez une ligne (1, 2 ou 3) : "))
    colonne = int(input("Choisissez une colonne (1, 2 ou 3) : "))
    ligne = ligne-1
    colonne = colonne-1
    return ligne, colonne

def coup_valide(grille, ligne, colonne):
    if 0<=ligne<3 and 0<= colonne<3 and grille[ligne][colonne]=="_": #si le coup est dans la grille et que il est sur une case inoccupé ("_")
        return True 
    return False

def verifier_victoire(grille):
    #verification des lignes
    for ligne in grille: #définit une liste ligne qui augmente de 1 à chaque fois
        if ligne[0] == ligne[1] == ligne[2] and ligne[0] != "_" : #si trois caractères sont identiques sur une ligne et sont différent d'une case vierge
            return True                                           #le premier[x] représente l'élément en position x de ligne (ligne étant défini automatiquement par la boucle for)
    
    #vérification des colonnes
    for col in range(3):
        if grille[0][col] == grille[1][col] == grille[2][col] and grille[0][col] != "_": #colonne est l'élément itérer, il part de 0 (colonne 0) et augment de 1 à chaque boucle, c'est une sorte de variable juste pour cette boucle
            return True                                                                  # le deuxième [x] représente l'élément à x position de la sous-liste
    
    #vérification des diagonales
    #diagonal 1
    if grille[0][0]==grille[1][1] == grille[2][2] and grille[0][0] != "_":
        return True
    #diagonal 2
    if grille[0][2]==grille[1][1]==grille[2][0] and grille[0][2] != "_":
        return True
    
def grille_pleine(grille):
    for ligne in grille:
        if "_" in ligne: #si il reste des cases vides
            return False
    return True

def morpion():
    grille = [["_","_","_"], #crée une liste de liste pour stocker l'état de chaque case
              ["_","_","_"],
              ["_","_","_"]]
    joueur = "X" #joueur qui commence
    while True:
        afficher_grille(grille)
        print(f"Tour du joueur {joueur}")
        ligne, colonne = demander_coup() 
        if coup_valide(grille, ligne, colonne):
            grille[ligne][colonne]=joueur #place le symbole du joueur dans la case choisi
        else:
            print("Case invalide, réessayer !")
            continue
        if verifier_victoire(grille):
            afficher_grille(grille)
            print(f"Le joueur {joueur} a gagné !")
            break
        elif grille_pleine(grille):
            afficher_grille(grille)
            print("Match nul !")
            break
        joueur = 0 if joueur == "X" else "X"

if __name__ == "__main__":
    morpion()
