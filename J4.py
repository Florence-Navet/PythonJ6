def draw_diagonal_carpet(size):
    # Largeur totale du tapis, y compris le contour
    total_width = size + 2  # On ajoute 2 pour les bordures

    # Parcourir chaque ligne du tapis
    for i in range(total_width):
        # Parcourir chaque colonne de la ligne actuelle
        for j in range(total_width):
            # Si on est dans un coin (haut-gauche, haut-droite, bas-gauche, bas-droite)
            if (i == 0 or i == total_width - 1) and (j == 0 or j == total_width - 1):
                print("+", end="")  # Afficher un "+"
            # Remplir la première ligne de `-`
            elif i == 0:
                print("-", end="")  # Remplir la première ligne de `-`
            # Remplir la dernière ligne de `-`, sauf les coins
            elif i == total_width - 1:
                if j == 0 or j == total_width - 1:
                    print("+", end="")  # Coins de la dernière ligne
                else:
                    print("-", end="")  # Remplir avec des tirets sauf pour les coins
            # Si on est sur la bordure verticale (colonne de gauche ou de droite, sauf coins)
            elif j == 0 or j == total_width - 1:
                print("|", end="")  # Afficher un "|"
            # Si on est sur la diagonale vide, laisser un espace
            elif i - 1 == j - 1:
                print(" ", end="")  # Laisser un espace vide pour la diagonale
            # Remplir les triangles de # (triangle supérieur gauche)
            elif i - 1 < j - 1:
                print("#", end="")  # Remplir le triangle supérieur gauche avec `#`
            # Remplir le triangle inférieur droit avec # (partie sous la diagonale)
            elif i - 1 > j - 1:
                print("#", end="")  # Remplir le triangle inférieur droit avec `#`
            else:
                print(" ", end="")  # Sinon, laisser un espace
        # Quand on a terminé une ligne, aller à la ligne suivante
        print()

# Demander à l'utilisateur de fournir une taille pour le tapis
n = int(input("Entrez la taille du tapis (n) : "))
draw_diagonal_carpet(n)


