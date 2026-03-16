#Graphes
#1 notion d'un graphes
#   1.1 Définition

        #Graphes       un "graphes" est la donnée d'un certains nombre de point d'un plans il s'appelle sommet,
        #Arrête        dont certain sont relié par des trait (segment de droite), appeller les "arrête" du graphes. On associes généralement des noms au sommet d'un graphes afin de les distinguer.

        #Adjacent       Dans un graphes donné, on dit qu'un sommet B et "adjacent" a un sommet A si il exite une arrête  permettant d'aller du sommet A vers le sommet B

        #Ordre       On appelle ordre d'un graphe le nombre de sommet du graphes
        #Taille       On appelle taille d'un graphe le nombre d'arrête du graphes
        #Degrès     On appelle degrès d'un sommet, le nombre d'arrête incidente a ce sommet

        #Remarque : Une arrête peut relié un sommet a lui même, on parle alors de boucle. Dans ce cas, l'arrête compte double dans le calcul du degrès

#exemple
"""
A-------B
| \   / |
|   E   |
| /   \ |
C-------D

Ordre: 5
Taille: 8
Degrès:
    A : 3
    B : 3
    C : 3
    D : 3
    E : 4

"""
#remarque : un graphes est entièrement déterminer par l'ensemble de ses sommet et leurs relation d'adjacence. Ainsi un même graphe peut avoir plusieur représentation possible.

#   1.2 Chemins dans un graphe
#       définitions:
            #Chemin     Un chemin d'un sommet A vers un sommet B d'un graphe est un séquence fini de sommet adjacent de deux à deux menant du sommet A vers un sommet B, il y a donc une infinité de chemin permettant d'aller de A a B

            #Chemin Simple      Un chemin est dit simple si il n'empreinte j'amais deux fois par la même arrête.
            #Chemin Élémentaire     Un chemin est dit élémentaire si in ne passe jamais deux fois par le même sommet.
            #ATTENTION : Un chemin élémentaire est necessairement simple mais la réciproque n'est pas vrai.

            #Cycle      On appel cycle dans un graphe un chemin simple (non vide) permettant de relié un sommet à lui même

            #Longueur       La longueur d'un chemin est défini par le nombre d'arrête qui constitue ce chemin
            #Distance       La distance entre deux sommet est la longueur la plus courte reliant ces deux sommet

            #Remarque : Les arbres sont des exemple particuliers de graphe.Dans un arbre il exite toujours un unique chemin simple reliant deux sommet quelconque de l'arbre. En particuliers un arbre de contient pas de cycles.

#   1.3 Graphe orienté
#       Définition
        #Un graphe orienté est un graphe dans lequel chaque arrête est muni d'un sens. On parle alors de arc

        #Dégrés   (refaire la def)  On défini le degrès sortant, respectivement le degrès entrant, d'un sommet par le nombre de sommet par adjacent a ce sommet,respectivement le nombre de sommet dont notre sommet est adjacent





