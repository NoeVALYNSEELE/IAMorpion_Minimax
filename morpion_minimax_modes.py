import random #aléatoire
import os #accède au nom du système s'exploitation
import time #permet de rajouter la fonction attendre



def effacer_ecran():
    # Efface l'écran de la console
    if os.name == 'nt':  # Pour Windows
        os.system('cls')
    else:  # Pour Unix/Linux/Mac
        os.system('clear')

def initialiser():
    return [["_","_","_"], #crée une liste de liste pour stocker l'état de chaque case
              ["_","_","_"],
              ["_","_","_"]]

def afficher_grille(grille, effacer=True):
     if effacer:
        effacer_ecran() #efface l'écran
     for index, ligne in enumerate(grille): #répète le nombre de ligne dans la liste fois (3) et établit l'élément ligne comme un élément de la liste grille(ici les sous-listes) + ajoute un index pour savoir où en est on dans la liste
        print(" | ".join(map(str, ligne))) #affiche les bars assemblé à l'élément actuel (ligne) grâce à join et vérifie que ce sont bie des caractères
        if index < len(grille)-1: #si ce n'est pas la dernière ligne
            print("-"*9) #affiche 9 trait



def demander_coup():
    while True:
        try:
            ligne = int(input("Choisissez une ligne (1, 2 ou 3) : ")) - 1 #demande la ligne et commence à compter par 1
            colonne = int(input("Choisissez une colonne (1, 2 ou 3) : ")) - 1
            if 0 <= ligne < 3 and 0 <= colonne < 3: #si dans la grille
                return ligne, colonne
            else:
                print("Les coordonnées doivent être entre 1 et 3.")
        except ValueError: #si tout autre symbole
            print("Veuillez entrer des nombres valides.") 

def coup_valide(grille, ligne, colonne):
    return 0 <= ligne < 3 and 0 <= colonne < 3 and grille[ligne][colonne] == "_"

    #if 0<=ligne<3 and 0<= colonne<3 and grille[ligne][colonne]=="_": #si le coup est dans la grille et que il est sur une case inoccupé ("_")
        #return True 
    #return False

def verifier_victoire(grille):
    #verification des lignes
    for ligne in grille: #définit une liste ligne qui augmente de 1 à chaque fois
        if ligne[0] == ligne[1] == ligne[2] and ligne[0] != "_" : #si trois caractères sont identiques sur une ligne et sont différent d'une case vierge
            return ligne[0]                                           #le premier[x] représente l'élément en position x de ligne (ligne étant défini automatiquement par la boucle for)
    
    #vérification des colonnes
    for col in range(3):
        if grille[0][col] == grille[1][col] == grille[2][col] and grille[0][col] != "_": #colonne est l'élément itérer, il part de 0 (colonne 0) et augment de 1 à chaque boucle, c'est une sorte de variable juste pour cette boucle
            return grille[0][col]                                                                 # le deuxième [x] représente l'élément à x position de la sous-liste
    
    #vérification des diagonales
    #diagonal 1
    if grille[0][0]==grille[1][1] == grille[2][2] and grille[0][0] != "_":
        return grille[0][0]
    #diagonal 2
    if grille[0][2]==grille[1][1]==grille[2][0] and grille[0][2] != "_":
        return grille[0][2]
    
    return None #personne n'a gagné
    
def grille_pleine(grille):
    for ligne in grille:
        if "_" in ligne: #si il reste des cases vides
            return False
    return True


