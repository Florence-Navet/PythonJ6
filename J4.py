def draw_tapis(n):
    size = n + 1

    # Dessiner la première ligne
    print('+' + '-' * (size - 2) + '+')

    # Dessiner les lignes intermédiaires
    for i in range(1, size):
        if i <= size // 2:
            left_triangle = ' ' * (i - 1) + '#' * (size - i)
            right_triangle = '#' * (size - i) + ' ' * (i - 1)
        else:
            left_triangle = ' ' * (size - i - 1) + '#' * (i - size // 2)
            right_triangle = '#' * (i - size // 2) + ' ' * (size - i - 1)

        print('|' + left_triangle + right_triangle + '|')

    # Dessiner la dernière ligne
    print('+' + '-' * (size - 2) + '+')

# Demander à l'utilisateur d'entrer la taille du tapis
n = int(input("Entrez la taille du tapis (n) : "))
draw_tapis(n)


