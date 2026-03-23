#Graphes
#1 notion d'un graphes
#   1.1 Définition

        #Graphes       un "graphes" est la donnée d'un certains nombre de point d'un plans il s'appelle sommet,
        #Arrête        dont certain sont relié par des trait (segment de droite), appeller les "arrête" du graphes. On associes généralement des noms au sommet d'un graphes afin de les distinguer.

        #Adjacent       Dans un graphes donné, on dit qu'un sommet B et "adjacent" a un sommet A si il exite une arrête  permettant d'aller du sommet A vers le sommet B

        #Ordre       On appelle ordre d'un graphe le nombre de sommet du graphes
        #Taille       On appelle taille d'un graphe le nombre d'arrête du graphes
        #Degrès     On appelle degrès d'un sommet, le nombre d'arrête incidente a ce sommet
        #Remarque:        La somme des degrès represente le double de la taille

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

#2 Matrice d'adjacence d'un graph
#   2.1 Introduction
        #On considère un graphe (orienté ou non) et on va noter ses sommets par des entier de 0 et 1, ou n'est pas l'ordre du graphe. On peut alors representr le graphe par une matrice de taille n*n, c'est à dire un tableau à n lignes et n colone, où l'élement à la i éme ligne et j ème colone sont 1 s'il existe une arrête reliant le sommet i vers le sommet j, et 0 sinon. On appelle cette matrice la "matrice d'ajacence"
        #exemple :

"""
   1
 /   \
0     2
|\   /|
|  3  |
4-----5


  0 1 2 3 4 5
0 0 1 0 1 1 0
1 1 0 1 0 0 0
2 0 1 0 1 0 1
3 1 0 1 0 0 0
4 1 0 0 0 0 1
5 0 0 1 0 1 0
"""

"""
0--->1--->3
> \  |    |
|  > >    |
|    2    <
4<--------5

0 1 1 0 0 0
0 0 1 1 0 0
0 0 0 0 0 0
0 0 0 0 0 1
1 0 0 0 0 0
0 0 0 0 1 0
"""
        #Remarque la contruction de la matruce d'ajacence dépend du choix de la numérotation des sommet donc un graphe possède plusieur matrice d'ajacences, mais ces matrices sont toutes équivalente
#   2.2 Representaion des matrice en python
        #Pour representer une matruce en python on va utiliser une liste de liste, où chaque liste va representer une ligne de la matrice.

        #Par exemple:
"""
1 2 4
5 0 7
6 2 3
"""
g = [
    [1,2,4],
    [5,0,7],
    [6,2,3]
        ]

        #quelque commande a retenir:
            #M[i] renvoie la i ème ligne de la matrice M
            #M[i][j] renvoie la i ème ligne et la j ème colone de la matrice M

#   2.3 Ordre d'un graphe
    #L'ordre d'un graphe correspond au nombre de ligne dans la matrice d'adjacent, c'est à dire au nombre d'élément dans la liste M. On peut facilement récuperer l'ordre du graphe à l'aide de l'instruction : "len(M)"

#   2.4 Taille d'un graphe
#       2.4.1 Graphe orienté
            #La taille d'un graphe orienté est égale à la somme des élément dans la matrice d'adjacence

def taille_oriente(M):
    t = 0
    m = len(M)
    for i in range(m):
        for j in range(m):
            t = t + m[i][j]
    return t

#   2.4.1 Graphe non orienté
        #Dans le cas d'un graphe orienté, toutes les arrêtes son compter deux fois dans la matrice d'adjacences (sauf boucle). Afin de répondre à ce probleme on peut uniquement compter les élément qui sont en dessous de la diagonale.

def taille_non_oriente(M):
    t = 0
    m = len(M)
    for i in range(m):
        for j in range(i+1):
            t = t + m[i][j]
    return t

#   2.5 Degré d'un sommet
#       2.5.1 Graphe non orienté
def degree_non_oriente(m,a):
    n=0
    for i in range(len(m[a])):
        n= n + m[a][i]
##        if m[a][a] == 1:
##            n+=1
    return n + m[a][a]

#       2.5.2 Graphe oriente
def degree_oriente(m,a):
    e=0
    s=0
    for i in range(len(m[a])):
        s = s + m[a][i]
        e = e + m[i][a]
    return e + s

m = [[0,1,0,0,1,0],[1,0,1,0,0,1],[0,1,0,1,0,1],[0,0,1,1,1,1],[0,0,0,1,0,1],[0,1,1,0,1,0]]
print(degree_oriente(m,2))

#3 Dictionnaire d'adjacence d'un graphe
#   3.1 Introduction
        #une autre manière de coder un graphe est d'utiliser un dictionnaire, dans le quel chaque sommet sera une clé du dictionnaire et la valeurs associé a cette clé sera une liste represantant l'enssemble des sommet adjacent a cette clé.

d = {"a" : ["b","c","d","f"],"b" : ["a","d"], "c" : ["a","d","e","f"], "e" : ["d","c","f"], "f" : ["a","c","e"]}

d = {0 : [1,2], 1 : [3], 2 : [3,1], 3 : [5], 4 : [0],5 : [2,4]}





