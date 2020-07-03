#prva domača naloga za TKK 2018/2019
#Maruša Oražem, 27151090, 2.letnik matematika

#1. naloga - Vigenerjeva šifra

#1.1

abeceda = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
pogostost = {'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253, 'E': 12.702, 'F': 2.228, 'G': 2.015, 'H': 6.094, 'I': 6.966, 'J': 0.153, 'K': 0.722, 'L': 4.025, 'M': 2.406, 'N': 6.749, 'O': 7.507, 'P': 1.929, 'Q': 0.095, 'R': 5.987, 'S': 6.327, 'T': 9.056, 'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150, 'Y': 1.974, 'Z': 0.074}

def Encrypt(besedilo,kljuc):
    kriptirano = ''
    kljuc_stevila = []
    besedilo_stevila = []
    for znak in kljuc:
        kljuc_stevila.append(abeceda[znak])
    for znak in besedilo:
        besedilo_stevila.append(abeceda[znak])

    dolzina = len(besedilo)
    i = 0
    while dolzina > 0:
        stevilo = (besedilo_stevila[i] + kljuc_stevila[i % len(kljuc)]) % 26
        kriptirano = kriptirano + list(abeceda.keys())[list(abeceda.values()).index(stevilo)]
        i += 1
        i = i%26
        dolzina -=1
    return kriptirano

def Decrypt(besedilo,kljuc):
    kriptirano = ''
    kljuc_stevila = []
    besedilo_stevila = []
    for znak in kljuc:
        kljuc_stevila.append(abeceda[znak])
    for znak in besedilo:
        besedilo_stevila.append(abeceda[znak])

    dolzina = len(besedilo)
    i = 0
    while dolzina > 0:
        stevilo = (besedilo_stevila[i] - kljuc_stevila[i % len(kljuc_stevila)]) % 26
        kriptirano = kriptirano + list(abeceda.keys())[list(abeceda.values()).index(stevilo)]
        i += 1
        dolzina -= 1
    return kriptirano


#1.2
from collections import Counter

def dolzine_kljuca(besedilo):
    # najprej poiščemo delčke, dolžine vsaj 3, ki se ponavljajo
    Ponovitve = []
    for i in range(len(besedilo)):
        for j in range(i,len(besedilo)):
            k=0
            while(besedilo[i+k] == besedilo[j+k] and (i+k)<len(besedilo)):
                k+=1
                if j == i:
                    break
                if i+k == len(besedilo) or j+k == len(besedilo):
                    break
            if k>= 3:
                Ponovitve.append(besedilo[i:i+k])
    #na katerih mestih so ponavljanja
    ponovitve = {}
    for ponovitev in Ponovitve:
        ponovitve[ponovitev] = []
        k = len(ponovitev)
        for i in range(len(besedilo)-k):
            beseda = ''
            for j in range(k):
                beseda += besedilo[i+j]
            if beseda == ponovitev:
                ponovitve[ponovitev].append(i)

    #koliko umesnih črk med ponavljanji
    razmiki = []
    for kluc in ponovitve.keys():
        seznam = ponovitve[kluc]
        for i in range(len(seznam)):
            for j in range(i+1,len(seznam)):
                razmiki.append(seznam[j] - seznam[i])

    #faktorji teh števil
    faktorji = []
    for stevilo in razmiki:
        i = 3
        while i <= stevilo:
            if stevilo % i == 0:
                faktorji.append(i)
            i+=1
    faktorji.sort()
    #kateri se ponovijo največkrat, tok naj bi bila dolžina kluca
    a = dict(Counter(faktorji))
    indeks = max(list(a.values()))
    #možne dolžine kluca
    resitve = []
    for kluc in a.keys():
        if a[kluc] == indeks:
            resitve.append(kluc)
    return resitve

#1.3
#ključ določimo tako da primerjamo pogostost črk v angleški abecedi in sicer
#tako da primerjamo odstotke pogostosti in vzamemo tistega,ki je najbližje
def ujemanje(besedilo):
    a = []
    #i = 0
    for znak in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        stevec = 0
        for crka in besedilo:
            if crka == znak:
                stevec += 1
        stevec = stevec/len(besedilo) *100
        a.append((stevec,znak))
    razlika = 0.0
    for stevilo, crka in a:
        razlika += abs(pogostost[crka] - stevilo)

    return razlika

def mozni_kjuci(besedilo, dolzina):
    razdelitev = [[] for i in range(dolzina)]
    for i in range(len(besedilo)):
        a = besedilo[i]
        razdelitev[i%dolzina].append(a)
    koncne = ''
    for delec in razdelitev:
        moznosti = []
        for znak in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            zamaknjeno = Decrypt(delec, znak)
            uje = ujemanje(zamaknjeno)
            moznosti.append((uje,znak))
        najboljsi = min(moznosti)
        stevilo, znak = najboljsi
        koncne = koncne + znak
    return koncne

dn= 'UTAHELHUSBXLZAZYMVXXGELAUOGDTEMOQRTUKGHCQRGTQNMUATMVASMYANZMARMOQLBIQRMPQSHMUTLWQOISQCTUNELADOGNQNHBSHMVYABUFABUUTLLJILAQNVLUNZYQAMLYEKNQNVPQSHUFHBZBOBUFTALBRXZQNMYQBXSXIHUNRHBSHMVGRKLBUUSUCMVMSXCQRXAQSMHZDMOQPKLEIWLZTBHXEELOTBVZOVJGRKPZGBUDEZBXAKJAUKZQDNYUNZATEKLNEESUOGHPDXKZOMHXIMAXEMVFHXZFRTPZTALETKPREHMFHXLXEVAUOGPEBNATUFHZNTAGRXWDAVAUCTSXYTWBLBLPTHATEYHOTLPZTALOALL'

#print(dolzine_kljuca(dn))
#print(mozni_kjuci(dn,4))
#print(Decrypt(dn,'MATH'))

#VIGENERJEVA ŠIFRA
#Ključ je dolžine 4.
#Ključ je 'MATH'
#Odkriptirano besedilo:
#ITHASLONGBEENAGRAVEQUESTIONWHETHERANYGOVERNMENTNOTTOOSTRONGFORTHELIBERTIESOFITSPEOPLECANBESTRONGENOUGHTOMAINTAINITSEXISTENCEINGREATEMERGENCIESONTHISPOINTTHEPRESENTREBELLIONBROUGHTOURREPUBLICTOASEVERETESTANDTHEPRESIDENTIALELECTIONOCCURRINGINREGULARCOURSEDURINGTHEREBELLIONADDEDNOTALITTLETOTHESTRAINTHESTRIFEOFTHEELECTIONISBUTHUMANNATUREPRACTICALLYAPPLIEDTOTHEFACTSINTHECASE

