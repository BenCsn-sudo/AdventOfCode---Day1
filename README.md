# AdventOfCode---Day1

# 🔐 North Pole Safe Cracker

**Résolution d'un puzzle logique : simulation d'un cadran de coffre-fort (0-99). Le script parse une liste de rotations (G/D) et utilise l'arithmétique modulaire pour compter combien de fois le curseur s'arrête sur 0, révélant ainsi le mot de passe caché.**

## 🎄 Contexte
Les Elfes ont perdu le mot de passe du coffre-fort du Pôle Nord. Pour l'ouvrir, il faut suivre une liste d'instructions de rotation sur un cadran circulaire numéroté de 0 à 99. Le "vrai" mot de passe n'est pas la position finale, mais le nombre de fois où le cadran s'arrête exactement sur la position **0**.

## ⚙️ Fonctionnement Technique
Le script Python simule le mouvement du cadran en appliquant des opérations mathématiques sur la position courante :

1.  **Parsing** : Lecture du fichier `input.txt` et découpage des instructions (ex: `R15`, `L99`).
2.  **Arithmétique Modulaire** : Utilisation de l'opérateur modulo (`% 100`) pour gérer la circularité du cadran (0-99).
    * Rotation Droite (R) : `(pos + n) % 100`
    * Rotation Gauche (L) : `(pos - n) % 100`
3.  **Logique** : 
    * Position initiale : **50**
    * Incrémentation du compteur de résultat à chaque passage à 0.

## 🚀 Utilisation

1. Assurez-vous d'avoir le fichier de données `input.txt` dans le même dossier.
2. Lancez le script :

```bash
python main.py
