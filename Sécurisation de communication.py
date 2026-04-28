def indice(x,c):
    for i in range(len(c)):
        if c[i] == x:
            return i
    return -1

cle = 1
message = "dhflgqjùfohdsvnq"

def chiffrement(m,k):
    lettre = "abcdefghijklmnopqrstuvwxyz"
    s=""
    for i in m:
        j = indice(i,lettre)
        if j == -1:
            s=s+i
        else:
            a = (j + k) % len(lettre)
            s = s + lettre[a]
    return s
#print(chiffrement(message,cle))

def dechiffrement(m,k):
    lettre = "abcdefghijklmnopqrstuvwxyz"
    s=""
    for i in m:
        j = indice(i,lettre)
        if j == -1:
            s=s+i
        else:
            a = (j - k) % len(lettre)
            s = s + lettre[a]
    return s
#print(dechiffrement(chiffrement("informatique",cle),cle))

"""
def chiffrement(m,k):
    lettre = "abcdefghijklmnopqrstuvwxyz"
    s=""
    for i in m:
        if indice(i,lettre) + k > len(lettre):
            s = s + lettre[(indice(i,lettre)+k)- k % len(lettre)]
        else:
            s = s + lettre[indice(i,lettre)+k]
    return s


def dechiffrement(m,k):
    lettre = "abcdefghijklmnopqrstuvwxyz"
    s=""
    for i in m:
        if indice(i,lettre) - k < 0:
            s = s + lettre[(indice(i,lettre)-k)+ k % len(lettre)]
        else:
            s = s + lettre[indice(i,lettre)-k]
    return s
#print(dechiffrement("nsktwrfynvzj",5))

"""

def binaire(n):
    b=""
    for i in range(8):
        r=n%2
        n=n//2
        b=str(r)+b
    return b

def xor(b1,b2):
    r=""
    for i in range(8):
        if b1[i] == b2[i]:
            r = r + str(0)
        else:
            r = r + str(1)
    return r
#print(xor("01001001","01010011"))

def decimal(n):
    r=0
    m = len(n)-1
    for i in range(len(n)):
        if n[i] == "1":
            r = r + 2**(m-i)
    return r

#print(decimal("00000001"))

def chiffrementxor(m,k):
    s=""
    for i in range(len(m)):
        a1= m[i]
        a2= k[i%len(k)]
        b1 = binaire(ord(a1))
        b2 = binaire(ord(a2))
        b = xor(b1,b2)
        d = decimal(b)
        s = s + chr(d)
    return s
print(chiffrementxor("informatique","super"))

