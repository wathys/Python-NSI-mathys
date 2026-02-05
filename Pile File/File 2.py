# Créé par mren, le 18/12/2025 en Python 3.7
class elt:
    def __init__(self,x=None):
        self.valeur=x
        self.devant=None
        self.derriere=None

    def __str__(self):
        if self.devant==None:
            return str(self.valeur)
        else:
            return str(self.valeur)+ " --> "+ str(self.devant)

class file:
    def __init__(self):
        self.debut=None
        self.fin=None
    def __repr__(self):
        return str(self.fin)
    def est_vide(self):
        return self.debut==None
    def ajouter(self,x):
        c=elt(x)
        if self.est_vide():
            self.debut=c
        else:
            c.devant=self.fin
            self.fin.derriere=c
        self.fin=c
    def retirer(self):
        if not self.est_vide():
            c=self.debut
            if c.derriere==None:
                self.debut=None
                self.fin=None
            else:
                self.debut=c.derriere
                self.debut.devant=None
            return c.valeur



from random import randint,choice
def genere_ajouter(n):
    f=file()
    for _ in range(n):
        f.ajouter(randint(1,10))
    return f

#f=genere_ajouter(5)
#print("f = ",f)

def taille(f):
    n=0
    g=file()
    while not f.est_vide():
        g.ajouter(f.retirer())
        n+=1
    return n
#print(taille(f))
def recherche(f,x):
    f2=file()
    rep=False
    while not f.est_vide():
        q=f.retirer()
        f2.ajouter(q)
        if q == x:
            rep = True
    while not f2.est_vide():
        f.ajouter(f2.retirer())
    return rep
#print(recherche(f,2))

def moyenne(f):
    f2=file()
    t=0
    c=0
    while not f.est_vide():
        q = f.retirer()
        t += q
        c+=1
        f2.ajouter(q)
    while not f2.est_vide():
        f.ajouter(f2.retirer())
    return t//c
#print(moyenne(f))

def echange(f,i,j):
    m=0
    f2=file()
    if i>=j:
        raise ValueError("i>=j")
    while not f.est_vide():
        q=f.retirer()
        if m==i :
            i2 = q
        if m==j :
            f2.ajouter(i2)
            j2=q
        if m != i and m != j:
            f2.ajouter(q)
        m+=1
    k=0
    while not f2.est_vide():
        if k == i:
            f.ajouter(j2)
        else:
            f.ajouter(f2.retirer())
        k+=1
    return "f= ", f

#print(echange(f,0,3))


def polynome(f,x):
    r=0
    n=0
    f2=file()
    while not f.est_vide():
        q=f.retirer()
        r += q*x**n
        n+=1
    while not f2.est_vide():
        f.ajouter(f2.retirer())
    return r

#print(polynome(f,2))

class carte:
    def __init__(self):
        self.type = choice(["Feu","Eau","Terre"])
        self.valeur = choice([1,2,3,4,5,6,7,8,9])
    def getnom(self):
        return str(self.valeur) + " de " + str(self.type)

c = carte()
#print(c.getnom())

def existe(c,f):
    f2=file()
    while not f.est_vide():
        q=f.retirer()
        f2.ajouter(q)
        if c == q :
            while not f2.est_vide():
                f.ajouter(f2.retirer())
            return True
    while not f2.est_vide():
        f.ajouter(f2.retirer())
    return False

c2=carte()
c2.type="Eau"
c2.valeur=2
def paquet():
    fc=file()
    #fc.ajouter(c2)
    for i in range(10):
        fc.ajouter(carte())
    return fc


#f2=paquet()
#print(existe(c2,f2))

def gagne(c1,c2):
    if c1.type == c2.type:
        if c1.valeur == c2.valeur:
            return 0
        else :
            if c1.valeur > c2.valeur:
                return 1
            else :
                return 2
    if c1.type == "Feu" and c2.type == "Terre" or c1.type == "Terre" and c2.type == "Eau" or c1.type == "Eau" and c2.type == "Feu":
        if c1.valeur == c2.valeur:
            return 0
        if c1.valeur > c2.valeur*2:
            return 1
        else:
            return 2
    if c2.type == "Feu" and c1.type == "Terre" or c2.type == "Terre" and c1.type == "Eau" or c2.type == "Eau" and c1.type == "Feu":
        if c1.valeur == c2.valeur:
            return 0
        if c2.valeur > c1.valeur*2:
            return 2
        else:
            return 1
    if c1.valeur == c2.valeur:
        return 0

def bataille():
    paq1=paquet()
    paq2=paquet()
    g=None
    n=1
    while not paq1.est_vide() and not paq2.est_vide():
        print("Tour n°",n)
        c1 = paq1.retirer()
        print("c1 : ",c1.getnom())
        c2 = paq2.retirer()
        print("c2 : ",c2.getnom())
        g = gagne(c1,c2)
        print("Joueur",g," à gagner")
        print("\n")
        n+=1

    if paq1.est_vide() and paq2.est_vide():
        return print("Egalité")
    elif paq1.est_vide() :
        print("joueur 2 l'emporte")
    else :
        print("joueur 1 l'emporte")

bataille()










































