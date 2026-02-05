class objet :
    def __init__(self,x=None):
        self.valeur = x
        self.prochain = None
    def __str__(self):
        if self.prochain != None:
            return str(self.valeur) + "\n" + str(self.prochain)
        else :
            return str(self.valeur)

class pile():
    def __init__(self):
        self.haut = None
    def __str__(self):
        return str(self.haut)
    def est_vide(self):
        if self.haut == None :
            return True
        return False
    def empiler(self,x):
        c = objet(x)
        if not self.est_vide():
            c.prochain = self.haut
        self.haut = c
    def depiler(self):
        self.est_vide()
        a=self.haut
        self.haut = a.prochain
        return a.valeur

def nb_element(p):
    p2=pile()
    c=0
    while not p.est_vide():
        c+=0
        q = p.depiler
        p2.empiler(q)
    while not p2.est_vide():
        p.empiler(p2.depiler())
    return c

def partage(p,q1,q2):
    while not p.est_vide():
        if q1.est_vide():
            q1.empiler(p.depiler)
        else:
            q = p.depiler()
            if q > q1.haut():
                p1.empiler(q)
            else :
                p2.empiler(q)

def remplissage(p,q1,q2):
    for i in range(nb_element(q1)+nb_element(q2)):
        if q1.haut > q2.haut or q2.est_vide():
            p.empiler(q1.depiler())
        elif q2.haut > q1.haut or q1.est_vide():
            p.empiler(q2.depiler())

def tri(p,q1,q2):
    for i in range(nb_element(p)):
        partage(p,q1,q2)
        remplissage(p,q1,q2)

def pol_inv(c):
    p=pile()
    for i in range(len(c)):
        if c[i] == "*" :
            n=int(c[i+1])
            p.empiler(p.haut.valeur * n)
        if [i] == "/":
            n=int(c[i+1])
            p.empiler(p.haut.valeur / n)
        if [i]== "-":
            n=int(c[i+1])
            p.empiler(p.haut.valeur + n)
        if [i] == "+":
            n=int(c[i+1])
            p.empiler(p.haut.valeur * n)
        else :
            p.empiler(c[i])
    return p.haut
c = "5/9*9+6-6"
#print(pol_inv(c))


def maxpile(p, i):
    p2 = pile()
    q = p.depiler()
    p2.empiler(q)
    i = 1
    for i in range(2,i+1):
        x = p.depiler()
        if x > m:
            m = x
            indice = k
        p2.empiler(x)
    while not p2.est_vide():
        p.empiler(p2.depiler())
    return x

def retouner(p,i) :
    """prend une pile p et un entier i et renvoie la position de j"""
    p2=pile()
    p3=pile()
    for _ in range(i):
        p2.empiler(p.depiler())
    while not p2.est_vide():
        p3.empiler(p2.depiler)
    while not p3.est_vide():
        p.empiler(p.depiler())

def trir(p):
    p2=pile()
    i = nb_element(p)-1
    for _ in range(nb_element(p)-1):
        indice_max = maxpile(p,t-k)
        retouner(p,indice_max)
        retouner(p,t-k)
"""
class pile1:
    def __init__(self):
        self.pile = []
    def __repr__(self):
        return str(self.pile)
    def est_vide(self):
        return self.pile == []
    def empiler(self,x):
        self.pile.append(x)
    def depiler(self):
        self.pile != []
        x = self.pile.pop(-1)
        return x
"""
global p1
global p2
p1 = pile()
p2 = pile()

def cree_pile(c1,c2):
    p3=pile()
    p4=pile()
    for i in c1:
        p1.empiler(i)
    for i in c2 :
        p3.empiler(i)
    while not p3.est_vide():
        p2.empiler(p3.depiler)

def supprimer():
    if not p1.est_vide():
        p1.depiler()

def inserer(c):
    for i in c:
        p1.empiler(i)

def avancer(n):
    for i in range(n):
        if not p2.est_vide():
            p1.empiler(p2.depiler())

def reculer(n):
    if n == 0 and not p1.est_vide():
        return None
    else:
        p2.empiler(p1.depiler())
        reculer(n-1)


def position():
    c=0
    while not p2.est_vide():
        p2.empiler(p1.depiler())
        c+=1
    for i in range(c):
        p1.empiler(p2.depiler)
    return c

def lecture():
    mot=""
    while not p1.est_vide():
        p2.empiler(p1.depiler())
        c-=1
    while not p2.est_vide():
        q = p2.depiler()
        print(v,end="")
        p1.empiler(q)
        n+=1
    reculer(n)
"""
cree_pile("Bon","jours")
print("\n",p2)
print("\n")
avancer(1)
print("\n")
print(p1,"\n","\n",p2)

#print(inserer("ab"))
##print(supprimer())
##print(avancer(5))
##print(reculer(2))
print(position())
print(lecture())
"""


