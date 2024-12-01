def draw_diagonal_carpet(size):
    # Largeur totale du tapis, y compris le contour.
    total_width = size + 2

    # Parcourir chaque ligne du tapis
    for i in range(total_width):
        # Parcourir chaque colonne de la ligne actuelle
        for j in range(total_width):
            # Si on est dans un coin (haut-gauche, haut-droite, bas-gauche, bas-droite)
            if (i == 0 or i == total_width - 1) and (j == 0 or j == total_width - 1):
                print("+", end="")  # Afficher un "+"
            # Si on est sur une bordure horizontale (ligne du haut ou du bas, sauf coins)
            elif i == 0 or i == total_width - 1:
                print("-", end="")  # Afficher un "-"
            # Si on est sur une bordure verticale (colonne de gauche ou de droite, sauf coins)
            elif j == 0 or j == total_width - 1:
                print("|", end="")  # Afficher un "|"
            # Si on est sur la diagonale vide
            elif i - 1 == j - 1:
                print(" ", end="")  # Laisser vide avec un espace
            # Zone supérieure droite (triangle inversé)
            elif i - 1 < j - 1:
                print("#", end="")  # Triangle supérieur droit
            # Zone inférieure gauche (triangle inversé)
            else:
                print("#", end="")  # Triangle inférieur gauche
        # Quand on a terminé une ligne, aller à la ligne suivante
        print()

# Demander à l'utilisateur de fournir une taille pour le tapis
n = int(input("Entrez la taille du tapis (n) : "))
draw_diagonal_carpet(n)
