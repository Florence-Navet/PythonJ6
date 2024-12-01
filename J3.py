L = int(input("Veuillez entrer le nombre de lignes:"))

def draw_tapis(n):
        size = n+1

        #dessiner la première ligne
        print('+' + '-' *(size-2)+ '+')

        for i in range(1, L + 1):

