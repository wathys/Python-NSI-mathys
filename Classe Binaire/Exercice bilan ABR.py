#Ex 1


class arbre:
    #arbre binaire de recherche initialement vide
    def __init__ (self):
        self.racine = None #arbre vide
        #si racine n'est pas vide alors c'st une instance de class noeud
    def est_vide(self):
        return self.racine == None
    def taille(self):
        if self.est_vide():
            return 0
        else:
            return 1 + self.racine.sag.taille() + self.racine.sad.taille()
    def inserer(self,x):
        if self.est_vide():
            self.racine = Noeud(x,arbre(),arbre())
        else:
            if self.racine.valeur < x:
                self.racine.sad.inserer(x)
            else:
                self.racine.sag.inserer(x)

class Noeud:
    def __init__(self,valeur,gauche = arbre(),droit = arbre()):
        self.valeur = valeur #valeur noeud entier
        self.sag = gauche #sous arbre gauche de l'arbre
        self.sad = droit # sous arbre droit de l'arbre

a = arbre()
#print(a.est_vide())

a.racine = Noeud(10,arbre(),arbre())
#print(a.est_vide())
#print(a.racine.valeur)

a.racine.sag.racine = Noeud(8,arbre(),arbre())
#print(a.racine.sag.racine.valeur)

a.racine.sad.racine = Noeud(8,arbre(),arbre())

a.inserer(2)
#print("valeur inserer est = ",a.racine.sag.racine.sag.racine.valeur)

#print("Taille = " ,a.taille())

#Parti A
#1) Valeur sag et sad
#2a) taille est le nombre de noeud qu'a un arbre 9 et 6
#3a
def somme(a):
    if a.est_vide():
        return 0
    else:
        g=a.racine.sag
        d=a.racine.sad
        return a.racine.valeur + somme(g) + somme(d)

#print("somme = ",somme(a))


#b
def semi_mobile(a):
    if a.est_vide():
        return False
    if somme(a.racine.sag) == somme(a.racine.sad):
        return True
    return False

#print("l'arbre est semi-mobile = ",semi_mobile(a))

#4c
def mobile(a):
    if a.est_vide():
        return True
    else:
        if semi_mobile(a):
            return mobile(a.racine.sag) and mobile(a.racine.sad)
        else:
            return False

#print("l'arbre est mobile ", mobile(a))

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
    return a


b= creation([1,4,5,7,5])
"""
print(b.est_vide())
print(b.taille())
print(b.racine.valeur)
"""
#4b)
def pivot(a):
    part_droit = a.racine
print(5 <= 1)

