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
            # Si on est sur la bordure horizontale (ligne du haut ou du bas, sauf coins)
            elif i == 0:  # Remplir la première ligne de `-`
                print("-", end="")  # Remplir la première ligne de `-`
            # Si on est sur la bordure verticale (colonne de gauche ou de droite, sauf coins)
            elif j == 0 or j == total_width - 1:
                print("|", end="")  # Afficher un "|"
            # Si on est sur la diagonale droite-gauche (inversée)
            elif i + j == total_width - 1:
                print(" ", end="")  # Laisser un espace vide pour la diagonale inversée
            # Remplir le triangle inférieur gauche avec `#` (au-dessous de la diagonale inversée)
            elif i + j < total_width - 1:  # Remplir le triangle avec la base en bas
                print("#", end="")
            # Remplir le triangle supérieur droit avec `#` (au-dessus de la diagonale inversée)
            elif i + j > total_width - 1:  # Remplir le triangle avec la base en haut
                print("#", end="")
            else:
                print(" ", end="")  # Sinon, laisser un espace
        # Quand on a terminé une ligne, aller à la ligne suivante
        print()

# Demander à l'utilisateur de fournir une taille pour le tapis
n = int(input("Entrez la taille du tapis (n) : "))
draw_diagonal_carpet(n)
