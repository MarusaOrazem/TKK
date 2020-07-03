#prva domača naloga za TKK 2018/2019
#Maruša Oražem, 27151090, 2.letnik matematika

#2. naloga - Hillova šifra

abeceda = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

def inv(stevilo):
    for i in range(26):
        if (stevilo * i) %26 == 1:
            return i

#2.1
#ključ je matrika 2x2, podana bo kar z seznamom elementov
#če ima matrika v prvi vrstici elementa a in b, v drugi pa c in d
#bo naš ključ podan kot k = [a,b,c,d]
def EncryptH(besedilo,kljuc):
    if len(besedilo) % 2 == 1:
        besedilo = besedilo + 'A'
    kriptirano = ''
    besedilo_stevila = []
    for znak in besedilo:
        besedilo_stevila.append(abeceda[znak])
    for i in range(len(besedilo)//2):
        prva = besedilo_stevila[2*i]
        druga = besedilo_stevila[2*i + 1]
        nova1 = prva * kljuc[0] + druga * kljuc[1]
        nova1 = nova1 % 26
        nova2 = prva * kljuc[2] + druga * kljuc[3]
        nova2 = nova2 % 26
        kriptirano = kriptirano + list(abeceda.keys())[list(abeceda.values()).index(nova1)] + list(abeceda.keys())[list(abeceda.values()).index(nova2)]
    return kriptirano

def DecryptH(besedilo,kljuc):
    #determinanta mora biti obrljivo število v Z26
    det = (kljuc[0]*kljuc[3] - kljuc[2] * kljuc[1])%26
    det = inv(det)
    inverz = [(det*kljuc[3])%26, (-det*kljuc[1])%26, (-det*kljuc[2])%26, (det*kljuc[0])%26]
    return EncryptH(besedilo,inverz)


#2.1
#najti želimo ključ in dešifrirati besedilo. predpostavimo da je ključ matrika velikosti 2x2.
#v angleškem besedilu se največkrat pojavi dvojec 'th' in 'he',
#zato bomo v našem kriptiranem besedilu našli najpogostejša dvojca,
#predpostavili da se 'th' preslika v prvi dve in 'he' v drugi dve in na podlagi tega
#napisali našo 2x2 matriko.

def Hill_kljuc(besedilo):
    Ponovitve = []
    for i in range(len(besedilo)):
        for j in range(i, len(besedilo)):
            k = 0
            while (besedilo[i + k] == besedilo[j + k] and (i + k) < len(besedilo)):
                k += 1
                if j == i:
                    break
                if i + k == len(besedilo) or j + k == len(besedilo):
                    break
            if k == 2:
                Ponovitve.append(besedilo[i:i + k])
    pojavitve = []
    for ponovitev in Ponovitve:
        i = 0
        j=0
        while j+1 < len(besedilo):
            beseda = besedilo[j] + besedilo[j+1]
            if beseda == ponovitev:
                i+= 1
            j+=1
        if (i,ponovitev) in pojavitve:
            pass
        else:
            pojavitve.append((i, ponovitev))
    pojavitve.sort()
    pojavitve.reverse()
    prvi = pojavitve[0][1]
    drugi = pojavitve[1][1]
    th = [19,7]
    he = [7,4]
    prvist=[]
    drugist=[]
    for znak in prvi:
        prvist.append(abeceda[znak])
    for znak in drugi:
        drugist.append(abeceda[znak])
    #Rešimo sistem enačb
    #A,B,C,D neznanke ključa matrike K
    #Kx = y
    x = [19,7,7,4]
    y = [prvist[0], drugist[0], prvist[1], drugist[1]]
    det = (x[0] * x[3] - x[1] * x[2])%26
    det = inv(det)
    A = (det*(y[0]*x[3] - y[1]*x[2]))%26
    B = (det*(-x[1]*y[0] + x[0]*y[1]))%26
    C = (det*(y[2]*x[3] - y[3]*x[2]))%26
    D = (det*(-x[1]*y[2] + x[0]*y[3]))%26
    return [A,B,C,D]

hillova = 'STSQALWTCJMIJMTHNFEBWZTVJWMRNNHPMFICJFNWSZSXGWPFHHAJFBNTWZTVTHIRMRCGVRJTAFXBWDIVMFWSNSTVLXIRACANWLYSIYVPJQMQNFLNMRPXSBHMWNJTIYNSZNHPHPIMNZDRWBPPNSHMSBUJMUHZXJHMWPSQHHJBMHHMWMJTAFXBWDICVETVLXIRANXFVETVUDWUHBWHEBMBSXHMWEEEHMANWUJUWWHAWWSNWZMLJXVXHWTVJTZZICACHHJTNWWTZRHWWTIYJSSUWSNSTVLWWWWHHPNSTVSNWWIYNSSOPFHMWEWHMHHMWNJTIYNSXPCQJTOQYFPBQKHMWEWHMHHMWNACHRNWHMWBSZWSIOGIICVETVLWWWWHHXANZRVZYWXUMVWZHDJHXAANHRUQZZOUNBTZTJFNSBUUMBVZSTTLHZXNWDTZELTVPPAJWTICVETVNNHPMFVZYWXUTVXBAJSQIUWWMHHMWNACHTGCTJIRGFCGVGSBYAPQITSDWISVPPNNZMWCIRMSFRSXHMWZEENFGDVBMHSYOYJHPBHLANXNNZVOSUSANTCVTVUMPSIATHYFAHEGCSPBWKNZMFWUYFIKXBMHHMWAAZWGJJAHSSWKVJANANXFVMAFSENLHMWBLZNDHMSBUJMNALWUFRSXWDMFWSVBTHLLJTYOSQWHYAGJHDJTXNNSTVMXTVJH'


#print(Hill_kljuc(hillova))
#print(DecryptH(hillova, [25,0,5,3]))

#HILLOVA ŠIFRA

#primer
#primer = EncryptH('MARUSIJEUSPELORESITIDOMACONALOGO', [1,5,2,3])
#desifrirano = DecryptH(primer,[1,5,2,3])
#kot vidimo, ko poženemo DecryptH na EncryptH, dobimo nazaj prvotno besedilo
#matrika (ključ), mora imeti obrljivo determinanto v tej grupi


#moj program ne bi deloval za matrike višjih dimenzij, saj je bilo uporabljenih preveč predpostavk
#ki so se navezovale na dolžino ključa, kot naprimer inverz 2x2 matrike

#ključ besedila je matrika, ki ima v prvi vrstici [25,0], v drugi pa [5,3]
#Odkriptirano besedilo:
#ITISAVERYPOORTHINGWHETHERFORNATIONSORINDIVIDUALSTOADVANCETHEHISTORYOFGREATDEEDSDONEINTHEPASTASANEXCUSEFORDOINGPOORLYINTHEPRESENTBUTITISANEXCELLENTTHINGTOSTUDYTHEHISTORYOFTHEGREATDEEDSOFTHEPASTANDOFTHEGREATMENWHODIDTHEMWITHANEARNESTDESIRETOPROFITTHEREBYSOASTORENDERBETTERSERVICEINTHEPRESENTINTHEIRESSENTIALSTHEMENOFTHEPRESENTDAYAREMUCHLIKETHEMENOFTHEPASTANDTHELIVEISSUESOFTHEPRESENTCANBEFACEDTOBETTERADVANTAGEBYMENWHOHAVEINGOODFAITHSTUDIEDHOWTHELEADERSOFTHENATIONFACEDTHEDEADISSUESOFTHEPASTSUCHASTUDYOFLINCOLNSLIFEWILLENABLEUSTOAVOIDTHETWINGULFSOFIMMORALITYANDINEFFICIENCYTHEGULFSWHICHALWAYSLIEONEONEACHSIDEOFTHECAREERSALIKEOFMANANDOFNATIONITHELPSNOTHINGTOHAVEAVOIDEDONEIFSHIPWRECKISENCOUNTEREDINTHEOTHERA