"""
Minimax est un algorithme qui simule tous les coups possibles dans un jeu à tour de rôle pour maximiser le score de l'IA et minimiser celui de l'adversaire, en choisissant le meilleur coup à chaque étape.
pour chaque possibilité minimax regarde le résultat et garde celui qui le fait gagner
 L'objectif de cette fonction est d'explorer toutes les possibilités de coups dans une partie de morpion
 pour trouver le meilleur coup possible, en alternant entre le joueur et le bot.

 1. L'algorithme explore récursivement chaque coup possible à partir de l'état actuel du jeu,
    simulant le déroulement de la partie jusqu'à ce qu'une situation finale soit atteinte (victoire, défaite ou match nul).
    Lorsqu'une situation finale est atteinte, un score est attribué à cette situation :
      - +1 pour une victoire du bot
      - -1 pour une victoire du joueur
      -  0 pour un match nul.
 2. Ensuite, l'algorithme "remonte" dans l'arbre des possibilités :
    - Si c'est au tour du **bot** de jouer (maximisation), il choisit le coup avec le **meilleur score possible** (le plus élevé),
      car le bot cherche à gagner ou à obtenir le meilleur résultat possible.
    - Si c'est au tour du **joueur** de jouer (minimisation), il choisit le coup avec le **pire score possible** (le plus bas),
      car le joueur cherche à empêcher le bot de gagner, ou à obtenir le résultat le plus défavorable pour le bot.

 À la fin de l'exécution de Minimax, le score calculé permet au bot de déterminer quel est le meilleur coup à jouer
 en tenant compte de tous les coups possibles pour les deux joueurs et de leurs conséquences jusqu'à la fin de la partie.

 Le score à chaque niveau est donc calculé lors de la simulation d'un coup jusqu'à la situation finale du jeu,
 puis ces scores sont comparés pour sélectionner le meilleur coup en fonction du joueur ou du bot.
"""
def minimax(grille, profondeur, maximiser, max_symbole): # Fonction Minimax -> VA REGARDER TOUS LES COUPS POSSIBLE ET LEUR ATTRIBUER UN SCORE!!! + en mode 6, va regarder quelle symbole est le minimax en train de jouer pour adapter les coups en concéquent
    gagnant = verifier_victoire(grille)     
    if gagnant == max_symbole:
        return 10-profondeur #score en cas de victoire en fonction de la profondeur(coup joué) ->incite minimax à privilégier les victoires rapides (stratégie défensive)
    elif gagnant is not None:
        return profondeur-10 #score en cas de défaite en fonction de la profondeur(coup joué) ->incite à éviter les risques de défaites rapides
    elif grille_pleine(grille): #si il y a match nul
        return 0
    
    min_symbole = "O" if max_symbole == "X" else "X" # Le symbole du min est l'autre que celui du minimax en train de jouer
    
    if maximiser:   #si c'est le tour du bot dans la simulation -> cherche le meilleur coup
        meilleur_score = -float("inf") #initialise le score à - l'infini car on cherche à le maximiser
        for i in range(3): #parcourt toute la grille i=ligne j=colonne
            for j in range(3):
                if grille[i][j]== "_": #si une case est libre
                    grille[i][j] = max_symbole #simule le coup du bot
                    score = minimax(grille, profondeur +1, False, max_symbole)
                    # On va refaire minimax() en alternant simulationBot et simulationJoueur jusqu'à ce que la simulation soit terminé sachant que simbot veut faire le meilleur coup et simjoueur veut faire le coup aboutissant au score le plus petit pour le bot. Quand c'est fait, chaque étape de simulation va attribuer un score à chaque possibilités, ce qui nous permet de remonter l'arbre et de voir le chemin optimal (voir shéma)
                    # Appel récursif de la fonction minimax pour simuler le prochain coup de l'adversaire (profondeur +1).
                    # La fonction va évaluer tous les coups possibles pour l'adversaire en changeant l'état de la grille.
                    # L'argument False indique que c'est au tour de l'adversaire de jouer (et non de l'IA).
                    # Cela permet à minimax de chercher à minimiser le score de l'IA en simulant les choix de l'adversaire.   
                    grille[i][j] = "_" #on annule le coup(Backtracking)
                    meilleur_score = max(meilleur_score, score) #on met à jour le meilleur score
        return meilleur_score
    
    else: #si c'est le tour du joueur X dans la simulation / donc si il y a eu l'appel récursif -> cherche le meilleur coup pour le joueur pour pouvoir comparer notre stratégie avec le coup le + dangereux
        meilleur_score = float("inf") #initialise le score à + l'infini car X cherche à faire perdre 0 et donc lui donner le + petit score
        for i in range(3): #parcourt toute la grille i=ligne j=colonne
            for j in range(3):
                if grille[i][j]== "_":
                    grille[i][j] = min_symbole #simule le coup du joueur
                    score = minimax(grille, profondeur +1, True, max_symbole) #appel récursif de minimax (voir plus  haut + shéma)
                    grille[i][j] = "_" #on annule le coup(backtracking)
                    meilleur_score = min(meilleur_score, score) #on garde le coup qui fait perdre le plus de point = qui serait leplus stratégique pour faire perdre le bot
                    #print(f"profondeur {profondeur}: Joueur (Min), score évalué: {score}, Meilleur score: {meilleur_score}")
        return meilleur_score

def meilleur_coup(grille, symbole): #regarde tous les coups trouové pas minimax et garde celui avec le meilleur score + symbole c'est le symbole du minimax en train de jouer, elle est déterminé dans le paramétrage de cette fonction dans le mode 6 dans la main boucle
    #Minimax va commencer par le coin. En effet, bien que le centre soit l'option optimale pour un joueur humain, l'algorithme Minimax n'est pas limité par des principes humains. Il analyse tous les coups possibles et choisit celui qui mène à une position avec la meilleure probabilité de victoire à partir des évaluations calculées.
    meilleur_score = -float("inf") #on veut maximiser le coup donc on met le score à -l'infini
    coup = None #On initialise la variable coup à rien du tout
    for i in range(3): #parcourt toute la grille i=ligne j=colonne
            for j in range(3):
                if grille[i][j]== "_":
                    grille[i][j] = symbole #simule que le bot joue ici
                    score = minimax(grille, 0, False, symbole) #on appelle la fonction minimax pour voir ce que ça donne comme score + c'est ici qu'on va fournir à la fonction minimax le symbole du minimax en train de jouer
                    grille[i][j]="_" #annule le coup
                    if score > meilleur_score: #on garde le meilleur coup qu'on a trouvé
                        meilleur_score = score
                        coup = (i, j)
    return coup



