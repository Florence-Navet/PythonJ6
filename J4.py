def msg_chiffreCesar(message, decalage):
    # Variable contenant le message chiffré
    msgacripter = ""

    # Parcourir chaque caractère du message
    for char in message:
        # Vérifier si chaque lettre est une lettre de l'alphabet
        if char.isalpha():
            # Vérifier si c'est une lettre majuscule ou minuscule
            if char.isupper():
                start = 'A'
            else:
                start = 'a'
            # Appliquer le décalage César
            msgacripter += chr((ord(char) - ord(start) + decalage) % 26 + ord(start))
        else:
            # Si ce n'est pas une lettre, ajouter le caractère tel quel
            msgacripter += char
    
    # Retourner le message chiffré
    return msgacripter

# Demander à l'utilisateur de saisir un message à chiffrer
message = input("Entrez le message à chiffrer : ")

# Demander à l'utilisateur de saisir le décalage (positif ou négatif)
decalage = int(input("Entrez le décalage (positif ou négatif) : "))

# Afficher le message chiffré
print("Le message chiffré est :", msg_chiffreCesar(message, decalage))




