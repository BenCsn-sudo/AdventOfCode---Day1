# Lire le fichier texte de l'input
with open('input.txt', 'r', encoding='utf-8') as fichier:
    # .read().split() va séparer automatiquement par espaces ou retours à la ligne
    instructions = fichier.read().split()

# Initialisation selon l'énoncé
position = 50
result = 0

for move in instructions:
    direction = move[0]         # La lettre R ou L
    valeur = int(move[1:])      # La valeur qui suit la lettre

    if direction == "R":
        dist_vers_zero = 100 - position                 # Distance pour atteindre 0

        if valeur >= dist_vers_zero:                    # Dans le cas ou on dépasse 0
            result += 1
            reste_mouvement = valeur - dist_vers_zero   # Combien de tour encore on peut faire
            result += reste_mouvement // 100
        
        position = (position + valeur) % 100            # On met la position a jour

    elif direction == "L":
        dist_vers_zero = position                       # Comme on est dans le négatif la distance à zéro = la position
        if position == 0:                               
            dist_vers_zero = 100                        # Si la position est à 0 on est à 100 du prochain et non pas 0
            
        if valeur >= dist_vers_zero:
            result += 1
            reste_mouvement = valeur - dist_vers_zero
            result += reste_mouvement // 100
            
        position = (position - valeur) % 100

print(f"Le mot de passe est : {result}")