def arrondir_notes(notes):
    # Liste vide pour stocker les notes arrondies
    notes_arrondies = []

    # Parcourir toutes les notes dans la liste donnée
    for note in notes:
        # Si la note est inférieure à 40, elle ne change pas
        if note < 40:
            notes_arrondies.append(note)
        else:
            # Calcul du prochain multiple de 5
            prochain_multiple_5 = ((note // 5) + 1) * 5
            
            # Si la différence entre la note et le prochain multiple de 5 est inférieure à 3
            if prochain_multiple_5 - note < 3:
                # Arrondir la note au prochain multiple de 5
                notes_arrondies.append(prochain_multiple_5)
            else:
                # Sinon, laisser la note telle quelle
                notes_arrondies.append(note)
    
    # Retourner la liste des notes arrondies
    return notes_arrondies
        
# Exemple d'utilisation
notes = [83, 82, 75, 38, 40, 98, 99]
notes_arrondies = arrondir_notes(notes)

print("Notes arrondies:", notes_arrondies)


        




