class arbre:
    def __init__(self,v):
        self.noeud = v
        self.gauche = None
        self.droit = None
    def ins_gauche(self,v):
        if self.gauche == None:
            self.gauche = arbre(v)
    def ins_droit(self,v):
        if self.droit == None:
            self.droit = arbre(v)
    def hauteur(self):
        if self.est_vide():
            return -1
        else:
            return 1+max(self.sag().hauteur(), self.sad().hauteur())
    def est_partiellement_equilibre(self):
        if self.est_vide():
            return True
        return abs( self.sag().hauteur() - self.sad().hauteur()) <= 1
class ABR:
    # arbre binaire de recherche initialement vide
    def __init__(self):
        self.racine = None # arbre vide
        # Remarque : si l’arbre n’est pas vide, racine est
        # une instance de la classe Noeud
    def est_vide(self):
        return self.racine == None
    def insere(self, nouveau_noeud):
        if self.est_vide():
            self.racine = nouveau_noeud
        elif self.racine.indice < nouveau_noeud.indice:
            self.racine.gauche.insere(nouveau_noeud)
        else:
            self.racine.droite.insere(nouveau_noeud)
    def est_present(self, indice_recherche):
        """renvoie True si l’indice de priorité indice_recherche (int) passé en paramètre
        est déjà l’indice d’un nœud de l’arbre, False sinon"""
        if self.est_vide():
            return False
        else:
            if self.racine.indice == indice_recherche :
                return True
            else:
                if self.racine.indice < indice_recherche:
                    return self.racine.droit.est_present(indice_recherche)
                else:
                    return self.racine.gauche.est_present(indice_recherche)
    def tache_prioritaire(self):
        """renvoie la tache du noeud situé le plus
à gauche de l’ABR supposé non vide"""
        if self.racine.gauche.est_vide():
            return self.racine
        else:
            return self.racine.gauche.tache_prioritaire()

class Noeud:
    def __init__(self, tache, indice):
        self.tache = tache # ce que doit accomplir le robot
        self.indice = indice # indice de priorité (int)
        self.gauche = ABR() # sous-arbre gauche vide (ABR)
        self.droite = ABR() # sous-arbre droit vide (ABR)

def taille(a):
    if a == None :
        return 0
    else:
        return 1 + taille(a.gauche) + taille(a.droit)

def hauteur(a):
    if a == None:
        return 0
    else :
        return 1 + max(hauteur(a.gauche), hauteur(a.droit))

def recherche(a,x):
    if a == None :
        return False
    else:
        if a.noeud == x :
            return True
        else:
            return recherche(a.gauche,x) or recherche(a.droit,x)

def minimum(a):
    n=a.noeud
    if a.gauche == None and a.droit ==None:
        return a.noeud
    else:
        if a.noeud < n :
            n = a.noeud
        else:
            if a.gauche == None:
                return min(a.noeud,minimum(a.droit))
            if a.droit == None:
                return min(a.noeud,minimum(a.gauche))
            else:
                return min(a.noeud,minimum(a.gauche),minimum(a.droit))

def maximum(a):
    n=a.noeud
    if a.gauche == None and a.droit ==None:
        return a.noeud
    else:
        if a.noeud > n :
            n = a.noeud
        else:
            if a.gauche == None:
                return min(a.noeud,minimum(a.droit))
            if a.droit == None:
                return min(a.noeud,minimum(a.gauche))
            else:
                return min(a.noeud,minimum(a.gauche),minimum(a.droit))


def profondeur(a,s):
    if a.noeud == s:
        return 1
    if recherche(a.gauche,s):
        return 1 + profondeur(a.gauche,s)
    if recherche(a.droit,s):
        return 1 + profondeur(a.droit,s)

def compte(a,x,y):
    if type(x) != int or type(y)!=int:
        raise TypeError
    if x>y:
        raise ValueError
    else:
        if a == None:
            return 0
        else:
            if x <= a.noeud <= y:
                return 1 + compte(a.gauche,x,y) + compte(a.droit,x,y)
            else:
                return compte(a.gauche,x,y) + compte(a.droit,x,y)

def strict(a):
    if a.gauche != None and a.droit == None or a.gauche == None and a.droit != None:
        return False
    elif a.gauche == None and a.droit == None:
        return True
    else:
        return strict(a.gauche) and strict(a.droit)

def additif(a):
    if strict(a) == False:
        return False
    if a.gauche == None and a.droit == None:
        return True
    else:
        if (a.gauche.noeud + a.droit.noeud) == a.noeud:
            return additif(a.gauche) and additif(a.droit)
        else:
            return False

def additif2(a,s=False):
    if s == False:
        if strict(a) == False:
            return False
        else:
            s = True
    if a.gauche == None and a.droit == None:
        return True
    else:
        if (a.gauche.noeud + a.droit.noeud) == a.noeud:
            return additif(a.gauche) and additif(a.droit)
        else:
            return False

