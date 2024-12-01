def pb_toilette(marches, hauteur_marches):
        #calcul de la hauteur d'un aller-retour
        hauteur_allers_retours = 2 * marches * hauteur_marches

        #nombre trajets par semaine(5 aller et retour )
        #10 trajet par jours sir 7 jours(donc sur une semaine)
        trajet_par_semaine = 10 * 7
        
        #distance en cm
        distance_cm = hauteur_allers_retours * trajet_par_semaine

        #distance en m
        distance_m = distance_cm / 100

        print(f"Pour {marches} marches de {hauteur_marches} cm, le gardien parcourt {distance_m} m par semaine.")

marches = int(input("Entrez un nombre de marches :"))
hauteur_marches = int(input("Entrez la hauteur de chaque marche en cm : "))

pb_toilette(marches, hauteur_marches)




