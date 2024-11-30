def draw_triangle(height):
    if height < 1:
        print("La hauteur doit être supérieure ou égale à 1.")
        return

    for i in range(height):
        # Calcul des espaces pour centrer le triangle
        space = height - i - 1
        
        if i == 0:
            # Sommet du triangle : juste une barre / et \
            print(' ' * space+ "/" + "\\")
        elif i == height - 1:
            # Base du triangle : underscores entre les barres / et \
            print(' ' * space + "/" + '_' * (2 * i - 1) + "\\")
        else:
            # Lignes intermédiaires : espaces entre les barres / et \
            print(' ' * space + '/' + ' ' * (2 * i - 1) + '\\')

# Demander à l'utilisateur d'entrer la hauteur du triangle
height = int(input("Entrez la hauteur du triangle : "))
draw_triangle(height)


