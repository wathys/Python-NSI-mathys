#Ex 1
class Noeud:
    def __init__(self,valeur,gauche,droit):
        self.valeur = valeur #valeur noeud entier
        self.sag = gauche #sous arbre gauche de l'arbre
        self.sad = droit # sous arbre droit de l'arbre

class arbre:
    #arbre binaire de recherche initialement vide
    def __init__ (self):
        self.racine = None #arbre vide
        #si racine n'est pas vide alors c'st une instance de class noeud
    def est_vide(self):
        return self.racine == None
    def taille(self):
        if self.est_vide():
            return None
        else:
            return 1 + self.racine.sag.taille() + self.racine.sad.taille()
    def inserer(self,x):
        if self.est_vide():
            self.racine.valeur = x
        else:
            if self.racine.valeur < x:
                return inserer(self.racine.sad,x)
            else:
                return inserer(self.racine.sag,x)



#Parti A
#1) Valeur sag et sad
#2a) taille est le nombre de noeud qu'a un arbre
#3a
def somme(a):
    if a.est_vide():
        return 0
    else:
        g=a.racine.sag
        d=a.racine.sad
        return a.valeur + somme(g) + somme(d)
#b
def semi_mobile(a):
    if somme(a.racine.sag) == somme(a.racine.sad):
        return True
    return False

#4c
def mobile(a):
    if a.est_vide():
        return True
    else:
        if semi_mobile(a.racine.sag) != semi_mobile(a.racine.sad):
            return False
        else:
            return mobile(a.racine.sag) and mobile(a.racine.sad)

#parti b

def construire(mini,maxi):
    if maxi - mini <=1:
        return Noeud(mini,None,None)
    else:
        m = (mini+maxi)//2
        if maxi - mini == 2:
            return Noeud(m,None,None)
        else:
            gauche = construire(mini,m)
            droit = construire(m,maxi)
            return Noeud(m,gauche,droit)

#1a)
#2a)arbre binaire de recherche arbre ou tout valeur inferieur a la racine sera inserer a gauche et inversement

#3b)
def creation(l):
    a=arbre()
    for i in l:
        a.inserer(i)

#4b)
def pivot(a):
    part_gauche = a.racine.sag
    part_droit = a.racine


