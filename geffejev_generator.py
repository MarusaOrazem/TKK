#druga domača naloga za TKK 2018/2019
#Maruša Oražem, 27151090, 2.letnik matematika

#program razbije geffejev generator, sestavljen iz treh LFSR-jev.
#izhodni bit generatorja je enak z = x1*x2 + x2*x3 + x3 (mod2)

abeceda = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

#zakriptirano besedilo, ki ga želimo razbiti(iz spletne učilnice)
DN2= '01100111011111111001100011111010101011100111101100011111100100111000111010010110111110110110111010000000011000100110111011001110000110010111010010011000101110001000000101011101011101011110111111110110110111001000100000100011101000000011110010110110100011100101100100111011011111011000100010111010110011101001001111100100100011000111011110001001011111010110011101010011010111010010000010000001000100001101010111010011100100011111010111111011100011000011000001111000101110100110101100011111000110010011100010101100011110101001101000101010101001001111111101101110110111010010110010010111100111111110000000010001010011101000001010010101111000111101100000000111111111010100111010010000110011000111111101011010001001110101101010101101101100101101011101000010011111110010001010101000101011111101110000100101110001110111010011101101110011000111000110000001010111101100000011000111100110101100111010000000111010110111101110000001010100110111000010001111000001110110100000101110010101111110001110010101000100100011000010010100001100001111010110101001111111100110010110110010010000001000110000011010101010100011010111100011100011100001011110111110110111010100010100001010101111101111010011011010101111011111110100100010110110111001101100010100001101101000111100111011101011110010001011010001110000000111000011010011000111000101011100101100001011100011011110110001100001000111011101010101011010101011100100110010001111110001011000011011000100011111001100100110110001100110001000100101100101101010010100010011001111111101010001000111110110100011000000001011000000001101111001000000011011000011001001000001000001100010100110100101111001010101100110111011111001100100101101011110011011101100010110111100110100111110000010000101100011010111000000100111110100111011110001101001011000010101111111001111010001000101001110110000000101001111011010010011010100001101110000110011010101001001011100100110100010010011010111100101110001110000110111001011100100011100101111110111100110111111011110111110111101110010111000101001011101011000110011111011001000110001101010110100100011011010000110011111101000010010111010111010110000010011010000011110111100101110010010001100001010110110100101111000011001011101100010100011111001001011010101111111010101010110101000100101011011110000111100000101011100011110010000110010100000010100100011001000000100101010000011110111000100111010011000100000111001001011000011001011010100001010000001101111001001100100011101111001111101000010011010011111100110001111111011100101111000101010111000110010001000011010011101100000001101010000001101101000100111101000001110111001110100101110001100001110111110101110101111011110000010001100111101101011100101011000001101010101010110000111100010101101011110001000010001111100100101110110110010011110110010011001010001101100101011000001011101010001010110000010101111111100000111100111110010111101001010110000000100101000101111110111011110101110101010111100101000111101000101011000101100110000010000011010101000011001101110111110100111011111011001101001011001100000111011101110'


#LFSR1 ima v našem primeru karakteristični polinom enak p1(x) = x^5 + x^2 + 1, m1 = 6
#LFSR2 pripada p2(x) = x^7 + x^1 + 1, m2 = 8
#LFSR3 pripada p3(x) = x^11 + x^2 + 1, m3 = 12
#iz tega vemo rekurzivno zvezo in znamo naprej sestavljati ključ.


#vsaka LSFR funkcija sprejme besedilo, na podlagi dolžine le tega, pa bomo sestavili kjuč, ki bo dolg kot dano besedilo
#funkcija sprejme tudi začetno stanje ključa(stevilo v bitnem zapisu), ki ga rabimo za rekurzivno nadaljevanje
def LFSR1(besedilo, zac_kluc):
    #sestavimo cel kjuč, dolžine enake kot besedilo
    kluc = zac_kluc
    for indeks in range(5,len(besedilo)):
        kluc += str((int(kluc[indeks-2]) + int(kluc[indeks-5]))%2) #rekurzivno zvezo dobimo iz karakterističnega polinoma p1
    return kluc


