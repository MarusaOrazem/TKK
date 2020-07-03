abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
       'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ind = {abc[i]:i for (i,abc[i]) in enumerate(abc)}
pogoste = ['THE', 'IS', 'SOME', 'FOR', 'IN', 'AT', 'TAKE','VERY', 'POOR', 'THING', 'ONE', 'TRUE', 'OF','AND',
           'NOT', 'WITH', 'HE', 'BUT', 'THIS', 'HIS', 'ME'] #vec besed -> bolj gotova pravilnost rezultata

'{0:05b}'.format(7)  #to je binarno za 7 dolzine 5


#iscemo zacetno stanje za vsak lfsr, torej niz dolzine, ki jo doloca karakteristicni polinom

p1 = [1,0,0,1,0]
p2 = [1,0,0,0,0,0,1]
p3 = [1,0,0,0,0,0,0,0,0,1,0]
pp = [1,1,0,0]

def encrpyt(b):
    rez = prevedi_besedilo(b)
    l = len(rez)
    kljuc = lfsr(rez,l,p1)
    out = sestej(kljuc,rez)
    return out

def lfsr(zac,d,pol):
    #zac je zacetni kljuc,podan v bitnem zapisu, d je dolzina niza, pol so koef. kar. polinoma vrne celotno zaporedje
    rez = zac
    k = len(pol)
    for i in range(k,d):
        s=0
        for j in range(1,k+1):
            aa = pol[k-j]
            bb = int(rez[i-j])
            a= aa*bb
            s+=a
        s = s%2
        rez += str(s)
    return rez

def geffe(zac1,zac2,zac3,d): #a jih res rabmo tok zacetnih, no, i guess da ja, ce pa jih je naloga poiskat
    #vrne kljuc, sestavljen iz treh LFSRjev
    #predpostavim, da je mnozenje kar bit and
    x1 = lfsr(bin(zac1)[2:].zfill(len(p1)),d,p1)
    x2 = lfsr(bin(zac2)[2:].zfill(len(p2)),d,p2)
    x3 = lfsr(bin(zac3)[2:].zfill(len(p3)),d,p3)
    z=''
    for i in range(d):
        z+=str((int(x1[i])*int(x2[i])+int(x2[i])*int(x3[i])+int(x3[i]))%2)
    return z

def prevedi_besedilo(b):
        #vrne besedilo, zapisano v bitih, dolzina vsakega znaka je 5
        rez=''
        for znak in b:
            rez += bin(ind[znak])[2:].zfill(5)
        return rez

def prevedi_bite(c):
    #vrne iz bitov prevedeno besedilo
    rez=''
    d=len(c)
    for i in range(d//5):
        rez+=abc[int(c[i*5:5*i+5],2)]
    return rez
    
def sestej(a,b):
    #predpostavimo, da sestevamo enako dolga stevila
    d=len(a)
    #bitwise and
    #a in b sta dvojiska niza
    return bin(int(a,2)^int(b,2))[2:].zfill(len(a))
    




#ZDAJ PRIDE NA VRSTO FUNKCIJA, KI S POMOCJO KORELACIJE DOLOCI ZACETNO STANJE
#pomagaj si z nalogo iz vaj, uporabi znano dejstvo, v kaj se sifrira beseda
beseda = 'CRYPTOGRAPHY' #ta verzija je z odbitkom
p = prevedi_besedilo(beseda) #za lazjo uporabo v razbijanju
#vemo, da se beseda CRIPTOGRAPHY sifrira v niz
ch = '011001110111111110011000111110101010111001111011000111111001'
#vemo, da se p prevede v ch

def razbij_geffe(b):
    z = sestej(p,ch) #z je gotovo output geffeja
    d = len(ch) #a bi mogoce mogu gledat celo besedilo? hm
    k1 = len(p1)
    k2 = len(p2)
    k3 = len(p3)
    for j in range(2**k1):
        kljuc1 =  bin(j)[2:].zfill(k1)
        x1 = lfsr(kljuc1,d,p1)
        s=0
        for i in range(d):
            if z[i]==x1[i]:
                s+=1
        if s/d > 0.75:
            print(s/d)
            key1=(j,x1)
            break
    for j in range(2**k3):
        kljuc3 = bin(j)[2:].zfill(k3)
        x3 = lfsr(kljuc3,d,p3)
        s=0
        for i in range(d):
            if z[i]==x3[i]:
                s+=1       
        if s/d > 0.75:
            print(s/d)
            key3=(j,x3)
            break
    for j in range(2**k2):
        kljuc2 = bin(j)[2:].zfill(k2)
        x2 = lfsr(kljuc2,d,p2)
        g=''
        for i in range(d):
            g += str((int(key1[1][i])*int(x2[i]) + int(x2[i])*int(key3[1][i]) + int(key3[1][i]))%2)

        flag = True
        for i in range(d):
            if g[i] != z[i]:
                flag = False
                break
        if flag==True:
            print(key1,key3)
            return (key1,(j,x2),key3)


    










sifra = encrpyt(beseda)

t = open('geffe.txt','r')
test = t.read()
d=len(test)
kljuci = razbij_geffe(test)
a,b,c=kljuci
#lfsr('1000',18,pp)
g=geffe(a[0],b[0],c[0],d)
print(g)
rezultat=sestej(test,g)
konec = prevedi_bite(rezultat)
print(konec)
                
