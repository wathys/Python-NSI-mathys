#Exercice type bac révision

#Parti A
    #1 ls
    #2 il remonte 2 fois dans l'arboresence puis le déplace a cette emplacement : /home/document

class Arbre:
    def __init__(self,nom,g,d):
        self.nom = nom
        self.gauche = g
        self.droit = d
    def est_vide(self):
        return self.gauche is None and self.droit is None

    def parcours(self):
        print(self.nom)
        if self.gauche != None :
            self.gauche.parcours()
        if self.droit != None :
            self.droit.parcours()

    #3 L'arbre est en binaire et peut donc contenir 2 sous dossier maximum tant dis que sur la figure 1 on peut voire plusieur sous dossier

    #4 prefixe

    #5 

#Partie B

class Dossier:
    def __init__(self,nom,liste):
        self.nom = nom
        self.fils = liste #liste d'objets de la class Dossier

    def est_vide(self):
        return self.fils == []

    def parcours(self):
        print(self.nom)
        for f in self.fils:
            f.parcours()

    def mkdir(self,nom):
        self.fils.append(Dossier(nom,[]))

    def contient(self,nom_dossier):
        if self.nom == nom_dossier:
            return True
        else : 
            for f in self.fils:
                return f.contient(nom_dossier)
        return False


var_home = Dossier("home",["document","multimedia"])
var_multimedia = Dossier("multimedia",["images","vidéo"])
var_images = Dossier("images",[])
var_videos = Dossier("video",["film"])
var_films = Dossier("films",[])
#9 car la condition d'arret est le for f in self.fils donc si fils est vide alors elle s'arrête
#10 
def parcours(self):
        for f in self.fils:
            f.parcours()
            print(self.nom)

#11 Pacours affiche tout les sous dossier a partir d'un dossier alors que UNIX ls affiche tout les fichiers et dossiers à partir d'un dossier.
#15 rajouter une variable parent
#Exercice 2 Partie A
    #1 Non car plusieur chanson peuvent avoir le même titre
    #2Wecome too the jungle Appetite for Destruction
    #3 SELECT titre ASC FROM chanson ORDER BY titre WHERE album="Showbiz";
    #4 INSERT INTO chanson VALUE ("Megalomania"),("Hullabaloo");
    #5 UPDATE chanson SET album = "Welcome to the jungle" WHERE titre = "Wecome too the jungle";

#Partie B

    #6 afin d'éviter de tout reecrire la même chose, et est plus presentable
    #7  id_album sert a faire le lien avec l'album de la chanson
    #9 SELECT Album.titre FROM Album JOIN Chanson ON Chanson.id_album = Album.id WHERE Chanson.titre = "Showbiz";
    #10 SELECT Chanson.titre FROM Chanson JOIN Chanson ON Chanson.id_album = Album.id
    #11 affiche le nombre d'album qui on comme groupe Muse

#Parti C

def ordre_lex(mot1, mot2):
    if mot1 == "":
        return True
    elif mot2 == "":
        return False
    else:
        c1 = mot1[0]
        c2 = mot2[0]
        if c1 < c2:
            return True
        elif c1 > c2:
            return False
        else:
            return ordre_lex(mot1[1:],mot2[1:])

def ordre_lex(mot1,mot2):
    for i in range(len(mot1)):
        if mot1[i] == "":
            return True
        else:
            if mot2 == "":
                return False
            else :
                if mot1[i]<mot2[i]:
                    return True
                elif mot1[i]>mot2[i]:
                    return False

#exercice 3
#a 172.16
#b 172.16.0.255
#c 2**8

#Partie B

4#




