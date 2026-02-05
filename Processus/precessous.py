#1) il peut se trouver prêt en execution et en attente

class Processus:
    def __init__(self,n,d,a):
        self.nom = n
        self.duree = d
        self.arrive = a
    #2
    def execute(self,p):
        p.duree -= 1
    def fini(self,p):
        return p.duree == 0
    def __repr__(self):
        return "(nom= " + self.nom +", durée= " + str(self.duree) + ", cycle de creation= " + str(self.arrive) + ")"

p = Processus("A",5,0)
#print(p)



#2a) soit en attente soit en execution

class File:
    def __init__(self):
        self.contenue = []
    def enfile(self,e):
        self.contenue.append(e)
    def defile(self):
        if not self.est_vide():
            return contenue.pop(0)
    def est_vide(self):
        return self.contenue == []
    def __repr__(self):
        f=File()
        s=""
        while not self.est_vide():
            q=self.defile()
            s += "\n" + q.__repr__()
        f.enfile(q)
        while not f.est_vide():
            self.enfile(f.defile())

f=(Processus("a",2,0),Processus("b",2,1),Processus("c",5,3))
print(f)


#a) First in first out

f=File()
#print(f.defile())

class ordonnanceur:
    def __init__(self):
        self.temps = 0
        self.file = File()
    def ajouter(self,p):
        self.file.enfile(p)
    def tourniquet(self):
        self.temps += 1
        if not self.file.est_vide():
            proc = self.file.defile()
            proc.execute()
            if not proc.fini():
                self.file.enfile(proc)
            return self.file

