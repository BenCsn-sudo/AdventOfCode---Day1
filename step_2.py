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
    valeur = move[1:]        # On récupère tout le reste (les nombres)
    unit = len(valeur)-2
    if unit > 0:
        result += int(valeur[:-2])
        valeur = valeur[-2:]
    valeur = int(valeur)
    if direction == "R":
        # Vers la droite : on ajoute
        position = (position + valeur)
        if position > 99:
            result += 1
            position %= 100
    elif direction == "L":
        # Vers la gauche : on soustrait et on prend le modulo 100
        position = (position - valeur)
        if position < 0:
            result += 1
            position %= 100
        
    # On vérifie si on est tombé sur 0
    if position == 0:
        result += 1

print(f"Le mot de passe est : {result}")