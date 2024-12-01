L = int(input("Veuillez entrer le nombre de lignes:"))


for i in range(1, L + 1):
    # Espaces avant les barres pour centrer le triangle
    for j in range(1, L - i + 1):
        print(" ", end="")  # Espaces avant les barres
    
    # Affichage des barres et des underscores
    if i == 1:
        # Le sommet : une seule ligne avec /\
        print("/\\")
        
    else:
        # Barre gauche (/), espaces entre, et barre droite (\\)
        print("/", end="")
        for j in range(1, 2 * i - 1):
            if i == L:
                # Pour la dernière ligne (base), mettre des underscores (_)
                print("_", end="")
            else:
                print(" ", end="")
        print("\\")