def LFSR2(besedilo, zac_kluc):
    #sestavimo cel kjuč, dolžine enake kot besedilo
    kluc = zac_kluc
    for indeks in range(7,len(besedilo)):
        kluc += str((int(kluc[indeks-1]) + int(kluc[indeks-7]))%2) #rekurzivno zvezo dobimo iz karakterističnega polinoma p2
    return kluc


def LFSR3(besedilo, zac_kluc):
    #sestavimo cel kjuč, dolžine enake kot besedilo
    kluc = zac_kluc
    for indeks in range(11,len(besedilo)):
        kluc += str((int(kluc[indeks-2]) + int(kluc[indeks-11]))%2) #rekurzivno zvezo dobimo iz karakterističnega polinoma p3
    return kluc


#iz ključev dobljenih v LFSR funkcijah, sedaj lahko sestavimo geffejev generator, dolzine enake ključem iz LFSR funkcij
def geffe_generator(kluc1,kluc2,kluc3):
    kluc = ''
    for i in range(len(kluc1)):
        nov = (int(kluc1[i])*int(kluc2[i]) + int(kluc2[i])*int(kluc3[i]) + int(kluc3[i]))%2 #izhodni bit generatorja je enak z = x1*x2 + x2*x3 + x3 (mod2)
        kluc += str(nov)
    return kluc

#funkcija nam iz danega besedila, vrne besedilo podano v bitih.
#pomeni, da za vsako črko, poišče njeno vrednost v zgornjem slovarju 'abeceda'
#in to število spremeni v bitno število
#števila skupaj 'zlepi' v niz
def besedilo_v_bite(besedilo):
    vbitih = ''
    for znak in besedilo:
        vrednost = abeceda[znak]
        bin_vrednost = str(bin(vrednost)[2:]) #naprimer bin(5) vrne '0b101', odstranimo začetne dva znaka, dobimo '101'
        dolzina = len(bin_vrednost)
        while dolzina != 5: #popravimo bitni zapis, da bo enak dolžine 5, naprimer '101' bo sedaj '00101'
            bin_vrednost = '0' + bin_vrednost
            dolzina += 1
        vbitih += bin_vrednost
    return vbitih

#predpostavimo da vemo, da je začetni del našega zakriptiranega besedila enak 'CRYPTOGRAPHY'
uganjeno_besedilo = 'CRYPTOGRAPHY'
#spremenimo ga v 'bitno besedilo'
uganjeno_besedilo_biti = besedilo_v_bite(uganjeno_besedilo)

#iz teorije vemo, da če XOR-amo uganjeno besedilo in zakriptirano besedilo
#bomo dobili ravno izhod, ki ga mora dati geffejev generator, ta izhod označimo z zac_vrednost
#na podlagi tega bomo razpili celotno besedilo
zac_vrednost = ''
for i in range(len(uganjeno_besedilo_biti)):
    novo = (int(uganjeno_besedilo_biti[i]) + int(DN2[i]))%2
    zac_vrednost += str(novo)


#napisala bom program, ki smo ga tudi napisali na vajah (za iskanje ključa)

#iz teorije vemo, da se mora izhod LFSR1 ujemati z geffejevim izhodom (zac_vrednost) v 75%.
#za iskanje le tega, rabimo pregledati vse možnosti začetnih kjučev in vzeti tistega, ki temu ustreza

#sestavimo vse možnosti začetnih ključev za LFSR1 (dalo bi se lepše napisat)
moznosti1 = []
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    moznost = str(i) + str(j) +str(k) + str(l) + str(m) #sestavimo skupaj vse možne nize iz 0 in 1, dolžine 5
                    if moznost not in moznosti1:
                        moznosti1.append(moznost)

resitev1 = ''
for moznost in moznosti1:
    #za vsako možnosti izračunamo ključ
    x1 = LFSR1(zac_vrednost, moznost)
    #preverimo ujemanje
    ujemanje = 0
    for i in range(len(x1)):
        if x1[i] == zac_vrednost[i]:
            ujemanje += 1
    procenti = (ujemanje*100)/len(zac_vrednost)
    if procenti > 75:
        resitev1 =  (moznost,x1) #shranimo si začetni ključ in celotni ključ, bomo rabili v nadaljevanju

#prav tako vemo, da se mora izhod LFSR3 ujemati z geffejevim v 75%

