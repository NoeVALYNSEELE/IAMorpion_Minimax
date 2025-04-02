import random
import os
import time

def effacer_ecran():
    # Efface l'écran de la console
    if os.name == 'nt':  # Pour Windows
        os.system('cls')
    else:  # Pour Unix/Linux/Mac
        os.system('clear')

def afficher_grille(grille, effacer=True):
    if effacer:
        effacer_ecran()  # Efface l'écran avant d'afficher la grille
    for i, ligne in enumerate(grille):
        ligne_affichee = []
        for j, case in enumerate(ligne):
            if case == "_":
                ligne_affichee.append(f"{i+1},{j+1}")  # Affiche les coordonnées des cases vides
            else:
                ligne_affichee.append(case)
        print(" | ".join(ligne_affichee))
        if i < len(grille) - 1:
            print("-" * 9)

def demander_coup():
    while True:
        try:
            ligne = int(input("Choisissez une ligne (1, 2 ou 3) : ")) - 1
            colonne = int(input("Choisissez une colonne (1, 2 ou 3) : ")) - 1
            if 0 <= ligne < 3 and 0 <= colonne < 3:
                return ligne, colonne
            else:
                print("Les coordonnées doivent être entre 1 et 3.")
        except ValueError:
            print("Veuillez entrer des nombres valides.")

def coup_valide(grille, ligne, colonne):
    return 0 <= ligne < 3 and 0 <= colonne < 3 and grille[ligne][colonne] == "_"

def verifier_victoire(grille):
    # Vérification des lignes
    for ligne in grille:
        if ligne[0] == ligne[1] == ligne[2] and ligne[0] != "_":
            return ligne[0]

    # Vérification des colonnes
    for col in range(3):
        if grille[0][col] == grille[1][col] == grille[2][col] and grille[0][col] != "_":
            return grille[0][col]

    # Vérification des diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] and grille[0][0] != "_":
        return grille[0][0]
    if grille[0][2] == grille[1][1] == grille[2][0] and grille[0][2] != "_":
        return grille[0][2]

    return None

def grille_pleine(grille):
    for ligne in grille:
        if "_" in ligne:
            return False
    return True

def minimax(grille, profondeur, maximiser, max_symbole):
    gagnant = verifier_victoire(grille)
    if gagnant == max_symbole:
        return 10 - profondeur
    elif gagnant is not None:
        return profondeur - 10
    elif grille_pleine(grille):
        return 0

    min_symbole = "O" if max_symbole == "X" else "X"

    if maximiser:
        meilleur_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if grille[i][j] == "_":
                    grille[i][j] = max_symbole
                    score = minimax(grille, profondeur + 1, False, max_symbole)
                    grille[i][j] = "_"
                    meilleur_score = max(meilleur_score, score)
        return meilleur_score
    else:
        meilleur_score = float("inf")
        for i in range(3):
            for j in range(3):
                if grille[i][j] == "_":
                    grille[i][j] = min_symbole
                    score = minimax(grille, profondeur + 1, True, max_symbole)
                    grille[i][j] = "_"
                    meilleur_score = min(meilleur_score, score)
        return meilleur_score

def meilleur_coup(grille, symbole):
    meilleur_score = -float("inf")
    coup = None
    for i in range(3):
        for j in range(3):
            if grille[i][j] == "_":
                grille[i][j] = symbole
                score = minimax(grille, 0, False, symbole)
                grille[i][j] = "_"
                if score > meilleur_score:
                    meilleur_score = score
                    coup = (i, j)
    return coup

def random_coup(grille):
    coups_possible = []
    for i in range(3):
        for j in range(3):
            if grille[i][j] == "_":
                coups_possible.append((i, j))  # Ajoute le coup possible à la fin de la liste
    return random.choice(coups_possible)  # Choisit un coup aléatoire parmi les coups possibles

def animation_reflexion(nom_bot):
    print(f"{nom_bot} réfléchit", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
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
            print("Choix invalide. Veuillez entrer un numéro entre 1 et 6.")

def morpion():
    global parties_jouees  # Utilisation du mot-clé global pour accéder à la variable globale
    parties_jouees += 1
    print(f"Partie numéro : {parties_jouees}")
    
    grille = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    joueur = random.choice(["X", "O"])  # Choisir aléatoirement qui commence
    mode = mode_de_jeu()
    while True:
        afficher_grille(grille)
        if mode == 1:  # Joueur vs Joueur
            print(f"Tour du joueur {joueur}")
            ligne, colonne = demander_coup()
            if coup_valide(grille, ligne, colonne):
                grille[ligne][colonne] = joueur
            else:
                print("Case invalide, réessayer !")
                continue
        elif mode == 2:  # Joueur vs Random
            if joueur == "X":
                print(f"Tour du joueur {joueur}")
                ligne, colonne = demander_coup()
                if coup_valide(grille, ligne, colonne):
                    grille[ligne][colonne] = joueur
                else:
                    print("Case invalide, réessayer !")
                    continue
            else:
                ligne, colonne = random_coup(grille)
                grille[ligne][colonne] = joueur
        elif mode == 3:  # Joueur vs Minimax
            if joueur == "X":
                print(f"Tour du joueur {joueur}")
                ligne, colonne = demander_coup()
                if coup_valide(grille, ligne, colonne):
                    grille[ligne][colonne] = joueur
                else:
                    print("Case invalide, réessayer !")
                    continue
            else:
                animation_reflexion("Minimax")
                ligne, colonne = meilleur_coup(grille, "O")
                grille[ligne][colonne] = joueur
        elif mode == 4:  # Random vs Minimax
            if joueur == "X":
                ligne, colonne = random_coup(grille)
                grille[ligne][colonne] = joueur
            else:
                animation_reflexion("Minimax")
                ligne, colonne = meilleur_coup(grille, "O")
                grille[ligne][colonne] = joueur
        elif mode == 5:  # Random vs Random
            ligne, colonne = random_coup(grille)
            grille[ligne][colonne] = joueur
        elif mode == 6:  # Minimax vs Minimax
            animation_reflexion("Minimax")
            ligne, colonne = meilleur_coup(grille, joueur)
            grille[ligne][colonne] = joueur

        if verifier_victoire(grille):
            afficher_grille(grille)
            print(f"Le joueur {joueur} a gagné !")
            break
        elif grille_pleine(grille):
            afficher_grille(grille)
            print("Match nul !")
            break
        joueur = "O" if joueur == "X" else "X"

if __name__ == "__main__":
    global parties_jouees
    parties_jouees = 0
    while True:
        morpion()
        rejouer = input("Voulez-vous rejouer ? (o/n) : ").lower()
        if rejouer != "o":
            break