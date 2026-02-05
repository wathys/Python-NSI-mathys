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
evaluer(a)