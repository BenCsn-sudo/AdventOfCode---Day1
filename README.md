# 🎄 Advent of Code - Day 1: Secret Entrance

![AoC Stars](https://img.shields.io/badge/Stars-2-yellow) ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

Ce dépôt contient ma solution pour le **Jour 1** de l'Advent of Code. Le défi consiste à manipuler un cadran de coffre-fort circulaire pour aider les Elfes à accéder à leurs décorations de Noël.

## 📖 Le Contexte

Nous sommes devant une entrée secrète au Pôle Nord. Le mot de passe a changé et se trouve dans un coffre-fort sécurisé par un cadran rotatif.

* **Le Cadran :** Un cercle numéroté de `0` à `99`.
* **Position de départ :** Le cadran pointe initialement sur `50`.
* **Mouvements :**
    * `L` (Left) : Tourne vers la gauche (vers les nombres décroissants).
    * `R` (Right) : Tourne vers la droite (vers les nombres croissants).
* **Circularité :** Le cadran boucle (après 99 on retourne à 0, et avant 0 on retourne à 99).

## 🧩 Partie 1 : Le Leurre

Le premier document de sécurité suggère que le mot de passe est le nombre de fois où le cadran **s'arrête** exactement sur `0` à la fin d'une rotation.

**Logique :**
1.  Lire la séquence d'instructions (ex: `L68`, `R48`).
2.  Mettre à jour la position courante en utilisant l'arithmétique modulaire (`% 100`).
3.  Incrémenter le compteur si la position **finale** après l'instruction est `0`.

**✅ Ma réponse :** `982`

## 🧩 Partie 2 : La vraie méthode (0x434C49434B)

Un second document révèle que le premier était un leurre. La vraie méthode de vérification compte le nombre de fois où le cadran **pointe sur 0 à n'importe quel moment**, c'est-à-dire :
* À la fin d'une rotation.
* PENDANT le mouvement de rotation (chaque "clic" passant par 0).

*Exemple : Si le cadran est à 50 et tourne de R1000, il passera par 0 dix fois.*

**Logique :**
Il faut calculer combien de fois l'intervalle parcouru traverse la frontière `99 -> 0` (pour R) ou `0 -> 99` (pour L) et ajouter cela au total.

**✅ Ma réponse :** `6106`

## 🛠️ Concepts Techniques

* **Parsing d'input :** Extraction des directions (`L`/`R`) et des distances.
* **Arithmétique Modulaire :** Gestion d'un tableau circulaire de taille 100.
    * Formule pour `R` (Droite) : `(position + distance) % 100`
    * Formule pour `L` (Gauche) : `(position - distance) % 100`

## ▶️ Comment lancer le code

Place ton fichier d'input (`input.txt`) dans le même dossier et lance le script :

```bash
# Remplacer par la commande correspondant à ton langage (ex: python main.py, node index.js, go run main.go)
python solution.py