def random_bot(grille):
    coups_possible =[]
    for i in range(3):
        for j in range(3):
            if grille[i][j] == "_":
                coups_possible.append((i, j)) # .apend sert à ajouter le coup possible à la fin de la liste
    return random.choice(coups_possible) #on choisit un coup aléatoire parmi la liste des coups possibles



def animation_reflexion(type_bot): #va faire l'animation en affichant le nom du bot qui joue (minimax ou random)
    print(f"{type_bot} réfléchit", end="") # end="" permet d'éviter que python mettent automatiquement un espace derrière ce print et ça permet d'afficher plusieurs print sur la même ligne sans passer à la ligne suivante!!!
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True) #par défaut, print est mise dans une mémoire tampon, ce empeche l'affichage immédiat dans la console. Flush force la vidange du tampon et afficheimmédiatement le print == rafraichissement d'écran en scratch
    print()



def mode_de_jeu():
    print("Choisissez un mode de jeu :")
    print("1. Joueur vs Joueur (PvP)")
    print("2. Joueur vs Random")
    print("3. Joueur vs Minimax")
    print("4. Random vs Minimax")
    print("5. Random vs Random")
    print("6. Minimax vs Minimax")

    while True:
        choix = input("Entrez le numéro du mode choisi : ")
        if choix in ["1", "2", "3", "4", "5", "6"]:
            return int(choix)
        else:
            print("Choix invalide, veuillez entre un nombre entre 1 et 6.")




#boucle principale
def morpion():
    grille = initialiser() #crée une liste de liste pour stocker l'état de chaque case
    joueur = random.choice(["X", "O"]) #joueur qui commence(tiré au harsard)
    
    while True:
        afficher_grille(grille)
        
        if mode == 1: #PvP
            print(f"Tour du joueur {joueur}")
            ligne, colonne = demander_coup()
            if coup_valide(grille, ligne, colonne):
                grille[ligne][colonne] = joueur
            else:
                print("Case invalide, réessayer !")
                continue
        
        elif mode == 2: #Joueur vs Random
            if joueur == "X":
                print(f"Tour du joueur {joueur}")
                ligne, colonne = demander_coup()
                if coup_valide(grille, ligne, colonne):
                    grille[ligne][colonne] = joueur
                else:
                    print("Case invalide, réessayer !")
                    continue
            else:
                animation_reflexion("Random")
                ligne, colonne = random_bot(grille) # Utilise une fonction random pour générer un coup aléatoire
                grille[ligne][colonne] = "O"
        
        elif mode == 3: #Joueur vs Minimax
            if joueur == "X": # tour du joueur humain
                print(f"Tour du joueur {joueur}")
                ligne, colonne = demander_coup() 
                if coup_valide(grille, ligne, colonne):
                    grille[ligne][colonne]="X" #place le symbole du joueur dans la case choisi
                else:
                    print("Case invalide, réessayer !")
                    continue
            else: #tour du robot
                animation_reflexion("Minimax")
                ligne, colonne = meilleur_coup(grille, "O") #on regarde le meilleur coup
                grille[ligne][colonne]="O" #mettre le coup choisi par minimax
        
        elif mode == 4: #Random vs Minimax
            if joueur == "X":
                animation_reflexion("Random")
                ligne, colonne = random_bot(grille)
                grille[ligne][colonne] = "X"
            else:
                animation_reflexion("Minimax")
                ligne, colonne = meilleur_coup(grille, "O")
                grille[ligne][colonne] = "O"
        
        elif mode == 5: #Random vs Random
            if joueur == "X":
                animation_reflexion("Random")
                ligne, colonne = random_bot(grille)
                grille[ligne][colonne] = "X"
            else:
                animation_reflexion("Random")
                ligne, colonne = random_bot(grille)
                grille[ligne][colonne] = "O"

        elif mode == 6: #Minimax vs Minimax
                animation_reflexion("Minimax")
                ligne, colonne = meilleur_coup(grille, joueur) #ici, on va envoyer à la fonction meilleur coup quelle est le symbole su minimax en train de jouer (il va lui même envoyer cette info à l'algorythme minimax)
                grille[ligne][colonne] = joueur
        
        #vérification de victoire et de fin de partie
        if verifier_victoire(grille):
            afficher_grille(grille)
            print(f"Le joueur {joueur} a gagné !")
            initialiser()
            break
            
        elif grille_pleine(grille):
            afficher_grille(grille)
            print("Match nul !")
            initialiser()
            break
            
        joueur = "O" if joueur == "X" else "X" #on change de joueur / ou le symbole du minimax en mode 6 -> ce qui équivaut à un changement de joueur

if __name__ == "__main__":
    while True:
        mode = mode_de_jeu()
        morpion()
        rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower() #lower passe tout caractères en minuscule
        if rejouer != "o":
            break
    # Ferme le terminal à la fin de l'exécution
    if os.name == 'nt':  # Pour Windows
        os.system('exit')
    else:  # Pour Unix/Linux/Mac
        os.system('kill $$')