def binaireit(n):
    c=""
    while n != 0:
        if n % 2 == 0:
            c = "0" + c
        elif n % 2 == 1:
            c = "1" + c
        n=n//2
    return c

def binairerec(n):
    if n == 0 :
        return ""
    else:
        if n % 2 == 0:
            return binairerec(n//2) + "0"
        else:
            return binairerec(n//2) + "1"

def binaire(n):
    return str(bin(n))

def ajnoeud(a,c,comp=1, arb = False):

    if a==None and c != "":
        a=arbre(1)

    if a == None :
        return None

    if c == "":
        return a

    if arb == False:
        arb = True
        c2 = c
        return ajnoeud(a,c,comp,arb)

    if arb == True:

        if c[comp] == "0":
            a.ins_gauche(c[0:comp+1])
            return ajnoeud(a.gauche,c,comp+1,arb)
        else:
            a.ins_droit(c[0:comp+1])
            return ajnoeud(a.droit,c,comp+1,arb)

#exemple 1
"""
a = arbre(10)
a.ins_gauche(5)
a.ins_droit(5)
a.gauche.ins_gauche(3)
a.gauche.ins_droit(2)
a.droit.ins_droit(3)
a.droit.ins_gauche(2)
"""
#exemple arbre 1
"""
a=arbre("a")
a.ins_gauche("b")
a.ins_droit("c")
a.gauche.ins_gauche("d")
a.gauche.ins_droit("e")
a.gauche.droit.ins_gauche("f")
a.gauche.droit.ins_droit("g")
"""
#exemple arbre 2*
"""
a = arbre("a")
a.ins_gauche("b")
a.gauche.ins_gauche("c")
a.gauche.gauche.ins_gauche("e")
a.gauche.gauche.ins_droit("f")
a.ins_droit("f")
a.droit.ins_gauche("g")
a.droit.ins_droit("i")
a.droit.gauche.ins_droit("h")
"""

#arbre Binaire numéroté 1 exemple ex6
"""
a=arbre(1)
a.ins_gauche(10)
a.ins_droit(11)
a.gauche.ins_droit(101)
a.gauche.droit.ins_gauche(1010)
a.gauche.droit.ins_droit(1011)
"""
#arbre Binaire numéroté 2 exemple 2a
"""
a=arbre(1)
a.ins_droit(11)
a.gauche.ins_gauche(10)
a.gauche.ins_droit(101)
a.gauche.droit.ins_gauche(1010)
a.gauche.droit.ins_droit(1011)
a.gauche.droit.droit.ins_gauche(10110)
a.gauche.droit.droit.gauche.ins_droit(101101)
"""

#arbre Binaire numéroté 2 exemple 2b
"""
a=arbre("1")
a.ins_gauche("10")
a.ins_droit("11")
a.droit.ins_droit("111")
a.droit.droit.ins_droit("1111")
a.gauche.ins_gauche("100")
a.gauche.gauche.ins_gauche("1000")
a.gauche.gauche.gauche.ins_droit("10001")
"""

"""
print(taille(a))
print(hauteur(a))
print(recherche(a,"z"))
print(minimum(a))
print(strict(a))
print(additif(a))
print(additif2(a))
print(binaireit(50))
print(binairerec(50))
print(ajnoeud(a,"11111"))
"""

#Feuille 2

#ex 2, 2 b

def evaluer(a):
    if a.gauche == None and a.droit == None :
        return a.noeud
    if a.noeud == "+" :
        return evaluer(a.gauche) + evaluer(a.droit)
    if a.noeud == "-" :
        return evaluer(a.gauche) - evaluer(a.droit)
    if a.noeud == "*" :
        return evaluer(a.gauche) * evaluer(a.droit)
    if a.noeud == "/" :
        return evaluer(a.gauche) / evaluer(a.droit)


#ex 2 ,1 a
"""
a = arbre("*")
a.ins_gauche("+")
a.gauche.ins_gauche(2)
a.gauche.ins_droit(5)
a.ins_droit("-")
a.droit.ins_gauche(3)
a.droit.ins_gauche(4)
"""
#ex 1 b
"""
a=arbre("*")
a.ins_gauche("+")
a.gauche.ins_gauche(3)
a.gauche.ins_droit(1)
a.ins_droit("/")
a.droit.ins_gauche("+")
a.droit.gauche.ins_gauche(4)
a.droit.gauche.ins_droit(2)
a.droit.ins.droit(3)
"""

#ex 1 c
"""
a=arbre("/")
a.ins_gauche("*")
a.gauche.ins_gauche("+")
a.gauche.gauche.ins_gauche(1)
a.gauche.gauche.ins_droit(2)
a.gauche.ins_droit(4)
a.ins_droit("-")
a.droit.ins.gauche("*")
a.droit.gauche.ins_gauche(2)
a.droit.gauche.ins_droit(3)
a.droit.ins_droit(5)

"""
"""evaluer(a)"""

#ABR FEUILLE 1

def est_abr(a):
    if a == None:
        return True
    if a.gauche != None and a.noeud < maximum(a.gauche):
        return False
    if a.droit != None and a.noeud > maximum(a.droit):
        return False
    return est_abr(a.gauche) and est_abr(a.droit)

def verifieABR(a):
    return est_abr(a) == True

def minABR(a):
    if a == None :
        return None
    if a.gauche == None and a.droit == None:
        return a.noeud
    else:
        minABR(a.gauche)

def minABR(a):
    if a == None :
        return None
    if a.gauche == None and a.droit == None:
        return a.noeud
    else:
        minABR(a.droit)
#ABR
"""
a=arbre(6)
a.ins_droit(7)
a.ins_gauche(1)
a.gauche.ins_droit(5)
a.droit.ins_droit(9)
a.gauche.droit.ins_gauche(4)
a.gauche.droit.gauche.ins_gauche(3)
a.gauche.droit.gauche.ins_gauche(2)
a.droit.droit.ins_gauche(8)

"""
a=arbre(15)
a.ins_gauche(4)
a.gauche.ins_droit(6)
a.gauche.droit.ins_droit(12)
a.ins_droit(18)
a.droit.ins_droit(23)
a.gauche.droit.droit.ins_droit(14)
a.gauche.ins_gauche(2)
a.droit.droit.ins_gauche(20)
a.gauche.droit.droit.ins_gauche(11)
a.droit.ins_gauche(16)
a.gauche.droit.droit.gauche.ins_gauche(7)

#print(est_abr(a))

def ajt_abr(x,a=None):
    if a == None:
        a=arbre(x)
        return a
    else:
        if a.noeud > x:
            if a.gauche == None:
                a.ins_gauche(x)
                return a
            else:
                return ajt_abr(x,a.gauche)
        else:
            if a.droit == None:
                a.ins_droit(x)
                return a

def contruction(a,l):
    a=arbre()
    for i in l:
        a = ajt_abr(i,a)
    return arbre

def tri_arbre(a):
    if a == None:
        return []
    else:
        if a.gauche == None and a.droit == None:
            return [a.noeud]
        else:
            return tri_arbre(a.gauche) + [a.noeud] + tri_arbre(a.droit)

#print(tri_arbre(a))

#Feuille 2 type bac
a1 = arbre(1)
a1.ins_gauche(0)
a1.ins_droit(2)
a1.droit.ins_droit(3)
a1.droit.droit.ins_droit(4)
a1.droit.droit.droit.ins_droit(5)
a1.droit.droit.droit.droit(6)

a2 = arbre(3)
a2.ins_gauche(2)
a2.gauche.ins_gauche(1)
a2.gauche.gauche.ins_gauche(0)
a2.ins_droit(4)

arbre_no1 = arbre()
arbre_no2 = arbre()
arbre_no3 = arbre()
for cle_a_inserer in [1,0,2,3,4,5,6]:
    arbre_no1.inserer(cle_a_inserer)
for cle_a_inserer in [0,1,2,6,5,4,3]:
    arbre_no2.inserer(cle_a_inserer)
for cle_a_inserer in [0,1,2,3,4,5,6]:
    arbre_no3.inserer(cle_a_inserer)
"""
def hauteur(self):
    if self.est_vide():
        return -1
    else:
        return 1+max(self.sag().hauteur(), self.sad().hauteur())
"""
"""
def est_present(self,cle_a_rechercher):
    if self.est_vide():
        return False
    elif cle_a_rechercher == self.cle():
        return True
    elif cle_a_rechercher < self.cle():
        return self.sad.est_present(cle_a_rechercher)
    else:
        return self.sag.est_present(cle_a_rechercher)
"""
"""
def est_partiellement_equilibre(self):
    if self.est_vide():
        return True
    return abs( self.sag().hauteur() - self.sad().hauteur()) <= 1
"""
#Feuille 3
#ex 1.1 File
#ex 1.2a Taille b racine c feuille

#ex 1.3 a tache indice droite gauche

# b elle se termine car sur l'abre est vide elle se termine automatiquement et elle s'apelle elle meme

# C <

#5a 3 5 6 7 8 10 11 13 16 14

#B lors de la recherche on prend la premiere valeur

"""
a) reçu une tâche d’indice de priorité 14 à accomplir
b) reçu une tâche d’indice de priorité 11 à accomplir
c) reçu une tâche d’indice de priorité 8 à accomplir
d) accompli sa tâche prioritaire
e) reçu une tâche d’indice de priorité 12 à accomplir
f) accompli sa tâche prioritaire
g) accompli sa tâche prioritaire
h) reçu une tâche d’indice de priorité 15 à accomplir
i) reçu une tâche d’indice de priorité 19 à accomplir
j) accompli sa tâche prioritaire
"""