#sestavimo vse možnosti za začetni ključ LFSR3
moznosti3 = []
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    for n in range(2):
                        for o in range(2):
                            for p in range(2):
                                for r in range(2):
                                    for s in range(2):
                                        for t in range(2):
                                            #enako kot prej, sestavimo vse možnosti začetnih ključev iz 0 in 1, tokrat dolžine 11
                                            moznost = str(i) + str(j) +str(k) + str(l) + str(m) +str(n) + str(o) +str(p) + str(r) + str(s) +str(t)
                                            if moznost not in moznosti3:
                                                moznosti3.append(moznost)
    

#postopek enak kot za iskanje LFSR1
resitev3 = ''
for moznost in moznosti3:
    x3 = LFSR3(zac_vrednost, moznost)
    ujemanje = 0
    for i in range(len(x3)):
        if x3[i] == zac_vrednost[i]:
            ujemanje += 1
    procenti = (ujemanje*100)/len(zac_vrednost)
    if procenti > 75:
        resitev3 =  (moznost,x3)

#sedaj ko imamo začetna ključa za LFSR1 in LFSR3, moramo samo še pregledati vse možnosti za LFSR2
moznosti2 = []
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    for n in range(2):
                        for o in range(2):
                            #tokrat dolžine 7
                            moznost = str(i) + str(j) +str(k) + str(l) + str(m) +str(n) + str(o)
                            if moznost not in moznosti1:
                                moznosti2.append(moznost)


#za vsako možnosti za drugi ključ, sestavimo geffejev generator.
#ujemat se more z izhodom, ki smo ga določili na začetku, sepravi z zac_vrednost
resitev2 = ''
for moznost in moznosti2:
    x2 = LFSR2(zac_vrednost, moznost)
    g = ''
    for i in range(len(zac_vrednost)):
        g += str((int(resitev1[1][i]) * int(x2[i]) + int(x2[i]) * int(resitev3[1][i]) + int(resitev3[1][i])) % 2) #sestavimo generator iz začetnih ključev
    if g == zac_vrednost:
        resitev2 = (moznost,x2)


#sedaj poznamo začetne ključe, sestavimo jih do konca, sepravi kot je dolžina našega besedila.
prvi_kluc = LFSR1(DN2,resitev1[0])
drugi_kluc = LFSR2(DN2,resitev2[0])
tretji_kluc = LFSR3(DN2,resitev3[0])

#iz teh ključev sestavimo celotni geffejev generator
geffe_ceu = geffe_generator(prvi_kluc,drugi_kluc,tretji_kluc)

#sedaj zakriptirano besedilo XOR-amo s tem kjučem
resitev = ''
for i in range(len(DN2)):
    resitev += str((int(geffe_ceu[i]) + int(DN2[i]))%2)

#dobljeno besedilo 0 in 1 sedaj spremenimo nazaj v abecedo
koncna = ''
for i in range(0,len(resitev),5):
    koncna += list(abeceda.keys())[list(abeceda.values()).index(int(resitev[i:i+5],2))]

#to je naše odkriptirano besedilo
print(koncna)
#CRYPTOGRAPHYPRIORTOTHEMODERNAGEWASEFFECTIVELYSYNONYMOUSWITHENCRYPTIONTHECONVERSIONOFINFORMATIONFROMAREADABLESTATE
#TOAPPARENTNONSENSETHEORIGINATOROFANENCRYPTEDMESSAGEALICESHAREDTHEDECODINGTECHNIQUENEEDEDTORECOVERTHEORIGINALINFORMATION
#ONLYWITHINTENDEDRECIPIENTSBOBTHEREBYPRECLUDINGUNWANTEDPERSONSEVEFROMDOINGTHESAMETHECRYPTOGRAPHYLITERATUREOFTENUSESALICEAFOR
#THESENDERBOBBFORTHEINTENDEDRECIPIENTANDEVEEAVESDROPPERFORTHEADVERSARYSINCETHEDEVELOPMENTOFROTORCIPHERMACHINESINWORLD
#WARIANDTHEADVENTOFCOMPUTERSINWORLDWARIITHEMETHODSUSEDTOCARRYOUTCRYPTOLOGYHAVEBECOMEINCREASINGLYCOMPLEXANDITSAPPLICATIONMOREWIDESPREAD























        
