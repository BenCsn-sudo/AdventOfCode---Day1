# Lire le fichier texte de l'input
with open('input.txt', 'r', encoding='utf-8') as fichier:
    # .read().split() va séparer automatiquement par espaces ou retours à la ligne
    instructions = fichier.read().split()

# Initialisation selon l'énoncé
position = 50
result = 0

for move in instructions:
    # On sépare la direction (1er caractère) de la valeur (le reste)
    direction = move[0]      # 'R' ou 'L'
    valeur = int(move[1:])   # Convertit tout le reste en entier
    
    if direction == "R":
        # Vers la droite : on ajoute
        position = position + valeur
        if position > 99:                       # Si on dépasse l'intervalle supérieur
            result += 1                         # Alors on est passé par 0
        position = position % 100               # Et on remet modulo 100 pour etre dans l'intervalle
    elif direction == "L":
        # Vers la gauche : on soustrait et on prend le modulo 100
        position = position - valeur
        if position < 0:                        # Si on dépasse l'intervalle inférieur
            result += 1
        position = position % 100
        
    # On vérifie si on est tombé sur 0
    if position == 0:
        result += 1

print(f"Le mot de passe est : {result}")