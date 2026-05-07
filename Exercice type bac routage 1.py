#Exercice 1
#Partie B
def adjacent(r,g):
    l=[]
    for i in range(len(g[r])):
        if g[r][i] == 1:
            l.append(i)
    return l

def recherche(r1,r2):
    if r1 == r2:
        return True
    else:
        for s in adjacent(r,g):
            if recherche(s,r2):
                return True
            return False

