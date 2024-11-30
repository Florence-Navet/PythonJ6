def draw_rectangle(width, height):
   

    # Dessiner la première ligne
    print('|' + '-' * (width - 2) + '|')

    # Dessiner les lignes intermédiaires
    for i in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')

    # Dessiner la dernière ligne
    
        print('|' + '-' * (width - 2) + '|')

# Exemple d'utilisation
draw_rectangle(10, 3)
